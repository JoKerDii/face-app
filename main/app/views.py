from flask import render_template, request
from flask import redirect, url_for
from PIL import Image
import pickle
from utils.classifier import *
import os
import cv2

uploadFolder = "main/static/uploads"

def home():
    return render_template("home.html")

def index():
    return render_template("index.html")

def app():
    return render_template("app.html")

def getWidth(path):
    img = Image.open(path)
    size = img.size # width and height
    ratio = size[0] / size[1]
    width = 600 * ratio
    return int(width)
    

def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(uploadFolder, filename)
        f.save(path)
        width = getWidth(path)
        
        # prediction
        pipeline_model(path, filename = filename, color = 'bgr')
        return render_template("gender.html", uploaded = True, img_name = filename, width = width)
    
    return render_template("gender.html", uploaded = False, img_name = 'facemask.jpg', width = 600)