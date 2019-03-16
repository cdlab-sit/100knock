'''
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ


'''

import re #正規表現を用いるのに必要
import json, gzip

def find_UK(country_name):
	with gzip.open("jawiki-country.json.gz", "r") as f:
		lines = f.readlines()
		for line in lines:        
			article = json.loads(line)
			if article["title"] == country_name:
				return article["text"]
	return ValueError("can't find UK")

def find_sections(article):
	sections = []
	for line in article.split('\n'):
		#[^ ] :否定文字
		# group(1) : (^=+)    = の連続
		# group(2) : ([^=]+)  = 以外の文字の連続
		section = re.search('(^=+)([^=]+)(=+$)',line)
		
		if section != None:
			title = section.group(2)
			level = len(section.group(1))-1
			print("lv{} : {}".format(level,title))

if __name__ == '__main__':
	article = find_UK("イギリス")
	find_sections(article)
