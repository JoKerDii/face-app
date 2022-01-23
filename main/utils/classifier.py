
from unicodedata import name
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pickle
import cv2
import os

# assert os.path.exists('model/')
# assert os.path.exists('static/')

# load the models
haar = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
model_pca  = pickle.load(open('model/pca_50.pkl', 'rb'))
mean  = pickle.load(open('model/mean_preprocess.pkl','rb'))
model_svm  = pickle.load(open('model/model_svm_best.pkl','rb'))
print('Four pickles are loaded')

# settings
gender_pre = ['Male','Female']
font = cv2.FONT_HERSHEY_SIMPLEX

# pipeline function
def pipeline_model(path,filename, color='bgr'):
    # read in image
    # img = np.array(Image.open(path)) # blue color
    # read in image
    img = cv2.imread(path) # original color
    
    if color == 'bgr': # convert to gray scale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    faces = haar.detectMultiScale(gray,1.5,3) # detect face
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi = gray[y:y+h,x:x+w] # crop image
        roi = roi / 255.0 # normalization
        if roi.shape[1] > 100: # resize
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_AREA)  # shrink
        else:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_CUBIC) # enlarge
        roi_reshape = roi_resize.reshape(1,10000) # flatten
        
        roi_mean = roi_reshape - mean
        eigen_image = model_pca.transform(roi_mean) # get eigen image

        results = model_svm.predict_proba(eigen_image)[0] # prediction
        predict = results.argmax() # 0 or 1 
        score = results[predict] # accuracy

        text = "%s : %0.2f"%(gender_pre[predict],score)
        cv2.putText(img,text,(x,y),font,1,(255,255,0),2)
        
    cv2.imwrite(f'static/predicts/{filename}', img)
    
if __name__ == "__main__":
    # test
    assert os.path.exists('images/')
    test_data_path = 'images/root_female.jpg'
    color = 'bgr'
    img = Image.open(test_data_path) # rgb
    img = np.array(img)
    pipeline_model(img, filename = "predicted_root.jpg", color = 'bgr')