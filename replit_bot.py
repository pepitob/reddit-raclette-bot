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

FRENCH_COMMENT = "Saviez-vous que la raclette n'est pas originaire de France, contrairement à ce que pensent beaucoup de gens, mais qu'elle vient en réalité du canton du Valais en Suisse ?  Oui, je sais, c'est difficile à croire pour les amateurs de fromage français, mais c'est la vérité !\n\n\n\n Bien que l’existence du fromage en Valais soit attestée à partir du 4e siècle avant J.-C., la pratique de la raclette est attestée dès 1574 en Valais. Le nom de « raclette » fut, luis, écrit dès 1874, bien avant que les Français ne se mettent à essayer de la copier.\n\n\n\n La raclette tire son nom du fromage du même nom, le Raclette qui est enregistré comme AOP depuis 2007. Cela signifie que la production de lait, la transformation et l’affinage du produit doivent être s’effectués exclusivement dans le canton du Valais. Ce fromage gras à pâte mi-dure est fabriqué à partir de lait cru de vache et doit être affiné en cave entre 3 et 6 mois. Il est riche en protéines, magnésium, calcium, vitamine A, vitamine B et oméga-3. La meule de raclette pèse environ 5 kg et a un diamètre de 30 cm. La flore alpine dont les vaches se nourrissent se retrouve dans les saveurs du Raclette, ainsi, selon le lieu de pâturage des animaux, le goût du fromage diffère.\n\n\n\n Accompagnée de pommes de terre en robe des champs, de petits oignons et cornichons au vinaigre et d’un verre de Fendant du Valais, la raclette est un délice à partager entre amis ou en famille. Et si vous voulez vraiment vous la jouer traditionnel, évitez les appareils électriques que la majorité des gens utilise (les raclonettes). Non, non, non, la cuisson doit être faite au feu de bois, ou encore mieux, dans un four à raclette pour demi-meule. Cela permet d'avoir une croûte croustillante et délicieuse, ainsi qu'un fromage fondu de manière homogène et crémeux à souhait.\n\n\n\n Alors, maintenant que vous savez tout sur la raclette, il ne vous reste plus qu'à en profiter ! Bon appétit !"
ENGLISH_COMMENT = "Hey there! Did you know that raclette is from the canton of Valais in Switzerland? Although the existence of cheese in Valais can be traced back to the 4th century BC, the practice of raclette was first documented in Valais in 1574. The name \"raclette\" was then officially recorded in 1874, long before the French started trying to copy it.\n\n\n\n Raclette gets its name from the cheese of the same name, which has been registered as an AOP (protected designation of origin) since 2007. This means that the production of milk, the processing, and aging of the cheese must all take place exclusively in the canton of Valais. This rich, semi-hard cheese is made from raw cow's milk and must be aged in a cellar for 3 to 6 months. It's packed with proteins, magnesium, calcium, vitamin A, vitamin B, and omega-3. A typical raclette wheel weighs around 5 kg and has a diameter of 30 cm. The alpine flora that the cows feed on influences the taste of the raclette, so the flavor of the cheese can vary depending on where the animals graze.\n\n\n\n Served with potatoes, pickled onions, cornichons, and a glass of Fendant wine, raclette is a delicious dish to share with friends or family. And if you want to go traditional, avoid the electric devices that most people use (raclonettes). No, no, no, the cooking should be done over an open fire or, even better, in a raclette oven for half a wheel. This allows for a crispy and delicious crust, and a cheese that melts evenly and is oh-so-creamy.\n\n\n\n So, now that you know all about raclette, time to enjoy it! Bon appétit!"

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
                        comment.reply(ENGLISH_COMMENT)
        time.sleep(30)

keep_alive()
while True:
    run_bot()
