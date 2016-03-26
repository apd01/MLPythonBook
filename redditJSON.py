import praw
import json
import os.path

debug_mode = True

# Todo: Probably only need one with open call in this file
# Todo: The syntax gets screwed up if there are zero comments

# Setup praw
r = praw.Reddit(user_agent = 'tmp_app')
r.config.store_json_result = True


# Get submission
'''
submissions = r.get_subreddit('mma').get_top_from_hour()
submission = next(submissions)
'''

submissions = r.get_subreddit('mma').get_top_from_day(limit=25)
# submission = r.get_submission(submission_id='49w6kw')

for submission in submissions:
    # Prepare file
    filename = submission.id.encode('ascii')
    filename = filename + '.txt'
    filename = 'ch03/data/reddit/' + filename

    # if we're not in debug mode, check if the submission has already been scraped
    # if we're in debug mode, go ahead anyway (probably need to test other things)
    # Should eventually do this on a per-comment basis
    # if(~debug_mode):
    if os.path.isfile(filename):
        print("Already have " + filename)
        with open(filename, 'r') as sub_file:
            data = json.load(sub_file)
            # only get comments if the number of comments has increased by more than 20%
            # In this case, just replace the file, as number of votes, edits etc. will be different
            if submission.num_comments > data["Submission"]["num_comments"] * 1.2:
                print(submission.num_comments)
                print(data["Submission"]["num_comments"])
            else:
                continue

    if debug_mode:
        print(filename)

    # Prepare json structure
    with open(filename, 'w') as outfile:
        outfile.write('{\n"Submission":\n')

        # Dump submission data as json. This is currently unzipped and formatted for readability
        outfile.write(json.dumps(submission.json_dict, indent=4,sort_keys=True))

        if debug_mode:
            print("Wrote data to " + filename)

        # Get all comments for the submission
        if debug_mode:
            print("Submission = %s" % submission.title)
        submission.replace_more_comments(limit=None, threshold=0)
        if debug_mode:
            print("Received comments")

        all_comments = praw.helpers.flatten_tree(submission.comments)
        if debug_mode:
            print("Flattened comments")

    def remakeCommentDict(comment_json):
        dictObjects = ["approved_by", "archived", "author", "author_flair_css_class", "author_flair_text", "banned_by",
        "body", "body_html", "controversiality", "created", "created_utc", "distinguished", "downs",
        "edited", "gilded", "id", "likes", "link_id", "mod_reports", "name", "num_reports","parent_id",
        "removal_reason", "report_reasons", "saved", "score", "score_hidden", "stickied",
        "subreddit", "subreddit_id", "ups", "user_reports"]

        new_comment = {}
        for item in dictObjects:
            new_comment[item] = comment_json[item]
        return new_comment

    # print(type(enumerate(all_comments)))
    with open(filename, 'a') as outfile:
        output = ""
        output += ',\n\n"CommentList":['

        for c in all_comments:
            output += '\n'
            str1 = json.dumps(remakeCommentDict(c.json_dict), indent=4, sort_keys=True, ensure_ascii=True, skipkeys=True) #outfile.write(json.dumps(c.json_dict, indent=4, sort_keys=True, ensure_ascii=True))
            output += str1
            output += ',\n'

        # Get rid of the last , (and \n), to comply with proper json formatting
        output = output[0:len(output)-2]#
        output += '\n]'
        outfile.write(output)

    # End file
    with open(filename, 'a') as outfile:
        outfile.write('\n}')





