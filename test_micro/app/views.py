from app import app
from flask import render_template, request, jsonify
import datetime
import random

# Data
data_excuses = {
	"Intros": [
		"Sorry I can't come",
		"Please forgive my absence",
		"This is going to sound crazy but",
		"Get this:",
		"I can't go because",
		"I know you're going to hate me but",
		"I was minding my own business and boom!",
		"I feel terrible but",
		"I regretfully cannot attend,",
		"This is going to sound like an excuse but"
	],
	"Scapegoat": [
		"my nephew",
		"the ghost of Hitler",
		"the Pope",
		"my ex",
		"high school marching band",
		"Dan Rather",
		"a sad clown",
		"the kid from Air Bud",
		"a professional cricket team",
		"my Tinder date"
	],
	"Delay": [
		"just shit the bed",
		"died in front of me",
		"won't stop telling me knock knock jokes",
		"is having a nervous breakdown",
		"gave me syphilis",
		"poured lemonade in my gas tank",
		"stabbed me",
		"found my box of human teeth",
		"stole my bicycle",
		"posted my nudes on Instagram"
	]
}

@app.route('/', methods=["GET"])
def home():
    date_string = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    return f"<h1>First Try on API Design</h1><p>This site is a prototype API.</p><b>There has been a change {date_string}</b>"

@app.route('/template')
def template():
    return render_template('home.html')

# A route to return all of the available entries in data.
@app.route('/api/v1/excuses/all', methods=['GET'])
def api_all():
    return jsonify(data_excuses)

# A route to return one personified excuse
@app.route('/api/v1/excuses/custom', methods=['GET'])
def api_custom():
    custom_excuse={}
    # Check if a name was provided as part of the URL.
    # If name is provided, assign it to a variable.
    # If no name is provided, display an error in the browser.
    if 'name' in request.args:
        name_custom = str(request.args['name'])
    else:
        return "Error: No name provided. Please specify a name."
    
    # Create with the given name a custome excuse with random Intro, Scapegoat and Delay
    custom_excuse['excuse'] = f'Dear {name_custom}, {data_excuses["Intros"][random.randint(0, len(data_excuses["Intros"])-1)]} {data_excuses["Scapegoat"][random.randint(0, len(data_excuses["Scapegoat"])-1)]} {data_excuses["Delay"][random.randint(0, len(data_excuses["Delay"])-1)]}'

    return jsonify(custom_excuse)

# A route to return a random excuse
@app.route('/api/v1/excuses/random', methods=['GET'])
def api_random():
	random_excuse={}
	# Create a random excuse with random Intro Scapegoat and Delay
	random_excuse['excuse'] = f'{data_excuses["Intros"][random.randint(0, len(data_excuses["Intros"])-1)]} {data_excuses["Scapegoat"][random.randint(0, len(data_excuses["Scapegoat"])-1)]} {data_excuses["Delay"][random.randint(0, len(data_excuses["Delay"])-1)]}'
	return jsonify(random_excuse)
