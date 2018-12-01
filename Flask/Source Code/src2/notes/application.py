'''
Sessions are how Flask can keep track of data that pertains to a particular user.
'''

from flask import Flask, render_template, request, session  # gives access to a
                        # variable called 'session', which can be used to keep
                        # values that are specific to a particular user
from flask_session import Session  # an additional extension to sessions which
                        # allows them to be stored server-side

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notes = []   # this is a global variable

# assuming there is some HTML form that can submit a note, the note can be stored
# in a place specific to the user using their session:
@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=notes)
