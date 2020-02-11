''' 正解率の計測 '''
# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

import numpy as np

W_RESULT = 'p76_result.txt'

def main():
    tp = fp = fn = tn = 0 # (正解, 予想), tp=(+1, +1), fp=(+1, -1), fn=(-1, +1), tn=(-1, -1)
    with open(W_RESULT, mode='r') as f:
        for line in f:
            words = line.split(' ')
            if words[0] == '+1' and words[1] == '+1':
                tp +=1
            elif words[0] == '+1' and words[1] == '-1':
                fp +=1
            elif words[0] == '-1' and words[1] == '+1':
                fn +=1
            elif words[0] == '-1' and words[1] == '-1':
                tn +=1
        print(tp, fp, fn, tn)
        accuracy = (tp + tn) / (tp + fp + fn + tn)
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f = (2 * precision * recall) / (precision + recall)
        print('accuracy=', accuracy, ' precision=', precision, ' recall=', recall, 'f=', f)

if __name__ == '__main__':
    main()
