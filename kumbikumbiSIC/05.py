def n_gram(words, n):
	'''
	n-gram

	第一引数：リスト
	第二引数：n値
	戻り値：n-gramのリスト
	'''
	result = []
	for i,word in enumerate(words):
		result.append(words[i:i+n])

	return result

words = "I am an NLPer"
list_words = words.split()

word_bi_gram = n_gram(list_words, 2)
print("単語bi-gram",word_bi_gram)

char_bi_gram = n_gram(words, 2)
print("文字bi-gram",char_bi_gram)