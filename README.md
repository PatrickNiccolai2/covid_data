# covid_data

old_data contains data from: https://ourworldindata.org/coronavirus and https://www.unicef.org/supply/covid-19-market-dashboard, which we currently aren't using but may incorporate in the future. 

Tweets from: https://github.com/rabindralamsal/MegaGeoCOV

shuffled_tweets.zip contains downloaded tweets including tweet text, the time and location the tweet was posted, and the tweet id.

tweets_with_sent.zip contains the same tweets but with BERTsent sentiment analysis applied and added to the tweet file.

tweet_downloader_4.py is the script to read in the tweet ids from the dataset and then use the twitter API to get those tweets.

bertsent.py is the script to read in the tweets we have downloaded and then apply BERTsent and save the results.