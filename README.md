# ITB buildings image classification
Simple image classification of Institut Teknologi Bandung buildings, which includes:
1. Aula Barat
2. Aula Timur
3. Student Center Barat
4. Student Center Timur
5. Labtek V
6. Labtek VI
* VGG16 pretrained model was used to classifying building image input.
* Model is trained using train.ipynb, using local datasets.

# Train
Model is trained using train.ipynb, using local datasets.
The model is then saved as *itbbuildingclassification.h5*

# Test model 
Just simply run itbbuildingclassification.py:
```
python itbbuildingclassification.py
```
- use the sample image
- put the model in the same file directory to ease.
