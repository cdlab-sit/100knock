'''
テンプレートの内容を利用し，国旗画像のURLを取得せよ
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

参照：
https://www.mediawiki.org/wiki/API:Imageinfo
'''

import re #正規表現を用いるのに必要
import json, gzip
import requests

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
	temp = re.findall("^\{\{基礎情報.*?$(.*?)^\}*$",article, re.MULTILINE + re.DOTALL)
	return temp #リスト 

def get_BasicInfo(temp):
	result = {}
	# 空白を除いて
	basic_info = re.findall("^\|(.*?)\s*=\s*(.*?)\n",temp[0], re.MULTILINE + re.DOTALL)
	for line in basic_info:
			result[line[0]] = line[1]
	return result

def remove_mkup(temp):
	list = []
	for line in temp:
		line = re.sub("'{2,3}","",line)
		line = re.sub("\[\[","",line)
		line = re.sub("\]\]","",line)
		list.append(line)
	return list

def get_links(temp):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	#print(temp)
	file_name = temp["国旗画像"]
	PARAMS = {
		"action":"query",
 		"format":"json",
		"prop": "imageinfo",
		"titles":"File:{}".format(file_name),
		"iiprop": "url",
	}
	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	#print(type(DATA))
	#print(DATA)
	pages = DATA["query"]["pages"]
	for k in pages.keys():
		if "imageinfo" in pages[k].keys():
			flag_url = pages[k]["imageinfo"][0]["url"]
			#print("check")
	return flag_url

if __name__ == '__main__':
	article = find_UK("イギリス")
	temp = get_BasicInfo_temp(article)
	temp = remove_mkup(temp)
	basic_info = get_BasicInfo(temp)

	link = get_links(basic_info)

	print(link)
	'''
	for key,value in basic_info.items():
		print("{} : {}".format(key,value))
	'''