from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is a home page"

# variable rules
@app.route('/<name>')
def variable(name):
    return 'This is variable {}'.format(name)

@app.route('/blog/<int:blogid>')
def blog(blogid):
    return f"The blog-id is {blogid}"

@app.route('/weight/<float:w>')
def weight(w):
    return "Your weight is %s"%w

if __name__ == "__main__":
    app.run(debug=True)