''' テンプレートの抽出 '''
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import gzip
import json
import re


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    basic_infos = get_basic(article_UK)
    print(basic_infos)


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
    print(article_UK)
    return article_UK


def get_basic(article_UK):
    """引数の記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
        その辞書オブジェクトをstrに変換したものを得る

    Arguments:
        article_UK {str} -- 対象の記事

    Returns:
        str -- フィールド名と値の辞書オブジェクト
    """
    basic_pattern = r'{{基礎情報(.+?)}}\n'
    basic_infos = re.search(basic_pattern, article_UK, flags=re.DOTALL)
    print(basic_infos.group())

    basic_pattern = r'\n\|(.+?) = (.+?)\n\|'
    basic_info = re.findall(
        basic_pattern, basic_infos.group(), flags=re.DOTALL)
    basic_info_dic = {}
    for line in basic_info:
        print(f'line[0] = {line[0]}')
        print(f'line[1] = {line[1]}')
        basic_info_dic[line[0]] = line[1]
    return '\n'.join([f'{field_name}: {val}'
                      for field_name, val in basic_info_dic.items()])

if __name__ == '__main__':
    main()
