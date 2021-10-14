import seaborn as sns
from functions import plot_counting_sentiments
import pandas as pd
import matplotlib.pyplot as plt
from functions import word_cloud

df = pd.read_csv('../data/sentiment_data_frame.cvs')
plot_counting_sentiments(df)
word_cloud(df)
