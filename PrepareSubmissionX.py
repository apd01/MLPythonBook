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
single_submission = []
for file in  files:
    with open('data/reddit/prediction_auto/' + file + '.txt', 'r') as infile:
        read_file_json = json.load(infile)

        # If a sub hasn't received 50 upvotes (yet), ignore it
        if read_file_json['Submission'][-1]['ups'] < 50:
            continue

        # if the 4th sample was taken more than 40 minutes after posting, ignore it
        if read_file_json['Submission'][3]['scrape_time'] - read_file_json['Submission'][3]['created_utc']  > 2400:
            continue

        # If we don't have more than 24 hours of data, ignore it (24 * 2600 = 86400)
        if read_file_json['Submission'][-1]['scrape_time'] - read_file_json['Submission'][-1]['created_utc']  < 86400:
            continue


        single_submission = []
        for sample in read_file_json['Submission']:
            #print(sample['title'])
            #print(sample['id'])
            t = sample['scrape_time']
            t_created = sample['created_utc']
            # print(int(t - t_created))
            new_sample = [int(t-t_created)]
            #print(new_sample)
            # don't take more than 25 hours of data (the curve tends to flatten out)
            if int(t-t_created) > 90000:
                continue

            new_sample = [file, new_sample[0], sample['ups'], sample['downs'], sample['num_comments']]
            #print(new_sample)
            single_submission.append(new_sample)
    X_data.append(single_submission)
        #y_data.append(sample)
        #print(len(X_data))

print(len(X_data))
print(y_data[0:9])

with open('./data/reddit/output/submission_data.p', 'w') as outfile:
    pickle.dump(X_data, outfile)









