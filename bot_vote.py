import random
import praw
import argparse
from textblob import TextBlob


parser = argparse.ArgumentParser(description='Add username from command line')
parser.add_argument('--username', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.username)
my_bot = 'mikesbots' + args.username

number_submissions = 0 
number_comments = 0

for submission in list(reddit.subreddit("cs40_2022fall").hot(limit=100)):

    if 'trump' in submission.title.lower():
        submission_textblob = TextBlob(submission.title)
        submission_polarity = submission_textblob.sentiment.polarity

        if submission_polarity >= 0.0:
            submission.downvote()
            print('downvoted '+submission.title)
            number_submissions +=1
            print('number_submissions=',number_submissions)
        

        else:
            submission.upvote()
            print('upvoted '+submission.title)
            number_submissions +=1
            print('number_submissions=',number_submissions)

    print('before .replace_more()')
    submission.comments.replace_more(limit=None, threshold=0)
    print('after .replace_more()')

    for c in submission.comments.list():
        if 'trump' in c.body.lower():
            c_textblob = TextBlob(c.body)
            c_polarity = c_textblob.sentiment.polarity

            if c_polarity >= 0.0:
                c.downvote()
                print('downvoted '+c.body)
                number_comments +=1
                print('number_comments=',number_comments)

            else:
                c.upvote()
                print('upvoted '+c.body)
                number_comments +=1
                print('number_comments=',number_comments)
