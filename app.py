''' application main page '''

# package
from flask import Flask, render_template
from markupsafe import escape

# handle the function
app = Flask(__name__)

# define the virtual data
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

# using template to show the web
@app.route('/')
def index():
    return render_template('index.html', name=name, movies = movies)

# Execute as a main file
if __name__ == '__main__':
    app.run()