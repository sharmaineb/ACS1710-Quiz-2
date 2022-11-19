from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.hmtl')