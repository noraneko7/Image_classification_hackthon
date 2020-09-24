画像ファイルの分類
import os
import shutil
import glob
import re
import pandas as pd
#読み込みたいcsv
csv = '/Muffin_end.csv'
#フォルダー番号（企業）
num = '0'
#フォルダー名（ジャンル）
genre = 'Muffin'
#正解クラス
true_class = genre
df = pd.read_csv(csv)
class_list = []
class_obj = []
for index, row in df.iterrows():
  point = row['index'].find('/00')+1
  if class_list.count(row['class']) == 0:
    class_list.append(row['class'])
for item in range(len(class_list)):
  tmp = []
  for index, row in df.iterrows():
    if row['class'] == class_list[item]:
      tmp.append(row['index'][point:])
  class_obj.append(tmp)
path1 = 'mydata/'+num+'/'+genre+'/正解'
os.makedirs(path1, exist_ok=True)
path2 = 'mydata/'+num+'/'+genre+'/不正解'
os.makedirs(path2, exist_ok=True)
for i in range(len(class_obj)):
  new_dir_path_recursive = 'mydata/'+num+'/'+genre+'/'+class_list[i]
  for item in class_obj[i]:
    image_path = 'drive/My Drive/Colab Notebooks/dataset/'+num+'/'+genre+'/'+item
    files = glob.glob(image_path)
    for file in files:
      if new_dir_path_recursive == 'mydata/'+num+'/'+genre+'/'+true_class:
        new_file_path = 'mydata/'+num+'/'+genre+'/正解'
        shutil.copy(file, new_file_path)
      else:
        new_file_path = 'mydata/'+num+'/'+genre+'/不正解'
        shutil.copy(file, new_file_path)