''' 学習 '''
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよう．

import pandas as pd
import numpy as np
import p72

FILE = 'sentiment-identity.txt'
S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
W_FILE='sentiment-identity.txt'

def main():
    labels = []
    texts = []
    X = []
    Y = []
    sentiment_identity, identity = p72.take_identity(W_FILE,S_FILE,CORRECT_DATA)
    inum = len(identity)
    print(identity[0])
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

if __name__ == '__main__':
    main()
