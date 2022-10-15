import flask
import os
import random
import json
from spoonacular_api import getInfo, getId

foods = ["pasta", "sushi", "soup", "protein bar", "burger", "ramen", "pancakes", "cookies", "smoothie", "cupcakes"]
app = flask.Flask (__name__)

@app.route ("/")
def index ():
    food = random.choice (foods)
    id = getId (food)
    name, pic, time, servings, diets, summary, steps, source = getInfo (id)

    return flask.render_template (
        "index.html",
        name = name,
        pic = pic,
        time = time,
        servings = servings,
        diets = diets,
        summary = summary,
        steps = steps,
        source = source
        )

app.run (

    port = int (os.getenv("PORT", 8080)),
    host = os.getenv ("IP", "0.0.0.0"),
    debug = True

)