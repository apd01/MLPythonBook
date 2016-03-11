import praw
from pprint import pprint
import json


r = praw.Reddit(user_agent = 'tmp_app')
# submissions = r.get_subreddit('mma').get_hot(limit=5)
submissions = r.get_subreddit('mma').get_top_from_week()
#submissions = r.get_submissions()

#for s in submissions:
#    print(s)

submission = next(submissions)

print("Submission = %s" % submission.title)
submission.replace_more_comments(limit=None, threshold=0)
print("Received comments")
all_comments = praw.helpers.flatten_tree(submission.comments)
print("Flattened comments")



with open("ch03\data\\reddit\ThreadInfo.txt", 'w') as outfile:
    outfile.write(submission.title)
    outfile.write("\n")
    outfile.write(submission.id)

for idx, comment in enumerate(all_comments):
    try:
        with open("ch03\data\\reddit\%.0f.txt" % idx, 'w') as outfile:
            outfile.write(comment.parent_id)
            outfile.write("\n")
            outfile.write("%.0f" % comment.score)
            outfile.write("\n")
            outfile.write(comment.body.encode('utf-8'))
    except:
        print(comment.body)
    # print("Author: %s" % comment.author)
    # print("Score: %s" % comment.score)
    # print(comment.body)
    # print("\n")
    # if idx > 5:
    #    break




# pprint the variables of submission and comment to disk, as
# for some reason the documentation doesn't tell you much
# with open('submission.txt', 'w') as outfile:
#     pprint(vars(submission), outfile)

# with open('comment.txt', 'w') as outfile:
#     pprint(vars(comment), outfile)