# Image_classification_hackthon
## AI-SCHOLAR主催プロジェクト型ハッカソン

## 今回のハッカソン 概要
- 機械学習に置いて二値分類は非常に高い精度が出ることが知られているが、ラベルの分布が正しいかはあまり考慮されていない。
- 画像分類などは専門のアノテーターに依頼することが多いが、アノテーションが正しく行われているのかをチェックするには多大なコストがかかる
- そこで、アノテーターにアノテーションしてもらったデータを用いてアノテーション者の評価ができないだろうか。

## タスク
アノテーションを依頼した３団体のアノテーション精度を評価し、順位付けをする

***
## preprocessing.py
水増し処理+numpy配列に変換

***
## API.py
FlickrAPIを用いて学習用データの作成

***
## cd.py
画像ファイルの分類

***
## CreateExcel/create_xlsx.py
エクセルファイルの作成

***
## CreateExcel/data_list_v3.json
エクセル生成用データ

***
## radcam.py
ヒートマップ 

***
## OpenCv/opencv.py
輪郭摘出

***
## OpenCv/opencvFace.py
顔・目の摘出

***
## accuracy
精度

***
## predict
予測