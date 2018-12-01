from flask import Flask     # Import the class "Flask" from the "flask" module, written by someone else

app = Flask(__name__)       # Instantiate a new web application called "app", 
                            # with "__name__" representing the currnt file

@app.route("/")             # A decorator; when the user goes to the route "/", 
def index():                # execute the function immediately below
    return "Hello, world!"
