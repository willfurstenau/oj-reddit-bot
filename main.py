#!/usr/bin/python

import praw
import os
from datetime import datetime, timedelta

keywords = ['PB278Q', 'QX2710', 'MG279Q']
reddit = praw.Reddit('bot1')

#reddit.login(REDDIT_USERNAME,REDDIT_PASS)

if not os.path.isfile("read_posts.txt"):
    read_posts = []

else:
    with open("read_posts.txt", "r") as f:
        read_posts = f.read()
        read_posts = read_posts.split("\n")
        read_posts = list(filter(None, read_posts))

hardwareswap = reddit.subreddit('hardwareswap')
oj_sub = reddit.subreddit('ojtestsub')

for submission in hardwareswap.new(limit=5):
    if submission.id not in read_posts:
        if(submission.link_flair_text == "Selling"):
            for key in keywords:
                if key.lower() in submission.title.lower() or key.lower() in submission.selftext.lower():
                    h = submission.title.find("[H]") + 4
                    w = submission.title.find("[W]")
                    title = "[" + key + "]" + "   " + submission.title[h:w]
                    oj_sub.submit(title=title, url=submission.url)
                    read_posts.append(submission.id)

for submission in oj_sub.new(limit = 100):
	if (datetime.fromtimestamp(submission.created) < (datetime.today() - timedelta(2))):
#		print (submission.title)
		submission.delete()

with open("read_posts.txt", "w") as f:
    for post_id in read_posts:
        f.write(post_id + "\n")
