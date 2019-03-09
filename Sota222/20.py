''' JSONデータの読み込み '''
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

# jawiki-country.jsonはjsonファイルではあるが、json形式になっているわけではない
# 第三章の問題文にも書いてあるように、一行、一行がjson形式になっているファイルである。
# よってjson.load()では読み込めず、一行ずつjson.loads()で読み込む必要がある。
# 紛らわしいわ!!


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    print(article_UK)


def get_article(file_name, article_name):
    """引数file_nameのファイルを開き、article_nameの記事を抽出する関数

    Arguments:
        file_name {str} -- 対象のファイル名
        article_name {str} -- 抽出する記事名

    Returns:
        str -- 対象の記事
    """
    with gzip.open(file_name, "r") as f_file:
        for line in f_file:
            article = json.loads(line)
            if article['title'] == article_name:
                article_UK = article['text']
                break
        print(type(article_UK))
    return article_UK

if __name__ == '__main__':
    main()
