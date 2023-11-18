from flask import Flask, render_template, make_response

app = Flask(__name__)

""""
with open('users.js') as file:
    data=file.read()
"""

@app.route('/')
def home0():
    return 'this is the home page!'

@app.route('/users.json')
def home():
    res=make_response(render_template('/users.json'))
    res.headers['Access-Control-Allow-Origin']='*'
    return res

@app.route('/test')
def test():
    return 'this is a test'

if __name__ == '__main__':
    app.run

