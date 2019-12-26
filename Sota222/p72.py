''' 素性抽出 '''
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，
# 各単語をステミング処理したものが最低限のベースラインとなるであろう．

import random
import nltk
import p71

S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
W_FILE='sentiment-identity.txt'
stop_words=[]


def main():
    sentiment_identity, identity = take_identity(W_FILE, S_FILE, CORRECT_DATA)
    write_data(W_FILE, sentiment_identity)
    print(' '.join(identity))
    print(len(identity))

def take_identity(w_file, s_file, correct_data):
    stemmer = nltk.PorterStemmer()
    stop_words = p71.make_stop_words(s_file)
    correct_data_list = p71.read_data(correct_data)
    sentiment_identity = []
    identity = []
    for line in correct_data_list[:]:
        words = line[2:].split()
        # print(' '.join(words))
        for i, word in enumerate(words):
            if not word.isalpha() or word in stop_words:
                words.remove(word)
            else :
                words[i] = stemmer.stem(word)
                identity.append(words[i])
        one_line = line[:2] + ' '.join(words)
        sentiment_identity.append(one_line)
    identity = list(set(identity))
    identity.sort()
    # print(sentiment_identity)
    return sentiment_identity, identity

def write_data(file, data):
    f =  open(file, 'w')
    for line in data:
        f.write(line)
        f.write('\n')
    f.close()
if __name__ == '__main__':
    main()
