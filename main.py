#!/usr/bin/python

import praw
import os
from datetime import datetime

keywords = ['SSD', 'PB278Q', 'QX2710']
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

for submission in hardwareswap.new(limit=50):

    if submission.id not in read_posts:
        if(submission.link_flair_text == "Selling"):
            for key in keywords
                if key in submission.title:
                    oj_sub.submit(title=submission.title, url=submission.url)
                    read_posts.append(submission.id)


with open("read_posts.txt", "w") as f:
    for post_id in read_posts:
        f.write(post_id + "\n")
