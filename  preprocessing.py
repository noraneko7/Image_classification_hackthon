#水増し処理をしてnumpy配列に変換

from PIL import Image
from sklearn import model_selection
import numpy as np
import glob, os, cv2
folder = ["./drive/My Drive/data/"]#保存先フォルダの指定
classes = ["Teddy Bear","Sheepdog","Saruman","Puppy","Muffin","Mop","Labradoodle","Fried Chicken","cookie","chihuahua","Afghan Hound"]#ラベル名記入
num_classes = len(classes)
image_size = 224
X = []
Y = []
for index, name in enumerate(classes):
    dir = "./drive/My Drive/data/" + name
    files = glob.glob(dir + "/*.*")
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        #image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        data = np.asarray(image)
        for angle in range(-20,20,5):
          #回転
          img_r = image.rotate(angle)
          data = np.array(img_r)
          X.append(data)
          Y.append(index)
          #反転
          img_trans =  image.transpose(Image.FLIP_LEFT_RIGHT)
          data = np.array(img_trans)
          X.append(data)
          Y.append(index)
X = np.array(X)
Y = np.array(Y)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
#numpy配列のファイル作成
np.save("test05.npy", xy)