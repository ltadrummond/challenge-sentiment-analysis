import seaborn as sns
from functions import plot_counting_sentiments
import pandas as pd
import matplotlib.pyplot as plt
from functions import word_cloud

df = pd.read_csv('../data/df_sentiments_blob.csv')
plot_counting_sentiments(df)
word_cloud(df)
