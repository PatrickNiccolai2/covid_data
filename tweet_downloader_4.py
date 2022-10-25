import tweepy
import os
import time
import random

if(__name__=="__main__"):
	# Update these with keys from twitter developer account
	consumer_key = "aRmOhzcdCDiWdVts9Q0K45u5K"
	consumer_secret = "TFsYHY5MBfMfzlXy33vsuttCjIzdKtKQB6Nalq3X2NFrfiw8m3"
	access_token = "1573003732987613187-ODn0j3HDW0BaYNJZll0DEvhODhGAZs"
	access_token_secret = "DFeLQprKhBQWj6VWth7DnMxoBYUwZhYiC4Jd3LBoSpcyw"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	keywords = ["vaccine", "vax", "vacc", "sinopharm", "sputnik", "pfizer", "moderna", "astrazeneca",
				"vaxzevria", "spikevax", "novavax", "nuvaxovid", "biontech", "comirnaty",
				"bbil", "covaxin", "janssen", "johnson", "covishield", "BBIBP-CorV",
				"sinovac", "coronavac", "gamaleya"]

	all_lines = []
	for filename in os.listdir("MegaGeoCOV_new"):
		print(filename)
		if(filename[0] == "c"):
			file_path = "MegaGeoCOV_new/" + filename
			file = open(file_path, "r")
			lines = file.readlines()
			for line in lines:
				line_arr = line.split(",")
				tweet_id = line_arr[0]
				all_lines.append(tweet_id)
			file.close()

	#print(all_lines[0])
	random.shuffle(all_lines)
	#print(all_lines[0])

	last_tweet_num = 0
	line_index = 0
	while(line_index + 100 < len(all_lines)):
		try:
			# Get next 100 lines
			ids = []
			for j in range(100):
				ids.append(int(all_lines[line_index].strip()))
				line_index += 1

			statuses = api.lookup_statuses(ids, tweet_mode='extended')
			for status in statuses:
				#print(status)
				if(status.full_text is not None):
					tweet_text = status.full_text
					tweet_time = status.created_at
					tweet_coords = status.coordinates
					tweet_place = status.place
					tweet_id = status.id

					print(tweet_text)

					contains_keyword = False

					for keyword in keywords:
						if(keyword.lower() in tweet_text.lower()):
							contains_keyword = True

					if(contains_keyword):
						outfile = open("new_tweets/new_tweet_" + str(last_tweet_num) + ".txt", "w")

						outfile.write(str(tweet_text))
						outfile.write("\n\n")
						outfile.write(str(tweet_time))
						outfile.write("\n\n")
						outfile.write(str(tweet_coords))
						outfile.write("\n\n")
						outfile.write(str(tweet_place))
						outfile.write("\n\n")
						outfile.write(str(tweet_id))

						outfile.close()
						last_tweet_num += 1
		except:
			continue
			
		time.sleep(3)
