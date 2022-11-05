import flask
import os
import random
import json
import re
# from spoonacular_api import getInfo, getId

def remove_html_tags (text):
    """ function to remove html tags """

    clean = re.compile ('<.*?>')
    return re.sub(clean, '', text)

foods = ["pasta", "sushi", "soup", "protein bar", "burger", "ramen", "pancakes", "cookies", "smoothie", "cupcakes"]
app = flask.Flask (__name__)

@app.route ("/")
def index ():
    food = random.choice (foods)
    # id = getId (food)
    # name, pic, time, servings, diets, summary, steps, source, ingredients = getInfo (id)

    name = 'Korean Extra Crispy Fried Chicken'
    pic = 'https://spoonacular.com/recipeImages/649048-312x231.jpg'
    ingredients = ['3 pounds whole chicken', '2 Tbsp rice wine' , '2 tsp minced ginger', '1 tsp fine sea salt', '1/2 tsp ground black pepper', '1 cup potato starch or corn starch', 'cooking oil for deep frying']
    time = 20
    servings = 4
    diets = ['silly diet', 'vegetarian sometimes', 'human diet']
    summary = "Easy and delicious Korean fried chicken recipe.  Would you care for super crunchy chicken that is coated with hugely addictive homemade Korean sweet chili sauce? Then read on.  This Korean fried chicken is perfect for any occasion and I’m sure everyone will fall in love with it instantly. Learn how to make it in three simple steps!"
    steps = ['prepare it', 'make it', 'sauce it', 'eat it', 'remove it']
    source = 'https://mykoreankitchen.com/korean-fried-chicken/'

    summary = remove_html_tags (summary)

    return flask.render_template (
        "index.html",
        name = name,
        pic = pic,
        time = time,
        servings = servings,
        diets = diets,
        summary = summary,
        steps = steps,
        source = source,
        ingredients = ingredients
        )

app.run (

    port = int (os.getenv("PORT", 8080)),
    host = os.getenv ("IP", "0.0.0.0"),
    debug = True

)