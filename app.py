from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_start_form():

    parts_of_speech = silly_story.prompts

    return render_template("questions.html", noun=parts_of_speech)
