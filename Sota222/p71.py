''' ストップワード '''
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
# それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

import random

S_FILE='stop-word.txt'

def main():
    stop_words = make_stop_words(S_FILE)
    print(check_stop_words('an', stop_words))
    print(check_stop_words('aaa', stop_words))

def make_stop_words(s_file):
    stop_words=[]
    data = read_data(s_file)
    for line in data:
        stop_words += line.split()
    return stop_words

def check_stop_words(word, stop_words):
    if word in stop_words:
        return True
    else:
        return False

def read_data(s_file):
    with open(s_file, mode='r') as f:
        data = f.readlines()
    return data

    
if __name__ == '__main__':
    main()
