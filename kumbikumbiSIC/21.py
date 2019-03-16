'''
記事中でカテゴリ名を宣言している行を抽出せよ

もう自力では無理でした

参照
https://qiita.com/nubilum/items/bf9f13162e007a7b7f73
'''
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

def search_category(text):
	categories = []
	for line in text.split("\n"):
		if "Category" in line:
			categories.append(line)
	return categories

if __name__ == '__main__':
	article = find_UK("イギリス")
	for category_line in search_category(article):
		print(category_line)

