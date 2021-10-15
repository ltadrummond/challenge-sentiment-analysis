import pandas as pd
import numpy as np
from textblob import TextBlob
from functions import sentiment_score_blob

df = pd.read_csv('../data/final_df')
df['sentiment'] = df['cleaned_tweet'].apply(lambda x: sentiment_score_blob(x[:500]))
df.to_csv('df_sentiments_blob.csv')

# try:
# st.write('The overall feeling about this Twitter tag is: ' tweets_df.cleaned_tweet.agg(average))
# try:
# plots_inclued