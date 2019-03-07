''' JSONデータの読み込み '''
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json
from os.path import dirname, join

with gzip.open(join(dirname(__file__), 'jawiki-country.json.gz'), "r") as f:
    for line in f:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            article_UK = article['text']
            break
print(article_UK)
