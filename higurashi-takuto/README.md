# higurashi-takuto
## 開発環境
- 言語: Python 3.7.2  
- OS: macOS Mojave(10.14.2)  

## ファイル生成
各番号のファイルを生成するコマンドです。適宜拡張子などを変えてご利用ください。
```
$ touch {00..99}.py
```

## MeCabのインストール
ここではMacのbrewを使ったインストール方法をまとめます。
```
$ brew install mecab mecab-ipadic swig
$ pip install mecab-python3
```
import時は`import MeCab`とします。