import re
import string
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
import re
import pandas as pd
from textblob import TextBlob
import csv
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
n_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import streamlit as st
import twint

porter = PorterStemmer()
lemmatizer = WordNetLemmatizer()
#nltk.download('punkt')
#nltk.download('wordnet')
import demoji


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
    stopwords = nltk.corpus.stopwords.words('english')
    cleaned_sentence = text.lower()
    cleaned_sentence = re.sub('[0-9]+', '', cleaned_sentence)
    cleaned_sentence = "".join([i for i in cleaned_sentence if i not in string.punctuation])
    number_words = len(cleaned_sentence.split())
    if number_words > 256:
        cleaned_sentence = cleaned_sentence.split()[:256]
        cleaned_sentence = ' '.join(cleaned_sentence)
    # removing @ tags and links from the text
    cleaned_sentence= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())
    # converting all letters to lower case and relacing '-' with spaces.
    cleaned_sentence= text.lower().replace('-', ' ')
    # removing stowards and numbers
    table= str.maketrans('', '', string.punctuation+string.digits)
    cleaned_sentence= text.translate(table)
    # tokenizing words
    tokens = word_tokenize(cleaned_sentence)
    # stemming the words
    stemmed = [porter.stem(word) for word in tokens]
    words = [w for w in stemmed if not w in n_words]
    cleaned_sentence = ' '.join(words)
    return cleaned_sentence


def convert_emoji(tweet):
    dict_emojis = demoji.findall(tweet)
    for emoji, emoji_word in dict_emojis.items():
        tweet = tweet.replace(emoji, f' {emoji_word}')
    return tweet


def create_word_cloud(text: str, image_path=None):
    st.write('Creating Word Cloud..')

    text = clean_text(text)

    if image_path == None:

        # Generate the word cloud
        word_cloud = WordCloud(width=600, height=600,
                              background_color='white',
                              stopwords=STOPWORDS,
                              min_font_size=10).generate(text)

    else:
        mask = np.array(Image.open(image_path))
        word_cloud = WordCloud(width=600, height=600,
                              background_color='white',
                              stopwords=STOPWORDS,
                              mask=mask,
                              min_font_size=5).generate(text)

        # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(word_cloud, interpolation='nearest')
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()


def get_tweets(tweet_keyword):
    t = twint.Config()
    t.Search = tweet_keyword
    t.Lang = "en"
    t.Limit = 10000
    t.Pandas = True
    t.Store_csv = True
    t.Output = "tweets_df_squid.csv"
    twint.run.Search(t)

