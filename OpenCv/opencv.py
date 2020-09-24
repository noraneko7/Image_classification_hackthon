#輪郭摘出

import numpy as np
import cv2
# カラー画像の読み込み
img=cv2.imread('saruman.jpg',1)
#img=cv2.imread(‘ダウンロード.jpeg’,cv2.COLOR_BGR2GRAY)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#カラー画像を読み込んでグレースケール値に変換。
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# グレースケール化
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 単純二値化
ret, img_binary = cv2.threshold(img_gray,
                                30, 224,
                                cv2.THRESH_BINARY)
# 輪郭抽出
contours, hierarchy = cv2.findContours(img_binary,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
# 輪郭を元画像に描画
img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 5)
# ここから画像描画
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(cv2.cvtColor(img_contour, cv2.COLOR_BGR2RGB))
ax1.axis('off')
plt.show()
plt.close()