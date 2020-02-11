''' ラベル付け '''
# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

import pandas as pd
import numpy as np
import p72
import nltk

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
    print ('start ...')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.33, random_state=12345)


    model = LogisticRegression(penalty="l2", random_state=0)
    model.fit(X_train, Y_train)

    predict = model.predict(X_test)

    print("正解率を出力\n", accuracy_score(Y_test, predict))
    predict_proba = model.predict_proba(X_test)

    w_lines = []
    for i in range(Y_test.size):
        test_y = '+1' if Y_test[i] == 0 else '-1'
        prefict_y = '+1' if predict[i] == 0 else '-1'    
        probability= str(predict_proba[i][0] if predict[i] == 0 else predict_proba[i][1])
        line = test_y + ' ' + prefict_y + ' ' + probability
        print(line)
        w_lines.append(line)
    
    with open(W_RESULT, mode='w') as f:
        f.write('\n'.join(w_lines))


if __name__ == '__main__':
    main()
