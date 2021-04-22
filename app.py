from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_start_form():
    ''' loads form with variable number of part_of_speech input forms ''' 
    parts_of_speech = silly_story.prompts

    return render_template("questions.html", pos_list = parts_of_speech)

@app.route("/story")
def show_story():
    ''' generates a madlib from the users inputs and displays text onto page ''' 
        # we need {place:paris, noun:taco, verb:run...}

    user_input_result = request.args
    user_story = silly_story.generate(user_input_result)
    
    return render_template("story.html", user_generated_story = user_story)