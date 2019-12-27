''' 予測 '''
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

import pandas as pd
import numpy as np
import p72
import nltk

FILE = 'sentiment-identity.txt'
S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
W_FILE='sentiment-identity.txt'

def main():
    X = []
    Y = []
    sentiment_identity, identity = p72.take_identity(W_FILE,S_FILE,CORRECT_DATA)
    inum = len(identity)
    print('inum=', inum)
    for line in sentiment_identity:    
        y = 0 if line[:2] == "+1" else 1
        Y.append(y) 
        line = line[2:]  
        x = np.zeros(inum, dtype=np.int)
        
        for i, word in enumerate(line.split()):
            if word in identity:
                x[identity.index(word)] = 1
    
        X.append(x)
    X = np.array(X)
    Y = np.array(Y)
    print(X)
    print(Y)
    print(X.shape)
    print(Y.shape)

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    print ('start ...')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.33, random_state=12345)


    model = LogisticRegression(penalty="l2", random_state=0)
    model.fit(X_train, Y_train)

    Y_hat = model.predict(X_test)
    print(np.mean(Y_hat == Y_test))

    from sklearn.metrics import classification_report

    print(classification_report(Y_test, Y_hat))

    coef = model.coef_
    # print(coef)
    # print(len(coef[0]))
    identity_weight = list(coef[0])
    identity_dic = {}
    for i, iden in enumerate(identity):
        identity_dic[iden] = identity_weight[i]
    # print(len(identity_weight))
    # print(len(identity))
    identity_dic2 = sorted(identity_dic.items(), key=lambda x:x[1], reverse=True)
    # print(identity_dic2)
    for iden_set in identity_dic2[:10]:
        print(iden_set)
    print('----')
    for iden_set in identity_dic2[-10:]:
        print(iden_set)
if __name__ == '__main__':
    main()
