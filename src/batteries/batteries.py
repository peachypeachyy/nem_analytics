import sys
import os
from pandas import DataFrame
from abc import ABC, abstractmethod
import pandas as pd

# Dynamically add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)

if src_dir not in sys.path:
    sys.path.append(src_dir)

from batteries.helpers.filter_battery import filter_battery
from batteries.helpers.add_revenue import add_revenue

class Batteries(ABC):

    @abstractmethod
    def add_revenue(self, df: DataFrame) -> DataFrame:
        pass

class HornsdaleBattery(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Hornsdale Power Reserve')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class VictorianBigBattery(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Victorian Big-Battery')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class DalrympleNorthBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Dalrymple North BESS')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class LakeBonneyBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Lake Bonney BESS1')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class WandoanBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Wandoan Battery Energy Storage System (BESS)')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class BallaratBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Ballarat Battery Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class WallgroveBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Wallgrove BESS 1')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class GannawarraBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Gannawarra Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class TorrensIslandBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Torrens Island BESS')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class HazelWoodBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Hazelwood Battery Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class BouldercombeBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Bouldercombe Battery Project')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class RiverinaEnergyStorageSystem1(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Riverina Energy Storage System 1')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class RiverenaEnergyStorageSystem2(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Riverena Energy Storage System 2')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class BulganaGreenPowerHub(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Bulgana Green Power Hub')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class QueanbeyanBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Queanbeyan BESS')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class DarlingtonPointEnergyStorageSystem(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Darlington Point Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class ChinchillaBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Chinchilla BESS, Units 1-80')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class BrokenHillBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Broken Hill Battery Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class CapitalBattery(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Capital Battery')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)
    

class TailemBend2(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Tailem Bend 2 Hybrid Renewable Power Station')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class WesternDownsBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Western Downs Battery Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class AdelaideDesalinationPlant(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Adelaide Desalination Plant')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class BlythBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Blyth Battery Energy Storage System')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class ChristiesBeachWastewaterTreatmentPlant(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Christies Beach Wastewater Treatment Plant')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)


class HappyValleyWaterTreatmentPlant(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Happy Valley Water Treatment Plant')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)

    
class KennedyEnergyParkBattery(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Kennedy Energy Park Battery')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)
    
class PhillipIslandBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Phillip Island BESS')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)
    
class RangebankBESS(Batteries):
    
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        self.battery = filter_battery(self.df, 'Rangebank BESS')
    
    def add_revenue(self, df: DataFrame) -> DataFrame:
        return add_revenue(df)