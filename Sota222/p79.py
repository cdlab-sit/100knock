''' 適合率-再現率グラフの描画 '''
# ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

import pandas as pd
import numpy as np
import p72
import nltk
import matplotlib.pyplot as plt

FILE = 'sentiment-identity.txt'
S_FILE='stop-word.txt'
CORRECT_DATA='sentiment.txt'
W_FILE='sentiment-identity.txt'
W_RESULT = 'p76_result.txt'

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
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_recall_curve
    print ('start ...')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.33, random_state=12345)


    model = LogisticRegression(penalty="l2", random_state=0)
    model.fit(X_train, Y_train)

    precision, recall, threshold = precision_recall_curve(Y_test, model.predict_proba(X_test)[:, 1])
    for i in range(21):
        close_point = np.argmin(np.abs(threshold - (i * 0.05)))
        plt.plot(precision[close_point], recall[close_point], 'o')

    
    plt.plot(precision, recall)
    plt.xlabel('Precision')
    plt.ylabel('Recall')

    plt.show()

if __name__ == '__main__':
    main()
