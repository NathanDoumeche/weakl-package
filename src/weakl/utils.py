import numpy as np
import pandas as pd
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def is_running_on_gpu():
  if torch.cuda.is_available():
    print("The algorithm is running on GPU.")
  else:
    print("The algorithm is not running on GPU.")

torch.set_default_dtype(torch.float64)
np_dtype = np.float64


def dataset_load():
    url = "https://zenodo.org/records/10041368/files/dataset_national.csv"
    df = pd.read_csv(url)
    return df
