#FlickrAPI

#pip install flickrapi
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import tensorflow as tf
import os, time, sys
#APIの情報
key="xxx"
sercret="xxx"
#待ち時間の設定
wait_time=1
#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./drive/My Drive/0_test/Saruman"#フォルダ名を指定
sample = "Saruman"#ラベル名の指定
flickr = FlickrAPI(key,sercret,format='parsed-json')
result = flickr.photos.search(
    #検索画像の指定
    text = sample,
    #画像の枚数指定
    per_page = 1500,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)
photos = result['photos']
#返り値の確認
#pprint(photos)
for i, photo in enumerate(photos['photo']):
  url_q = photo['url_q']
  #ファイル名の指定(iを.jpgの前に)
  filepath = savedir + '/' + photo['id'] + '.jpg'
  if os.path.exists(filepath): continue
  urlretrieve(url_q,filepath)
  time.sleep(wait_time)