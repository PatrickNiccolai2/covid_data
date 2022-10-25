import torch
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer 
import tensorflow as tf
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import locale

import os
import time

def main():
	# Create the pre trained model and tokenizer
	model = TFAutoModelForSequenceClassification.from_pretrained("rabindralamsal/finetuned-bertweet-sentiment-analysis")

	tokenizer = AutoTokenizer.from_pretrained("rabindralamsal/finetuned-bertweet-sentiment-analysis")

	# Loop through all files
	for filename in os.listdir("covid_data/shuffled_tweets/"):
		if(filename[0] == "s"):
			file_path = "covid_data/shuffled_tweets/" + filename

			# Open file
			in_file = open(file_path, "r")

			# Read file into a string
			lines = in_file.read()

			# Close file
			in_file.close()

			# Split the string and get components
			lines_arr = lines.split("\n\n")

			# Get the tweet text
			tweet_text = ""
			for i in range(5, len(lines_arr) + 1):
				tweet_text = tweet_text + lines_arr[-i]

			# Get BERTsent prediction
			encoded_tweet = tokenizer.encode(tweet_text, return_tensors="tf")
			output = model.predict(encoded_tweet)[0]
			prediction = tf.nn.softmax(output, axis=1).numpy()

			# Create file to write tweet + sentiment
			out_file_name = "sent_" + filename
			out_file = open("tweets_with_sent/" + out_file_name, "w")

			# Write original tweet
			out_file.write(lines)

			# Write sentiment
			out_file.write("\n\n")
			out_file.write(str(prediction))

			out_file.close()


if(__name__ == "__main__"):
	main()