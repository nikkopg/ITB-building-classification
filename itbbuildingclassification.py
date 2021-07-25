# -*- coding: utf-8 -*-
print('[INFO]: Loading. Please wait.')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2
import numpy as np
from tkinter.filedialog import askopenfilename
from tensorflow.keras.models import load_model
import ctypes

img_size = 100

def extract_features(img_):
    img_data = cv2.resize(img_, (img_size,img_size), interpolation = cv2.INTER_AREA)
    img_data = np.array(img_data)/255.
    return img_data

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def main():
    # LOAD MODEL
    model_filename = 'itbbuildingclassification.h5'
    model = None
    while model is None:
        try:
            model = load_model(model_filename)
        except Exception as error:
            Mbox(
                'WARNING!',
                f'ERROR OCCURED:\n{str(error)}', 0
                )
            print('[INFO]: Please select saved model to load.')
            model_filename = askopenfilename()

    print('[INFO]: Model loaded.\n[INFO]: Please select image to predict.')

    # LOAD IMAGE
    filename = askopenfilename(title="Select An Image", filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png")))
    img_to_predict = cv2.imread(filename)
    pic = ResizeWithAspectRatio(img_to_predict, width=600)

    # PROCESS IMAGE
    img_data = extract_features(img_to_predict)
    test_data = [img_data.reshape(-1,img_size,img_size,3)]

    # PREDICTING
    pred = model.predict(test_data)
    predicts = {
        "Aula Barat":round((pred[0][0]*100),2),
        "Aula Timur":round((pred[0][1]*100),2),
        "CC Barat":round((pred[0][2]*100),2),
        "CC Timur":round((pred[0][3]*100),2),
        "Labtek V":round((pred[0][4]*100),2),
        "Labtek VI":round((pred[0][5]*100),2)
    }

    # PRINTING TEXT ON IMAGE
    font_scale = 0.7
    (tW, tH) = cv2.getTextSize('II', cv2.FONT_HERSHEY_SIMPLEX, font_scale, 1)[0]
    tH += int(tH*0.2)
    cv2.putText(pic, 'Prediction:',
        (0,tH), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (150,25,25), 2)
    for n, (key, value) in enumerate(sorted(predicts.items(), key=lambda item: item[1], reverse=True)):
        cv2.putText(pic, f"{key}: {value}%",
            (0,(n+2)*tH), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0,100,0), 2)
    cv2.imshow('Display', pic)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()