'''
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ

正規表現　参照
https://www.mnet.ne.jp/~nakama/

re 参照
https://docs.python.org/ja/3/library/re.html
'''

import re #正規表現を用いるのに必要
import json, gzip

def find_UK(country_name):
# 圧縮(gzファイル)なのでgzipを使う必要がある
	with gzip.open("jawiki-country.json.gz", "r") as f:
		lines = f.readlines()
		for line in lines:        
			article = json.loads(line)
			if article["title"] == country_name:
				return article["text"]
	return ValueError("can't find UK")

# 名前によりカテゴリを検索（行単位でなく）
def search_category_ByName(text):
	categories = []
	for line in text.split("\n"):
		'''
		正規表現の特殊文字
		()	: グループ化
		[]	: 指定した文字のどれか
		^	: 先頭指定
		|	: or
		.*	: 任意の０文字以上

		^は正規表現の先頭、$は終端のものしかメタ文字として認識されません。
		[ ]の中で ^ が使用された場合は、行の先頭を表す ^ とは意味が異なりますので注意して下さい。
		'''
		category = re.search("\[\[Category:([^\|]+)(.*)+\]\]", line) 					 

		#print(type(category))
		if category != None:
			categories.append(category.group(0))
	return categories

if __name__ == '__main__':
	article = find_UK("イギリス")
	for category_line in search_category_ByName(article):
		print(category_line)
