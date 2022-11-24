import praw
import random
import time
import datetime
import argparse

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [

    "[TRUMP] is a [THREAT], but [HE] not [FOOL]. Nevertheless, [DEMS] and [CITIZENS] must take [TRUMP] seriously - he will do anything in his [POWER] to win. ",
    "It is not [SURPRISING] that [TRUMP] [ANNOUNCED] his candidacy for President in 2024. You would think that after [SCANDALS], he would drop out of politics all together. But, we must not forget he is a [HUNGRY] [THREAT]. ",
    "[TRUMP] has transformed [GOP] and radicalized American politics in [UNIMAGINABLE] ways. There is no such thing as [MODERATE] anymore. You are either [PRO][TRUMP] or [ANTI][TRUMP]. ",
    "The trend towards [POLAR] among [CITIZENS] is [DANGER]. History [REPEAT]. The [POLAR] incited by [TRUMP] and [HE] eerily similar to the events that led to Hitler's rise to power during the Third Reich in Germany. ",
    "This is not to [SAY] that [TRUMP] is Hitler. Only that [TRUMP] and [HE] are [AUTHOR]. ",
    "[DEMOCRACY] is not done for just because of [TRUMP]. We, as [CITIZENS], have the [POWER] to keep [TRUMP] and his [HUNGRY] self out of office -- we must VOTE!"
    ]

replacements = {
    'TRUMP' : ['Trump', 'Donald Trump', 'President Trump'],    
    'THREAT' : ['threat to American democracy', 'demagogue', 'fascist'],
    'HE' : ['his agenda is', 'his ideas are', 'his tactics are'],
    'FOOL' : ['stupid', 'foolish', 'as dumb as he seems'],
    'DEMS' : ['Democrats', 'Liberals', 'other politicians'],
    'CITIZENS' : ['the American public', 'citizens', 'civilians'],
    'POWER' : ['power', 'control', 'authority'],
    'HUNGRY' : ['power-hungry', 'narcissistic', 'self-absorbed'],
    'SURPRISING' : ['surprising', 'shocking', 'astounding'],
    'ANNOUNCED' : ['announced', 'declared', 'affirmed'],
    'SCANDALS' : ['scandals', 'being banned from Twitter', 'loss during the 2020 election', 'being impeached twice'],
    'GOP' : ['the GOP', 'the Republican party', 'the right-wing'],
    'UNIMAGINABLE' : ['unimaginable', 'unprecedented', 'profound'],
    'MODERATE' : ['a moderate Republican', 'a socially liberal, fiscally conservative individual', 'an independent'],
    'PRO' : ['pro-', 'gung-ho for ', 'a die-hard supporter of '],
    'ANTI' : ['anti-', 'aggressively against ', 'an active protestor of '],
    'POLAR' : ['polarization', 'identity politics', 'radicalization'],
    'DANGER' : ['dangerous', 'frightening', 'scary'],
    'REPEAT' : ['repeats', 'rhymes', 'does not always repeat, but it does rhyme'],
    'SAY' : ['say', 'argue', 'declare'],
    'AUTHOR' : ['authoritarian', 'anti-democratic', 'threatening civil liberties'],
    'DEMOCRACY' : ['Democracy', 'American Democracy', 'The US and our democracy'],

    }


def generate_comment():

    madlib = random.choice(madlibs)
    for replacement in replacements.keys(): 
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

print('generate_comment()=', generate_comment())
#FROM MADLIBS.PY -- practiced submitting messages - do i need this?
'''
url = "https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/"
submission = reddit.submission(url=url)
comments = submission.comments.list()
for i in range(10):
    print(datetime.datetime.now(), ': made a comment, i=',i)
    try: 
        submission.reply(generate_comment())
        reply_random = random.choice(comments)
        print('random author=', reply_random.author)
        reply_random.reply(generate_comment())
    except praw.exceptions.APIException:
        print('sleeping for 5 seconds')
        time.sleep(5)
    except AttributeError: 
        pass
'''

# FIXME:
# connect to reddit 

parser = argparse.ArgumentParser(description='Add username from command line')
parser.add_argument('--username', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.username)
my_bot = 'mikesbots' + args.username
# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.

# submission_list = list(reddit.subreddit("cs40_2022fall").hot(limit=None))
# submission = random.choice(submission_list)
# submission_url = submission.url
# print('submission_url=', submission_url)
submission_url = "https://www.reddit.com/r/cs40_2022fall/comments/yz0j52/kanye_buying_parler/"
submission = reddit.submission(url=submission_url)

#submission_url = "https://www.reddit.com/r/cs40_2022fall/comments/yz66i9/pence_calls_trump_tweet_on_january_6_reckless/"

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    print('before .replace_more()')
    submission.comments.replace_more(limit=None, threshold=0)
    print('after .replace_more()')
    
    for c in submission.comments.list():
        all_comments.append(c)
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for c in all_comments:
        if c.author != my_bot:
            not_my_comments.append(c)
    

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        print(datetime.datetime.now(), ': made a top level comment')
        submission.reply(generate_comment())
        #pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            author_comment =[]
            for reply in comment.replies:
                author_comment.append(str(reply.author))
            if my_bot in author_comment: 
                pass
            else:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            random_comment = random.choice(comments_without_replies)
            try:
                #random_comment.reply(generate_comment())
                # comment to must upvoted instead of above, just replying randomly
                upvotes = 0
                for c in comments_without_replies:
                    if c.score > upvotes:
                        upvotes = c.score
                        highly_upvoted = c
                highly_upvoted.reply(generate_comment())                
            except praw.exceptions.APIException:
                print('deleted comment - cannot reply')
                pass
        except IndexError:
            print('my comments')
            pass
        
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=5)))
    pass

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)



