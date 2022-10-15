from imp import source_from_cache
import requests
import os
import json
import random
from os.path import join, dirname 
from dotenv import load_dotenv

dotenv_path = join (dirname(__file__), "spoonacular.env")
load_dotenv (dotenv_path)
spoonKey = os.environ["SPOONACULAR_KEY"]

def getId (food):
    url= "https://api.spoonacular.com/recipes/complexSearch?query={}&apiKey={}".format(food, spoonKey)
    response = requests.get (url)
    result = response.json()
    #result_json = json.dumps(result,indent = 2)
    
    recipe = result["results"][0]
    id = recipe ["id"]

    return id

#id = 648506
def getInfo (id):
    url="https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}".format(id, spoonKey)
    response = requests.get (url)
    result = response.json()
    result_json = json.dumps(result,indent = 2)
    print (result_json)
    ingredients = []
    for ingredient in result["extendedIngredients"]:
        name = ingredient["name"]
        ingredients.append (name)
    
    recipeName = result["title"]
    pic = result["image"]
    time = result["readyInMinutes"]
    source = result["sourceUrl"]
    servings = result["servings"]
    summary = result["summary"]
    diets = result["diets"]
    instructions =result["analyzedInstructions"][0]["steps"]
    steps = []

    for step in instructions:
        steps.append (step["step"])

    return recipeName, pic, time, servings, diets, summary, steps, source

