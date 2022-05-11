from flask import render_template, request
# from flask import redirect, url_for
from PIL import Image
# import pickle
from utils.classifier import *
import os
# import cv2

uploadFolder = "static/uploads/"
WIDTH = 630

def home():
    return render_template("home.html")

def index():
    return render_template("index.html")

def app():
    return render_template("app.html")

def getHeight(path):
    img = Image.open(path)
    size = img.size # width and height
    ratio = size[1] / size[0]
    height = WIDTH * ratio
    return int(height)
    

def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(uploadFolder, filename)
        print(path)
        f.save(path)
        print('File saved sucessfully in \n', path)
        height = getHeight(path)
        
        # prediction
        pipeline_model(path, filename = filename, color = 'bgr')
        return render_template("gender.html", uploaded = True, img_name = filename, height = height)
    
    return render_template("gender.html", uploaded = False, img_name = 'facemask.jpg', height = WIDTH)