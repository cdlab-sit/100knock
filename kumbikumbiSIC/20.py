# coding: utf-8
'''
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

参考
https://qiita.com/segavvy/items/dc1e63fd8f7bd5d99eea

json 参照
https://docs.python.org/ja/3/library/json.html#module-json

gzip 参照
https://docs.python.org/ja/3/library/gzip.html#module-gzip
'''

import json, gzip

# 圧縮(gzファイル)なのでgzipを使う必要がある
with gzip.open("jawiki-country.json.gz", "r") as f:
	lines = f.readlines()
	for line in lines:        
		article = json.loads(line)
		if article["title"] == "イギリス":
			#print(article["text"])
			text = article["text"]

with open("jason_bri.json", "w") as f:
	# なぜかハイライトされて出力される
	f.write(text)
	#json.dump(text, f)
