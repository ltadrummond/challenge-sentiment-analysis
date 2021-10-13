from functions import *

df = pd.read_csv('../data/tweets_df_squid.csv')
print(df.head())
print(df.shape) # 11600 tweets
print(df.duplicated().value_counts()) #no duplicates
print(df.duplicated().isnull())


df = prepare_df_to_clean_tweets(df)
df['cleaned_tweet'] = df['tweet'].apply(lambda x: clean_tweets(x))

