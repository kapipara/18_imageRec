# <参考URL>
# 環境構築 : https://qiita.com/FukuharaYohei/items/5d49938ffd33d198f0c0
# キャプチャ　：https://qiita.com/wkentaro/items/3d3bee56445894da879e
# キャプチャ2(英語) :https://pysource.com/2018/01/20/loading-video-and-webcam-opencv-3-4-with-python-3-tutorial-2/
# 時間関係 : https://note.nkmk.me/python-datetime-usage/
# 時間とファイル保存 : https://hawksnowlog.blogspot.com/2017/03/opencv3-take-a-photo.html

# Open CV のインポート
# よくわからんけど，numpyもいれとく
# とりあえず，ファイル名のためにdatatimeを入れる
import cv2
import numpy as np
import datetime 
import time

cap = cv2.VideoCapture(1) # 0はカメラのデバイス番号 (接続順で番号を振る　　例，内蔵カメラが０番　外付けwebカメラが１番)
cap2 = cv2.VideoCapture(2) 
i=0
# retは画像を取得成功フラグ
# VideoCaptureから1フレーム読み込む
while True:
    ret, frame = cap.read()
    ret, frame2 =cap2.read()

    # フレームを表示する
    cv2.imshow("frame", frame)
    cv2.imshow("frame2",frame2)
    time.sleep(1)#1秒おきに動かす
    i=i+1
    print("%d",i)
    if i == 3: #定義したiの値-1回写真を撮る
        break

    #下のブロックがファイルネーム関係
    now = datetime.datetime.now() # 年月日時を取得
    filename = now.strftime("%Y%m%d_%H%M%S%f") # 最後のfがマイクロ秒6桁
    print(filename)
    cv2.imwrite('./img/%s cam1.png'%filename, frame) # ファイルの拡張子はここと下の行変更すればイけるかも 
    cv2.imwrite("./img/%s cam2.png"%filename, frame2)
    # img = cv2.imread(filename + '.png') ←これいらなくね？
    
    

    
# キャプチャを解放する 
cap.release()
cv2.destroyAllWindows()
