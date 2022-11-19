from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_URL = 'https://swapi.py4e.com/api/'

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/search_results', methods = ['GET', 'POST'])
def search_reults():
    if request.method == 'POST':
        people = request.form.get('people_list')
        people_result = requests.get(f"{API_URL} people/ {people}")
        name = json.loads(people_result.content).get('name')
        height = json.loads(people_result.content).get('height')
        mass = json.loads(people_result.content).get('mass')
        hair_color = json.loads(people_result.content).get('hair_color')
        eye_color = json.loads(people_result.content).get('eye_color')

        context = {
            'name' : name,
            'height' : height,
            'mass' : mass,
            'hair_color' : hair_color,
            'eye_color' : eye_color
        }
    return render_template('search_results')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)








