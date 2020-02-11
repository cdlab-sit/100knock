''' 5分割交差検定 '''
# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
# すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
# そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

import pandas as pd
import numpy as np
import p72
import nltk

FILE = 'sentiment-identity.txt'
S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
W_FILE='sentiment-identity.txt'
W_RESULT = 'p78_result.txt'

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
        
        for _, word in enumerate(line.split()):
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
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import cross_validate
    print ('start ...')

    model = LogisticRegression(penalty="l2", random_state=0)

    scores = cross_validate(model, X, Y, cv=5, scoring=['accuracy', 'precision', 'recall', 'f1'])
    print('accuracy=', scores['test_accuracy'].mean(), ' precision=', scores['test_precision'].mean(), ' recall=', scores['test_recall'].mean(), 'f=', scores['test_f1'].mean())


if __name__ == '__main__':
    main()
