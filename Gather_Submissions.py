import praw
import json
import os.path
from datetime import datetime, tzinfo
from os import listdir
import time

debug_mode = True

# Todo: The syntax gets screwed up if there are zero comments
# Setup praw
r = praw.Reddit(user_agent = 'sub_autoscraper')
r.config.store_json_result = True


while True:
    tic = datetime.utcnow()


    def get_submission_sample(id):
        with open('data/reddit/prediction_auto/' + id + '.txt', 'r') as outfile:
            submission = r.get_submission(submission_id=id)
            file_json = json.load(outfile)
            tmp = submission.json_dict
            # Can't add to Submission object, so create a dict
            # Then add the UTC time since 1970-1-1
            tmp["scrape_time"] = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()

            # iter(tmp).next['Submission'].append(tmp)
            # file_json["Submission"].append(tmp)
            file_json["Submission"].append(tmp)
        with open('data/reddit/prediction_auto/' + id + '.txt', 'w') as outfile:
            outfile.write(json.dumps(file_json, indent=4, sort_keys=True))





    files = listdir('data/reddit/prediction_auto/')
    files = [file[0:len(file)-4] for file in files]
    # if the submission is less than ?3 days old, get another sample
    for f in files:
        with open('data/reddit/prediction_auto/' + f + '.txt', 'r') as infile:
            read_file_json = json.load(infile)
            # Might need to try/except here
            if read_file_json['Submission'][len(read_file_json)-1]['scrape_time'] > (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() - (60 * 60 * 24 * 3):

            #if read_file_json['Submission'][len(read_file_json)-1]['scrape_time'] - datetime.utcnow() > datetime.date(0,0,3):
                get_submission_sample(f)
                print('accessing ' + f)



    submissions = r.get_subreddit('mma').get_new(limit=25)
    for submission in submissions:
        # Prepare file
        sub_id = submission.id.encode('ascii')
        filename = 'data/reddit/prediction_auto/' + sub_id
        filename = filename + '.txt'

        # if(~debug_mode):
        if not os.path.isfile(filename):
            print("Prepping " + filename)
            with open(filename, 'w') as sub_file:
                try:
                    sub_file.write('{\n"Submission":[]}\n')
                    sub_file.write('\n')
                    # data = json.load(outfile)
                except Exception as e:
                    print(e)

        get_submission_sample(sub_id)
        # End file

    toc = datetime.utcnow()
    time_to_delay = 600 - (toc-tic).total_seconds()
    time.sleep(time_to_delay)
