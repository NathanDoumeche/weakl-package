import src.weakl.adaptive as adapt
import src.weakl.additive_model as additive
from src.weakl.utils import device, dataset_load
import pandas as pd
import numpy as np


def test_dataset():
    df = dataset_load()
    columns = ["date", "tod", 
            "Load", "Load_d1", "Load_d7",
            "temperature_smooth_950", "temperature", "temperature_max_smooth_990", 'temperature_min_smooth_950',
                'toy', 'day_type_week', "day_type_jf"]
    data = df[columns].copy()
    data['day_type_week']=np.float64(data.loc[:,'day_type_week'])
    data.rename(columns={'date':'Time'}, inplace=True)
    n = len(data['Time'])
    data['time'] = [i/n*np.pi for i in range(n)]
    assert True