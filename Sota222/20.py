''' JSONデータの読み込み '''
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json
from os.path import dirname, join

# jawiki-country.jsonはjsonファイルではあるが、json形式になっているわけではない
# 第三章の問題文にも書いてあるように、一行、一行がjson形式になっているファイルである。
# よってjson.load()では読み込めず、一行ずつjson.loads()で読み込む必要がある。
# 紛らわしいわ!!
with gzip.open(join(dirname(__file__), 'jawiki-country.json.gz'), "r") as f:
    for line in f:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            article_UK = article['text']
            break


with open(join(dirname(__file__), 'article_UK.json'), "w") as f:
    json.dump(article_UK, f)  # json形式で書き込み

    # json.dump(article_UK, f, ensure_ascii=False,
    #                indent=4, sort_keys=True, separators=(',', ': '))
