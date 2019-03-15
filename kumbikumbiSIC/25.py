'''
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

if __name__ == '__main__':
