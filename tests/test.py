import src.weakl.adaptive as adapt
import src.weakl.additive_model as additive
from src.weakl.utils import device, dataset_load
import pandas as pd
import numpy as np

def test_dataset():
    assert dataset_load()