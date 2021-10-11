from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import re
import string

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Authentication
consumer_key = '4jR2O9wrSf41jptgt5sq0iRAr'
consumer_secret = 'Y6lLPdwAFRuVtzaclpnimjo8OHsvHHEECeh8Ing5CoxBIPGMZV'
access_token = '1447462589294948353-10TUag7uxO8Sshl7oLsgzKuPbKH33o'
access_token_secret = 'fYXKMZbqxRTA4jWpTEiaJV9XU3asuZKJ4YCr2Nu24Yr3R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)