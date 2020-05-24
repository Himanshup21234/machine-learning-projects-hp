import os as os
import sys
import pandas as pd
import math
import numpy as np
import random as rand

df=pd.read_csv("abc.csv",nrows=100)
print(df.head())
print(df.sentiment.value_count())
