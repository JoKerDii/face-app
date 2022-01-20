from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/route1')
def route1():
    return "Hello World from route1"

def route2():
    return "Hello World from route2"

app.add_url_rule('/route2','route2',route2)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=1234,debug=True)