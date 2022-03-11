#Note flask does not appear to work anymore

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

