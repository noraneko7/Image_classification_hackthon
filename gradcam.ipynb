ヒートマップ
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torchvision import models
from tqdm import tqdm_notebook as tqdm
from PIL import Image
import cv2

#企業番号
num = '0'
#フォルダー名
folder_name = 'Afghan Hound'
#クラス名
class_name = 'vestment'
#画像名
image_name = '000037.jpg'


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

feature_extractor = models.vgg16(pretrained=True).features
classifier = models.vgg16(pretrained=True).classifier

normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225])

# 画像を256x256にリサイズ　→　中央の224を切り取り
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize
])

img = Image.open('/content/drive/My Drive/Colab Notebooks/mydata/'+num+'/'+folder_name+'/'+class_name+'/'+image_name)
img

# 画像の正規化
img_tensor = preprocess(img)

# 各モデルを予測モードにする
feature_extractor = feature_extractor.eval()
classifier = classifier.eval()

# feature_extractorにより特徴マップを得る
feature = feature_extractor(img_tensor.view(-1,3,224,224))
print('特徴マップのサイズは　{}'.format(feature.shape))

# classifierにより分類を行います
predict = classifier(feature.view(-1,512*7*7))
print('予測されたクラスは {}'.format(torch.argmax(predict,1)))

# グレースケールをヒートマップにする関数
# 得られたグレースケールの注目箇所をヒートマップに変換する際に用います
def toHeatmap(x):
    x = (x*255).reshape(-1)
    cm = plt.get_cmap('jet')
    x = np.array([cm(int(np.round(xi)))[:3] for xi in x])
    return x.reshape(224,224,3)

feature = feature_extractor(img_tensor.view(-1,3,224,224)) #特徴マップを計算
feature = feature.clone().detach().requires_grad_(True) #勾配を計算するようにコピー
y_pred = classifier(feature.view(-1,512*7*7)) #予測を行う
y_pred[0][torch.argmax(y_pred)].backward() # 予測でもっとも高い値をとったクラスの勾配を計算
# 以下は上記の式に倣って計算しています
alpha = torch.mean(feature.grad.view(512,7*7),1)
feature = feature.view(512,7,7)
L = F.relu(torch.sum(feature*alpha.view(-1,1,1),0)).cpu().detach().numpy()
# (0,1)になるように正規化
L_min = np.min(L)
L_max = np.max(L - L_min)
L = (L - L_min)/L_max
# 得られた注目度をヒートマップに変換
L = toHeatmap(cv2.resize(L,(224,224)))

# 画像の正規化を戻すのに利用します
mean = torch.tensor([0.485, 0.456, 0.406]).view(3,1,1)
std = torch.tensor([0.229, 0.224, 0.225]).view(3,1,1)

plt.figure(figsize=(10,10))
plt.imshow((img_tensor*std + mean).permute(1,2,0).cpu().detach().numpy())

img1 = (img_tensor*std + mean).permute(1,2,0).cpu().detach().numpy()
img2 = L

alpha = 0.3
blended = img1*alpha + img2*(1-alpha)
# 結果を表示する。
plt.figure(figsize=(10,10))
plt.imshow(blended)
plt.axis('off')
plt.show()