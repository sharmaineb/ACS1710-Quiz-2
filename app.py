from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_URL = "https://swapi.py4e.com/api/"

# Homepage
@app.route("/")
def homepage():
    return render_template("home.html") 

# Shows the user a form to get character's results 
@app.route("/results")
def form():
    return render_template("results.html")

# Shows the results ot the character the user searched for
# from SWAPI 
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        character = request.form.get('character_index')
        character_result = requests.get(f"{API_URL}people/{character}")
        
        name = json.loads(character_result.content).get('name')
        height = json.loads(character_result.content).get('height')
        mass = json.loads(character_result.content).get('mass')
        hair_color = json.loads(character_result.content).get('hair_color')
        eye_color = json.loads(character_result.content).get('eye_color')

        # homeworld
        # attempted homeworld stretch challenge
        # homeworld = request.form.get('planet')
        # homeworld_input = requests.get(f"{API_URL}planets/{homeworld}")
        # homeworld_search = json.loads(homeworld.content).get('homeworld_search')
        
        # films
        # my attempt at the film stretch challenge, but it still returns the url of the film :)
        films = json.loads(character_result.content).get('films')
        list_of_films = []
        for film in films:
            film = requests.get(f"{API_URL}films/{film}")
            film_title = json.loads(character_result.content).get('film_title')
            list_of_films.append(film_title)

        # key value pairs
        context = {
            'name' : name,
            'height' : height,
            'mass' : mass,
            'hair_color' : hair_color,
            'eye_color' : eye_color,
            'films' : films
        }

        return render_template("results.html", **context)

    else:
        
        return render_template("results.html")

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)








