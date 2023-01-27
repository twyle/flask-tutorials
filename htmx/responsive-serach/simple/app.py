from flask import Flask, render_template, request, render_template_string
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

@app.route('/search/', methods=['POST'])
def search():
    templ = """
            {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.fname }}</td>
                <td>{{ user.lname }}</td>
                <td>{{ user.email }}</td>
            </tr>
            {% endfor %}
    """
    searchWord = request.form.get('search', None)
    matchusers = [user for user in users if user.search(searchWord)]
    return render_template_string(templ, users=matchusers)


if __name__ == '__main__':
    app.run(debug=True)