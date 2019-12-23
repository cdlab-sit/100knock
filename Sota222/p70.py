''' データの入手・整形 '''
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import tarfile
import random

C_FILE = 'rt-polaritydata.tar.gz'
NEG = 'rt-polaritydata/rt-polarity.neg'
POS = 'rt-polaritydata/rt-polarity.pos'
W_FILE='sentiment.txt'

def main():
    data = []
    neg_data = extract_tar_file(C_FILE, NEG)
    for line in neg_data:
        str = "-1" + line.decode("utf-8","ignore")
        data.append(str)
    neg_data_num = len(data)
    pos_data = extract_tar_file(C_FILE, POS)
    for line in pos_data:
        str = "+1" + line.decode("utf-8","ignore")
        data.append(str)
    pos_data_num = len(data) - neg_data_num
    print('neg_data_num=', neg_data_num, 'pos_data_num=', pos_data_num)
    random.shuffle(data)
    write_data(W_FILE, data)
    

def extract_tar_file(c_file, file):
    with tarfile.open(c_file, 'r:gz') as tf, tf.extractfile(file) as f:
        data = f.readlines()
    return data


def write_data(w_file, data):
    with open(w_file, mode='w') as f:
        f.writelines(data)
    print('wrote sentiment.txt') 
if __name__ == '__main__':
    main()
