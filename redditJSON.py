import praw
import json

debug_mode = False

# Todo: Probably only need one with open call in this file

# Setup praw
r = praw.Reddit(user_agent = 'tmp_app')
r.config.store_json_result = True


# Get submission
submissions = r.get_subreddit('bjj').get_top_from_hour()
submission = next(submissions)

# Prepare file
filename = submission.id.encode('ascii')
if debug_mode:
    print(filename + '.txt')
# Prepare json structure
with open(filename + '.txt', 'w') as outfile:
    outfile.write('{\n"Submission":\n')


# Dump submission data as json
with open(filename + '.txt', 'a') as outfile:
    if debug_mode:
        print(type(submission.json_dict))
    #json.dumps(submission.json_dict, outfile)
    outfile.write(json.dumps(submission.json_dict, indent=4,sort_keys=True))

if debug_mode:
    print("Wrote data to " + filename + '.txt')

# Get all comments for the submission
if debug_mode:
    print("Submission = %s" % submission.title)
submission.replace_more_comments(limit=None, threshold=0)
if debug_mode:
    print("Received comments")

all_comments = praw.helpers.flatten_tree(submission.comments)
if debug_mode:
    print("Flattened comments")

# print(type(enumerate(all_comments)))
with open(filename + '.txt', 'a') as outfile:
    output = ""
    output += ',\n\n"CommentList":['


    for c in all_comments:
        output += "\n" # outfile.write('\n')
        #outfile.write(json.dumps(c, indent=4, sort_keys=True))
        output += json.dumps(c.json_dict, indent=4, sort_keys=True, ensure_ascii=True) #outfile.write(json.dumps(c.json_dict, indent=4, sort_keys=True, ensure_ascii=True))

        output += ',\n'# outfile.write(',\n')

    output = output[0:len(output)-2]# outfile.write(']')
    output += '\n]'
    outfile.write(output)


# End file
with open(filename + '.txt', 'a') as outfile:
    outfile.write('\n}')

