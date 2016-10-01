#HanSolo_Bot

import praw
import pdb
import re
import os
from config_skel import *

#Define user agent
user_agent = ("HanSolo_Bot v0.1")

#Create a reddit instance and login
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

#if reply log doesnt exist make empty list
if not os.path.isfile("replied.txt"):
    replied = []

#else open and read
else:
    with open("replied.txt", "r") as f:
        replied = f.read()
        replied = replied.split("\n")
        replied = filter(none, replied);
        
#open subreddit
subreddit = r.get_subreddit("all")


for submission in subreddit.get_hot(limit = 100):
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    already_done = set()
    for comment in flat_comments:
        if not hasattr(comment, "body"):
            continue
        if comment.body == "I love you." and comment.id not in already_done:
            comment.reply("I know.")
            print "Replying to : ", submission.title
            already_done.add(comment.id)
