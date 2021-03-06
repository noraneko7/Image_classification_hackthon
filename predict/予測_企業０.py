# -*- coding: utf-8 -*-
"""予測_企業０.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11h5HFTrrySKGWRSZb3p1ahO4qjE1A8dp
"""

from tensorflow.python.keras.applications.vgg16 import preprocess_input,decode_predictions
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array
import numpy as np
import pandas as pd
import os, glob
from tensorflow.keras.models import load_model

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Puppy = ["./drive/My Drive/dataset/0/Puppy"]

#写真の取り出し
Y = []
images = []
for name in folder_Puppy:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Puppy01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Muffin = ["./drive/My Drive/dataset/0/Muffin"]

#写真の取り出し
Y = []
images = []
for name in folder_Muffin:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Muffin01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Labradoodle = ["./drive/My Drive/dataset/0/Labradoodle"]

#写真の取り出し
Y = []
images = []
for name in folder_Labradoodle:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Labradoodle01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Afghan_Hound = ["./drive/My Drive/dataset/0/Afghan Hound"]

#写真の取り出し
Y = []
images = []
for name in folder_Afghan_Hound:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Afghan Hound01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_chihuahua = ["./drive/My Drive/dataset/0/chihuahua"]

#写真の取り出し
Y = []
images = []
for name in folder_chihuahua:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("chihuahua01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_cookie = ["./drive/My Drive/dataset/0/cookie"]

#写真の取り出し
Y = []
images = []
for name in folder_cookie:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("cookie01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Fried_Chicken = ["./drive/My Drive/dataset/0/Fried Chicken"]

#写真の取り出し
Y = []
images = []
for name in folder_Fried_Chicken:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Fried Chicken01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Mop = ["./drive/My Drive/dataset/0/Mop"]

#写真の取り出し
Y = []
images = []
for name in folder_Mop:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Mop01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Saruman = ["./drive/My Drive/dataset/0/Saruman"]

#写真の取り出し
Y = []
images = []
for name in folder_Saruman:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Saruman01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Sheepdog = ["./drive/My Drive/dataset/0/Sheepdog"]

#写真の取り出し
Y = []
images = []
for name in folder_Sheepdog:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Sheepdog01.csv",index = False)

model = load_model('./drive/My Drive/AI画像分類ハッカソン /sample01.h5')

images=[]
Y=[]
folder_Teddy_Bear = ["./drive/My Drive/dataset/0/Teddy Bear"]

#写真の取り出し
Y = []
images = []
for name in folder_Teddy_Bear:
    path = glob.glob(name + '/*.*') 
    for img in path:
        Y.append(img)
        images.append(preprocess_input(img_to_array(load_img(img, target_size=(224, 224)))))
len(images)


preds = model.predict(np.stack(images))
classes = ['Afghan Hound','chihuahua','cookie','Fried Chicken','Labradoodle','Mop','Muffin','Puppy','Saruman','Sheepdog','Teddy Bear']
pred_labels = np.argmax(preds, axis=-1)

pred_label_names = [classes[x] for x in pred_labels]
print(pred_label_names)  

resuls=[]
#for i in range(292):
 #   resuls.append(pred_label_names[i])

resuls = pd.DataFrame(pred_label_names,columns=["class"])
Y = pd.DataFrame(Y,columns=["index"])

index= pd.concat([Y,resuls],axis=1)
index.to_csv("Teddy Bear01.csv",index = False)