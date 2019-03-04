# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

str = 'Now I need a drink, alcoholic of course, after the heavy lectures '\
    'involving quantum mechanics.'
str_list = str.split()
# print(str_list)

wordnum_list = []
for word in str_list:
    # word = word.replace(",", "")
    # word = word.replace(".", "")
    # replase()を連ねる。そういうのもあるのか
    wordnum_list.append(len(word.replace(",", "").replace(".", "")))
print(wordnum_list)
