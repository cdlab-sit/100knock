# higurashi-takuto
## 開発環境
- 言語: Python 3.7.2  
- OS: macOS Mojave  

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
