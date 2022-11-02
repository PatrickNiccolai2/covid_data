import os
from langdetect import detect

def main():
	# Loop through all files
	for filenum in range(128831):
			file_path = "tweets_with_sent/sent_shuffled_tweet_" + str(filenum) + ".txt"

			try:
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
				for i in range(6, len(lines_arr) + 1):
					tweet_text = tweet_text + lines_arr[-i]

				try:
					# Get language
				    language = detect(tweet_text)
				except:
					language = "None"

				# Create file to write tweet + language
				out_file_name = "tweets_with_lang/lang_sent_shuffled_tweet_" + str(filenum) + ".txt"
				out_file = open(out_file_name, "w")

				# Write original tweet
				out_file.write(lines)

				# Write sentiment
				out_file.write("\n\n")
				out_file.write(str(language))

				out_file.close()
			except:
				pass

if(__name__ == "__main__"):
	main()