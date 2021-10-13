import twint

t = twint.Config()
t.Search = "SquidGame"
t.Lang = "en"
t.Limit = 10000
t.Pandas = True
t.Store_csv = True
t.Output = "tweets_df_squid.csv"
twint.run.Search(t)