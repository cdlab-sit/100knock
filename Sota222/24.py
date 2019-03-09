'''  ファイル参照の抽出 '''
# 記事から参照されているメディアファイルをすべて抜き出せ．

import gzip
import json
import re


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    media_files = get_media(article_UK)
    print(media_files)


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
    return article_UK


def get_media(article_UK):
    """引数の記事から参照されているメディアファイル得る関数

    Arguments:
        article_UK {str} -- 対象の記事名

    Returns:
        str -- メディアファイル
    """
    m_file_pattern = r'(?:File|ファイル):(.+?)\|'
    media_files = re.findall(m_file_pattern, article_UK)
    return '\n'.join(media_files)

if __name__ == '__main__':
    main()
