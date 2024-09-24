import sys
import os
from pandas import DataFrame
import pandas as pd

# Dynamically add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)

if src_dir not in sys.path:
    sys.path.append(src_dir)


def add_revenue(df: DataFrame) -> DataFrame:

    dfs = []

    if df['Type'].str.contains('Generating Unit', na=False).any():
        gen_unit = df[df['Type'] == 'Generating Unit']
        gen_unit['FINALMW'] = gen_unit['INITIALMW'].shift(-1)
        gen_unit['REVENUE_MW'] = (gen_unit['FINALMW'] + gen_unit['INITIALMW']) / 2
        gen_unit['REVENUE_MW'] = gen_unit['REVENUE_MW'].dropna()
        dfs.append(gen_unit)

    if df['Type'].str.contains('Load', na=False).any():
        load_unit = df[df['Type'] == 'Load']
        load_unit['FINALMW'] = load_unit['INITIALMW'].shift(-1)
        load_unit['REVENUE_MW'] = (load_unit['FINALMW'] + load_unit['INITIALMW']) / 2
        load_unit['REVENUE_MW'] = load_unit['REVENUE_MW'].dropna()
        dfs.append(load_unit)

    if df['Type'].str.contains('Bi-Directional Unit', na=False).any():
        bi_unit = df[df['Type'] == 'Bi-Directional Unit']
        bi_unit['FINALMW'] = bi_unit['INITIALMW'].shift(-1)
        bi_unit['REVENUE_MW'] = (bi_unit['FINALMW'] + bi_unit['INITIALMW']) / 2
        bi_unit['REVENUE_MW'] = bi_unit['REVENUE_MW'].dropna()
        
        # Pre-Check when it comes to Bi-Directional units, the same Battery should not
        # be dispatched using 'Bi-Directional Unit' and 'Load/Generation' at the same time
        result_load = df.groupby('SETTLEMENTDATE').filter(
        lambda x: ('Load' in x['Type'].values and 
                'Bi-Directional Unit' in x['Type'].values and 
                (x.loc[x['Type'] == 'Load', 'TOTALCLEARED'].values[0] > 0) and 
                (x.loc[x['Type'] == 'Bi-Directional Unit', 'TOTALCLEARED'].values[0] > 0))
        )
        if not result_load['TOTALCLEARED'].empty:
            raise Exception("Load and Bi-Directional Unit have TOTALCLEARED at the same time")
        
        result_generation = df.groupby('SETTLEMENTDATE').filter(
        lambda x: ('Generating Unit' in x['Type'].values and 
                'Bi-Directional Unit' in x['Type'].values and 
                (x.loc[x['Type'] == 'Generating Unit', 'TOTALCLEARED'].values[0] > 0) and 
                (x.loc[x['Type'] == 'Bi-Directional Unit', 'TOTALCLEARED'].values[0] > 0))
        )
        if not result_generation['TOTALCLEARED'].empty:
            raise Exception("Generating Unit and Bi-Directional Unit have TOTALCLEARED at the same time")
        
        dfs.append(bi_unit)

    if not dfs:
        return -1

    df = pd.concat(dfs, ignore_index=True)
    
    price_columns = ['RRP', 'RAISE6SECRRP', 'RAISE60SECRRP', 'RAISE5MINRRP', 'RAISEREGRRP', 'LOWER6SECRRP', 'LOWER60SECRRP', 'LOWER5MINRRP', 'LOWERREGRRP']

    # These new columns were added in August 2023, therefore these columns should exist
    # only after this timeframe, else we compute without this.
    price_columns_to_check = ['LOWER1SECRRP', 'RAISE1SECRRP']
    for col in price_columns_to_check:
        if col in df.columns:
            price_columns.append(col)
    
    # Need to calculate with MWh and not Mw, since power is dispatched every 5 min, we divide by 12 to calculate MWh
    generation_mw_columns = ['REVENUE_MW', 'RAISEREG', 'RAISE6SEC', 'RAISE60SEC', 'RAISE5MIN', 'LOWERREG', 'LOWER6SEC', 'LOWER60SEC', 'LOWER5MIN']
    
    generation_columns_to_check = ['LOWER1SEC', 'RAISE1SEC']
    for col in generation_columns_to_check:
        if col in df.columns:
            generation_mw_columns.append(col)

    dispatch_interval = 12 # Power is dispatched every 5 min in 1 hour.

    for column in generation_mw_columns:
        df[column] = df[column] / dispatch_interval

    for column in price_columns:
        if column not in df.columns:
            return -1
    
    df.loc[df['Type'] == 'Generating Unit', 'REVENUE'] = df['REVENUE_MW'] * df['RRP']
    df.loc[df['Type'] == 'Bi-Directional Unit', 'REVENUE'] = df['REVENUE_MW'] * df['RRP']
    df.loc[df['Type'] == 'Load', 'REVENUE'] = df['REVENUE_MW'] * df['RRP'] * -1
    df.shift()

    df['RAISEREGREVENUE'] = df['RAISEREGRRP'] * df['RAISEREG']
    df['LOWERREGREVENUE'] = df['LOWERREGRRP'] * df['LOWERREG']
    df['LOWER6SECREVENUE'] = df['LOWER6SECRRP'] * df['LOWER6SEC']
    df['LOWER60SECREVENUE'] = df['LOWER60SECRRP'] * df['LOWER60SEC']
    df['LOWER5MINREVENUE'] = df['LOWER5MINRRP'] * df['LOWER5MIN']
    df['RAISE6SECREVENUE'] = df['RAISE6SECRRP'] * df['RAISE6SEC']
    df['RAISE60SECREVENUE'] = df['RAISE60SECRRP'] * df['RAISE60SEC']
    df['RAISE5MINREVENUE'] = df['RAISE5MINRRP'] * df['RAISE5MIN']
    
    if 'RAISE1SEC' in df.columns:
        df['RAISE1SECREVENUE'] = df['RAISE1SECRRP'] * df['RAISE1SEC']
    
    if 'LOWER1SEC' in df.columns:
        df['LOWER1SECREVENUE'] = df['LOWER1SECRRP'] * df['LOWER1SEC']
        
    return df