'''
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）
を除去してテキストに変換せよ（参考: マークアップ早見表）
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
		list.append(re.sub("'{2,3}","",line))
	#print(list)
	return list

if __name__ == '__main__':
	article = find_UK("イギリス")
	temp = get_BasicInfo_temp(article)
	re_temp = remove_mkup(temp)
	basic_info = get_BasicInfo(re_temp)
	#basic_info2 = get_BasicInfo(temp)

	#print("\n修正前")
	##	print("{} : {}".format(key,value)) 

	#print("\n修正後")
	for key,value in basic_info.items():
		print("{} : {}".format(key,value))