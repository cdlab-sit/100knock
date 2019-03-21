''' ステミング '''
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
# 単語と語幹をタブ区切り形式で出力せよ．
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
import snowballstemmer
import p50
import p51


def main():
    file_name = 'nlp.txt'
    sentence = p50.read_file(file_name)
    sentence_list = p50.divide_sentence(sentence)
    words = p51.divide_word(sentence_list)
    stemming_words = stemming(words)
    print(stemming_words)


def stemming(words):
    stemmer = snowballstemmer.stemmer('english')
    return '\n'.join([f'{word}\t{stemmer.stemWord(word)}'
                      for word in words.split('\n')])

if __name__ == "__main__":
    main()
