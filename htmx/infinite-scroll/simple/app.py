from flask import Flask, render_template, request, render_template_string

total = 10

messages = [f"Message {count}" for count in range(total)]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

# @app.route('/search/', methods=['POST'])
# def search():
#     templ = """
#             {% for user in users %}
#             <tr>
#                 <td>{{ user.id }}</td>
#                 <td>{{ user.fname }}</td>
#                 <td>{{ user.lname }}</td>
#                 <td>{{ user.email }}</td>
#             </tr>
#             {% endfor %}
#     """
#     searchWord = request.form.get('search', None)
#     matchusers = [user for user in users if user.search(searchWord)]
#     return render_template_string(templ, users=matchusers)


if __name__ == '__main__':
    app.run(debug=True)