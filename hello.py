from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Seu navegador é {}</h1>'.format(user_agent)

