import re
import string
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
import re
import string
from nltk.tokenize import word_tokenize
import twint
import plotly.express as px
import matplotlib.pyplot as plt


def prepare_df_to_clean_tweets(df):
    df = df[df['language'] == 'en']
    df = df.drop(columns=['id', 'conversation_id', 'created_at', 'date', 'time', 'timezone', 'user_id', 'username',
                          'name', 'place', 'mentions', 'urls', 'photos', 'replies_count', 'retweets_count',
                          'likes_count', 'hashtags',
                          'cashtags', 'link', 'retweet', 'quote_url', 'video', 'thumbnail', 'near', 'geo', 'source',
                          'user_rt_id', 'user_rt',
                          'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src', 'trans_dest'])
    df = df.drop_duplicates()
    return df

def clean_tweets(text):
    cleaned_sentence = text.lower()
    cleaned_sentence = re.sub('[0-9]+', '', cleaned_sentence)
    cleaned_sentence = "".join([i for i in cleaned_sentence if i not in string.punctuation])
    number_words = len(cleaned_sentence.split())
    if number_words > 256:
        cleaned_sentence = cleaned_sentence.split()[:256]
        cleaned_sentence = ' '.join(cleaned_sentence)
    cleaned_sentence= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())
    cleaned_sentence= text.lower().replace('-', ' ')
    table= str.maketrans('', '', string.punctuation+string.digits)
    cleaned_sentence = text.translate(table)
    # tokenizing words
    tokens = word_tokenize(cleaned_sentence)
    # stemming the words
    cleaned_sentence = ' '.join(words)
    return cleaned_sentence


def word_cloud(df):
    text = " ".join(tweet for tweet in df.cleaned_tweet)
    # Create and generate a word cloud image:
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white")
    wc.generate(text)
    plt.figure(figsize=[10,10])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def get_tweets(tweet_keyword):
    t = twint.Config()
    t.Search = tweet_keyword
    t.Lang = "en"
    t.Limit = 100
    t.Pandas = True
    twint.run.Search(t)
    twint_df = twint.storage.panda.Tweets_df
    return twint_df

def sentiment_score_blob(tweet):
    analysis = TextBlob(tweet)
    senti= analysis.sentiment.polarity
    if senti<0:
        emotion = "Negative"
    elif senti>0:
        emotion = "Positive"
    else:
        emotion = "Neutral"
    return emotion

def plot_counting_sentiments(df):
    fig = px.histogram(df, x="sentiment")
    fig.update_layout(bargap=0.2)
    return fig.show()
