''' カテゴリ名を含む行を抽出 '''
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    category = get_category(article_UK)
    print(category)


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


def get_category(article_UK):
    """引数の記事からカテゴリ名を宣言している行を得る関数

    Arguments:
        article_UK {str} -- 対象の記事名

    Returns:
        str -- カテゴリ名を宣言している行
    """
    article_UK_list = article_UK.split()
    category_line = []
    for line in article_UK_list:
        if 'Category' in line:
            category_line.append(line)
    return '\n'.join(category_line)

if __name__ == '__main__':
    main()
