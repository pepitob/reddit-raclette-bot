import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="console:raclette-bot:1.0 (by u/Raclette_bot)",
)

# subreddit = reddit.subreddit("raclettetest")

# for submission in subreddit.hot(limit=10):
#     print("****************")
#     print(submission.title)

#     for comment in submission.comments:
#         if hasattr(comment, "body"):
#             print("-------------------")
#             print(comment.body)


def run_bot():
    subreddit = reddit.subreddit("raclettetest")
    for comment in subreddit.stream.comments(skip_existing=True):
        if "raclette" in comment.body.lower() or "Raclette" in comment.body:
            comment.reply("I love raclette too! It's such a delicious dish. 😋")
            time.sleep(30)

while True:
    run_bot()
    time.sleep(30)
