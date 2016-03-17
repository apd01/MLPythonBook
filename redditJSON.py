import praw
import json
import os.path

debug_mode = False

# Todo: Probably only need one with open call in this file

# Setup praw
r = praw.Reddit(user_agent = 'tmp_app')
r.config.store_json_result = True


# Get submission
'''
submissions = r.get_subreddit('mma').get_top_from_hour()
submission = next(submissions)
'''
submissions = r.get_subreddit('mma').get_top_from_week(limit=5)
# submission = r.get_submission(submission_id='49w6kw')

for submission in submissions:
    # Prepare file
    filename = submission.id.encode('ascii')
    filename = filename + '.txt'
    filename = 'ch03/data/reddit/' + filename

    # if we're not in debug mode, check if the submission has already been scraped
    # if we're in debug mode, go ahead anyway (probably need to test other things)
    if(~debug_mode):
        if os.path.isfile(filename):
            continue

    if debug_mode:
        print(filename)
    # Prepare json structure
    with open(filename, 'w') as outfile:
        outfile.write('{\n"Submission":\n')


    # Dump submission data as json
    with open(filename, 'a') as outfile:
        if debug_mode:
            print(type(submission.json_dict))
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

        newComment = {}
        for item in dictObjects:
            newComment[item] = comment_json[item]
        return newComment

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





