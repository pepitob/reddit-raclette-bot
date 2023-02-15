import praw
import os
import time
from langdetect import detect
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="console:raclette-bot:1.0 (by u/Raclette_bot)",
)

FRENCH_COMMENT = "Hey ! Saviez-vous que la raclette n'est pas originaire de France, contrairement à ce que pensent beaucoup de gens, mais qu'elle vient en réalité du canton du Valais en Suisse ?  Oui, je sais, c'est difficile à croire pour les amateurs de fromage français, mais c'est la vérité !\n Bien que l’existence du fromage en Valais soit attestée à partir du 4e siècle avant J.-C., la pratique de la raclette est attestée dès 1574 en Valais. Le nom de « raclette » fut, luis, écrit dès 1874, bien avant que les Français ne se mettent à essayer de la copier.\n La raclette tire son nom du fromage du même nom, le Raclette qui est enregistré comme AOP depuis 2007. Cela signifie que la production de lait, la transformation et l’affinage du produit doivent être s’effectués exclusivement dans le canton du Valais. Ce fromage gras à pâte mi-dure est fabriqué à partir de lait cru de vache et doit être affiné en cave entre 3 et 6 mois. Il est riche en protéines, magnésium, calcium, vitamine A, vitamine B et oméga-3. La meule de raclette pèse environ 5 kg et a un diamètre de 30 cm. La flore alpine dont les vaches se nourrissent se retrouve dans les saveurs du Raclette, ainsi, selon le lieu de pâturage des animaux, le goût du fromage diffère.\n Accompagnée de pommes de terre en robe des champs, de petits oignons, cornichons au vinaigre et d’un verre de Fendant du Valais, la raclette est un délice à partager entre amis ou en famille. Et si vous voulez vraiment vous la jouer traditionnel, évitez les appareils électriques que la majorité des gens utilise (les raclonettes). Non, non, non, la cuisson doit être faite au feu de bois, ou encore mieux, dans un four à raclette pour demi-meule. Cela permet d'avoir une croûte croustillante et délicieuse, un fromage fondu de manière homogène et crémeux à souhait.\n Alors, maintenant que vous savez tout sur la raclette, il ne vous reste plus qu'à en profiter ! Bon appétit !"

def run_bot():
    subreddits = ["AskFrance", "Cheese", "food", "FoodPorn", "AskCulinary", "CulinaryPorn", "FoodVideos", "EuropeEats", "france", "FranceDetendue"]
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        for comment in subreddit.stream.comments(skip_existing=True):
            lang = detect(comment.body)
            if comment.author.name != os.getenv("REDDIT_USERNAME"):
                if "raclette" in comment.body.lower():
                    if sub == "france" or sub == "FranceDetendue" or lang == 'fr':
                    # French response
                        comment.reply(FRENCH_COMMENT)
                    else:
                    # English response
                        comment.reply("I love raclette too! It's such a delicious dish. 😋")
        time.sleep(30)

keep_alive()
while True:
    run_bot()
