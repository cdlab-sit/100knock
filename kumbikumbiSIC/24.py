'''
記事から参照されているメディアファイルをすべて抜き出せ．


'''
import re #正規表現を用いるのに必要
import json, gzip

def get_UK(country_name):
	with gzip.open("jawiki-country.json.gz", "r") as f:
		lines = f.readlines()
		for line in lines:        
			article = json.loads(line)
			if article["title"] == country_name:
				return article["text"]
	return ValueError("can't find UK")

def get_media(article):
	'''
	Python の正規表現は、複数候補の中から最も長い文字列にマッチします。これを貪欲マッチとよびます。
	しかし正規表現の後ろに ? を添えると、最も短い文字列にマッチするようになります。これを非貪欲マッチ
	参照：
	https://python.atelierkobato.com/multi/
	'''
	files = re.findall("[file|ファイル]:(.*?)\|",article)
	return "\n".join(files)

if __name__ == '__main__':
	article = get_UK("イギリス")
	mediaes = get_media(article)
	print(mediaes)
