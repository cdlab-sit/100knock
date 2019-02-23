# higurashi-takuto
## 開発環境
- 言語: Python 3.7.2  
- OS: macOS Mojave  

## ファイル生成
各番号のファイルを生成するコマンドです。適宜拡張子などを変えてご利用ください。
```
$ touch {00..99}.py
```

## 実行速度の計測
`time-report.py`を使います。`time-report.py`は内部で`path.py`を使用します。`path.py`の中身は`current`という変数に作業パスを入れているだけのファイルです。

## MeCabのインストール
ここではMacのbrewを使ったインストール方法をまとめます。
```
$ brew install mecab mecab-ipadic swig
$ pip install mecab-python3
```
import時は`import MeCab`とします。

## CaboChaのインストール
ここではMacのbrewを使ったインストール方法をまとめます。  
上記のMeCabが入っていないといけません。  
cabochaのリポジトリを手元に落とすので、`clone`してくるパスに注意してください。
```
$ brew install crf++ cabocha
$ git clone https://github.com/taku910/cabocha
$ cd cabocha
$ pip install python/
```
ちなみに[使いやすいラッパー](https://github.com/kenkov/cabocha)があるらしいですが、試してません。  
import時は`import CaboCha`とします。
