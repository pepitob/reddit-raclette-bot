import praw
import os
from dotenv import load_dotenv
import time
from langdetect import detect


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
        lang = detect(comment.body)
        if comment.author.name != os.getenv("REDDIT_USERNAME"):
            if "raclette" in comment.body.lower():
                if lang == 'fr':
                # French response
                    comment.reply("J'aime aussi la raclette! C'est un plat tellement délicieux. 😋")
                else:
                # English response
                    comment.reply("I love raclette too! It's such a delicious dish. 😋")
    time.sleep(30)

while True:
    run_bot()



"france"
"FranceDetendue"

"AskFrance"
"Cheese"
"food"
"FoodPorn"
"AskCulinary"
"CulinaryPorn"
"FoodVideos"
"EuropeEats"
