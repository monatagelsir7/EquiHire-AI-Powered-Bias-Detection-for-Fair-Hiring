import pyreadr
import pandas as pd
import numpy as np

def load_data():
    """
    Directly access the rData as dataframe
    """
    data = pyreadr.read_r('resume.rda')['resume'] # pathway
    df = pd.DataFrame(data)

    return df
