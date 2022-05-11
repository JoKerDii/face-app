# Gender Identification APP

This is a Flask application integrated with a Machine Learning model for gender identification. This APP can only identify female and male due to the limitation of data. Thank you for your understanding.

## Install Dependencies

```python
pip3 install -r requirements.txt
```

## Run Flask Locally

```python
python main.py
```

## Heroku Deployment Log

Python 3.8.8

```
$ python --version
```

Create `runtime.txt` and `requirements.txt`.

```
$ echo "python-3.8.8" > runtime.txt
$ pip freeze > requirements.txt
```

Create `Procfile`.

 `main` corresponds to `main.py`. `app` corresponds to `app = Flask(__name__)`.

```
$ echo "web: gunicorn main:app\nheroku ps:scale web=1" > Procfile
```

Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

```
$ heroku login
```

Use Git to clone gender-identification-app's source code to local machine.

```
$ heroku git:clone -a gender-identification-app 
$ cd gender-identification-app
```

Make some changes to the code and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```