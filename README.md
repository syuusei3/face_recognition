##face_recognition

日本語でのface_recognitionを使用した、
動画を流すまでの実装例がなかったので
せっかく実装したので誰かの助けになればと思います。

顔認識の精度としては、99.38%とかなりいい数字が出ています。

動画を流す以外のところはこちらの記事を参考にしました。

[Face Recognition](https://github.com/ageitgey/face_recognition/blob/master/README.md)

コード内にコメントアウトで説明はしていますが、
こちらの記事も参考にしてみて下さい。

## Description

単純なPythonの顔認識ライブラリface_recognitonを使用して、
mp4の動画データから指定した顔を判別するプログラムを実装しました。

入力する動画データを、リアルタイムのカメラなどにすれば簡単に
自動受付などのシステムを組むことができます。


## Demo
長澤まさみさんの顔写真を学習させて、
動画を流してみたら、しっかりこんな感じでラベル付けしてくれました。

<img src="https://i.imgur.com/JsMLyPQ.png" alt="masami" title="masami">



## Requirement
・Python3.3 + python 2.7<br>
 ・macOS or Linux

## Install
必要なものはこれぐらいです。
```
$pip3 install face_recogniton
```
##　referannce



[Face Recognition](https://github.com/ageitgey/face_recognition)
