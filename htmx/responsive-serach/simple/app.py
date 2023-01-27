from flask import Flask, render_template
from models import User

users = [
    User("abe", "vida", "abe@nowhere.com"),
    User("betty", "b", "bb@nowhere.com"),
    User("joe", "robinson", "jrobinson@nowhere.com"),

    User("Luis", "Cortes", "Luis@somewhere.com"),
    User("marty", "hinkle", "mhinkle@nowhere.com"),
    User("matthew", "robinson", "mrobinson@nowhere.com"),

    User("collin", "western", "cwest@nowhere.com"),
    User("marty", "hinkle II", "mhinkle2@nowhere.com"),
    User("joe", "robinson", "jrobinson@nowhere.com"),

    User("juan", "vida", "juanvida@nowhere.com"),
    User("marty", "hinkle III", "mhinkle3@nowhere.com"),
    User("zoe", "omega", "zoe@nowhere.com") 
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)