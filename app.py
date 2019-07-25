from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!还好吧'


# ...
@app.route('/ss')
def index():
    return render_template('index.html')
