from flask import render_template, url_for, flash, redirect
from isitbusy import app
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'html.parser')


@app.route("/")
@app.route("/home")
def home():
    world = soup.find('tr', {"class": "total_row_world"})
    entries = world.find_all('td')
    return render_template('home.html', entries=entries)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
