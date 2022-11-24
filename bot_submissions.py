import random
import praw
import argparse

parser = argparse.ArgumentParser(description='Add username from command line')
parser.add_argument('--username', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.username)
my_bot = 'mikesbots' + args.username
for i in range(200):
    
    submission_list = list(reddit.subreddit("liberal").hot(limit=None))
    submission = random.choice(submission_list)
    submission_title = submission.title
    selftext=submission.selftext

    if selftext =='':
        url = submission.url
        subreddit = reddit.subreddit("cs40_2022fall")
        subreddit.submit(submission_title,url=url)
    else:
        subreddit = reddit.subreddit("cs40_2022fall")
        subreddit.submit(submission_title, selftext=selftext)
    print('Submission created')