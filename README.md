# Project-4
This project was completed for CS40 at CMC. Instructions found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_04). 

My `bot.py` file generates comments and replies that oppose Donald Trump for various Reddit bots. My bots are under the usernames @mikesbots1, @mikesbots2, @mikesbots3, @mikesbots4, and @mikesbots5.  

# Favorite Thread
Below is a screenshot of one of my favorite threads initiated by my reddit bots. The thread begins with an initial post created by one of my bots, @mikesbots4, which I found interesting because the language mimicked that of the /r/liberal subreddit. The fact that the following bots are conversing in the comments - one of which is from another one of my bots, @mikesbots5, - is particularly fascinating because it seems as though three users (not bots) are just engaging in this thread. 

![Screenshot of thread with my bots](redditscreenshot.png)


#Output of the `bot_counter.py` for @mikesbots1: 

```
taylordaetz@Taylors-MacBook-Air-4 topic_10 % /usr/local/bin/python3 "/Users/taylordaetz/CSCI 040/topic_10/project_4/bot_counter.py" --username=1
len(comments)= 938
len(top_level_comments)= 132
len(replies)= 806
len(valid_top_level_comments)= 132
len(not_self_replies)= 805
deleted reply.
len(valid_replies)= 805
========================================
valid_comments= 937
========================================
``` 

I believe that my score should be 33/30. I completed all 6 tasks in `bot.py`, worth 2 points each, for a total of 12 points. This github repo is 3 points. I had 937 valid comments for 8 points. For additional points, I made my bot create at least 200 new submission posts to the class subreddit by scanning the /r/liberal subreddit, which is worth 2 points (see `bot_submissions.py`). I also created 5 bots that all post similar comments (500 comments each) for another 2 points. Then, I had my bot reply to the most highly upvoted comments that it had not already replied to for 2 more points. I also had my bot upvote and downvote various submissions depending on whether the post mentioned 'trump', worth 2 points - see `bot_vote.py`. My `bot_vote.py` file also used the TextBlob library to downvote or upvote depending on whether the post had positive or negative sentiments about Trump. 
