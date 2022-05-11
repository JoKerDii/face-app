from flask import Flask
from app import views

app = Flask(__name__)

app.add_url_rule('/home', 'home', views.home)
app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/app', 'app', views.app)
app.add_url_rule('/app/gender', 'gender', views.gender, methods = ['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug = True)