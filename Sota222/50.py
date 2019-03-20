''' 文区切り '''
# 文(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
# 入力された文書を1行1文の形式で出力せよ．
import re


def main():
    file_name = 'nlp.txt'
    sentence = read_file(file_name)
    sentence_list = devide_sentence(sentence)
    print('\n'.join(sentence_list))


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def devide_sentence(sentence):
    return re.split(r'[.;:?!] [A-Z]', sentence)


if __name__ == "__main__":
    main()
