import sys
import os
from pandas import DataFrame
import pandas as pd
import numpy as np

# Dynamically add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)

if src_dir not in sys.path:
    sys.path.append(src_dir)

def filter_battery(df: DataFrame, station_name:str) -> DataFrame:
    
    df = df[df['Station Name'] == station_name]
    
    if 'BBATTERY' in df['DUID'].values:
        df['DUID'] = df['DUID'].replace('BBATTERY', 'BBATRYG1')

    if 'DALNTH01' in df['DUID'].values:
        df['DUID'] = df['DUID'].replace('DALNTH01', 'DALNTH1')

    df['Base_DUID'] = np.where(df['Type'] == 'Bi-Directional Unit', df['DUID'].str[:-1],
                      np.where((df['Type'] == 'Generating Unit') | (df['Type'] == 'Load'), df['DUID'].str[:-2], np.nan))

    return df