#SENTIMENT ANALYSIS
analysis = TextBlob(tweet)
            senti= analysis.sentiment.polarity
            # labeling the sentiment
            if senti<0 :
              emotion = "NEG"
            elif senti>0:
              emotion= "POS"
            else:
              emotion= "NEU"
            # appending all data
            tweets.append((tweet, senti, emotion))

#PD TO DATAFRAME
df= pd.DataFrame(tweets, columns= ['tweets', 'senti', 'emotion'])
# droping retweets
df= df.drop_duplicates()


#WORD CLOUD
def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                                and not word.startswith('#')
                                and word != 'rt'
                            ])
    wordcloud = WordCloud(
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    # using matplotlib to display the images in notebook itself.
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
df_pos = df[ df['emotion'] == 'POS']
df_pos = df_pos['tweets']
wordcloud_draw(df_pos, 'white')
