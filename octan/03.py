# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

string = 'Now I need a drink, alcoholic of course, after the heavy lectures '\
    'involving quantum mechanics.'
words_list = string.split()
# print(str_list)

wordnum_list = []
for word in words_list:
    # word = word.replace(",", "")
    # word = word.replace(".", "")
    word = word.replace(",", "").replace(".", "")
    wordnum = len(word)
    wordnum_list.append(wordnum)
print(wordnum_list)
