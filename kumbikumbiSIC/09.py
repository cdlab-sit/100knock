import random

given = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = given.split()

def typoglycemia(words):
	'''
	各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替える
	長さが４以下の単語は並び替えない

	引数：単語群のリスト
	戻り値：作り直した単語群のリスト
	'''

	result = []

	for word in words:

		sub_word = ""
		char_list = []

		if len(word) > 4:

			sub_word += word[0]

			for char in word[1:len(word)-1]:
				char_list.append(char)

			char_list = random.sample(char_list,len(char_list))
			for char in char_list:
				sub_word += char

			sub_word += word[len(word)-1]

			result.append(sub_word)
		
		else:
			result.append(word)

	return result

print(typoglycemia(words))


#メモ
#Python の文字列は変更できません – つまり不変 (immutable) です。
#従って、文字列のインデックスで指定したある場所に代入を行うとエラーが発生します。