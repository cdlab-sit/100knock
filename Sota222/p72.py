''' 素性抽出 '''
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，
# 各単語をステミング処理したものが最低限のベースラインとなるであろう．

import random
import nltk
import p71

S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
stop_words=[]

def main():
    print(get_identity(S_FILE, CORRECT_DATA))
    
def get_identity(s_file, correct_data):
    stemmer = nltk.PorterStemmer()
    stop_words = p71.make_stop_words(s_file)
    correct_data_list = p71.read_data(correct_data)
    identity = []
    for line in correct_data_list[:]:
        words = line[2:].split()
        for stop_word in stop_words:
            if stop_word in words:
                words.remove(stop_word)
        for word in words:
            identity.append(stemmer.stem(word))
    return identity
if __name__ == '__main__':
    main()
