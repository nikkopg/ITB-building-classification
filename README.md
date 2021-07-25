# ITBbuildingimageclassification

Simple image classification of Institut Teknologi Bandung buildings, which includes:
1. Aula Barat
2. Aula Timur
3. Student Center Barat
4. Student Center Timur
5. Labtek V
6. Labtek VI

* VGG16 pretrained model was used to classifying building image input.
* Model is trained using train.ipynb, using local datasets.
* The model is then saved as itbbuildingclassification.h5
* To test a new image, just simply run itbbuildingclassification.py using command prompt by typing: python itbbuildingclassification.py
* MAKE SURE TO PUT THE MODEL FILE IN THE SAME DIRECTORY AS THE PY FILE
