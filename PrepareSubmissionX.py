#
# This will take all the files in the /prediction folder (each containing samples of submissions)
# and turn it into a vector with this structure:
#
# sample_time   num_upvotes     num_downvotes   num_comments
#

import json
import gzip
import pickle
from os import listdir
import re
import praw

directory = './data/reddit/prediction/'
#r = praw.Reddit(user_agent = 'sub_scraper')
#r.config.store_json_result = True



#
# In the future, look at:
# Keywords in title
# Self/not self (binary)
#   Analysis of self text
# Controversy of post?
# Far future: use beautifulsoup to check rss feeds, compare news headlines to title/text in link
#



files = listdir('data/reddit/prediction_auto/')
files = [file[0:len(file)-4] for file in files]

X_data = []
y_data = []
for file in  files:
    with open('data/reddit/prediction_auto/' + file + '.txt', 'r') as infile:
        read_file_json = json.load(infile)
        for sample in read_file_json['Submission']:
            #print(sample['title'])
            #print(sample['id'])
            t = sample['scrape_time']
            t_created = sample['created_utc']
            # print(int(t - t_created))
            new_sample = [int(t-t_created)]
            #print(new_sample)

            new_sample = [file, new_sample[0], sample['ups'], sample['downs'], sample['num_comments']]
            #print(new_sample)
            X_data.append([new_sample])
        #y_data.append(sample)
        #print(len(X_data))

print(len(X_data))
print(y_data[0:9])

with open('./data/reddit/output/submission_data.p', 'w') as outfile:
    pickle.dump(X_data, outfile)









