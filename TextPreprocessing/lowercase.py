# at the time of tokenization we python think Basic and basic are different
# this is the additional complexity in our model.

import pandas as pd

df = pd. read_csv('filepath')

df['text_column'] = df['text_column'].str.lower()