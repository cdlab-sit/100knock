'''
27の処理に加えて，テンプレートの値から
MediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''

#精神的に可能じゃない

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

def get_BasicInfo_temp(article):
	# flags=re.DOTALL ：”.”を改行後も対象とする
	# flags=re.MULTILINE ：”^”,"$"を改行後も対象とする
	#temp = re.findall("{{基礎情報",article,flags=re.DOTALL)
	temp = re.findall("^\{\{基礎情報.*?$(.*?)^\}*$",article, re.MULTILINE + re.DOTALL)
	return temp #リスト 

def get_BasicInfo(temp):
	result = {}
	basic_info = re.findall("^\|(.*?)=(.*?)\n",temp[0], re.MULTILINE + re.DOTALL)
	for line in basic_info:
			result[line[0]] = line[1]
	return result

def remove_mkup(value):
	list = []
	for line in value:
		line = re.sub("'{2,3}","",line)
		line = re.sub("\[\[","",line)
		line = re.sub("\]\]","",line)
		list.append(line)
	return list

if __name__ == '__main__':
	article = find_UK("イギリス")
	temp = get_BasicInfo_temp(article)
	re_temp = remove_mkup(temp)
	basic_info = get_BasicInfo(re_temp)

	for key,value in basic_info.items():
		print("{} : {}".format(key,value))