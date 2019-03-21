''' 単語の切り出し '''
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，
# 1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
import p50


def main():
    file_name = 'nlp.txt'
    sentence = p50.read_file(file_name)
    sentence_list = p50.divide_sentence(sentence)
    words = divide_word(sentence_list)
    print(words)


def divide_word(sentence_list):
    word_list = []
    for sentence in sentence_list:
        for word in sentence.split(' '):
            word_list.append(word)
        word_list.append(' ')
    return '\n'.join(word_list)

if __name__ == "__main__":
    main()
