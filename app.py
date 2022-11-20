from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_URL = "https://swapi.py4e.com/api/"

@app.route("/")
def homepage():
    return render_template("home.html") 

@app.route("/results")
def form():
    return render_template("results.html")

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

        context = {
            'name' : name,
            'height' : height,
            'mass' : mass,
            'hair_color' : hair_color,
            'eye_color' : eye_color
        }

        return render_template("results.html", **context)

    else:
        return render_template("results.html")

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)








