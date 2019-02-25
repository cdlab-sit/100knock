def n_gram(words, n):
	'''
	n-gram 05より

	第一引数：リスト
	第二引数：n値
	戻り値：n-gramのリスト
	'''
	result = []
	for i,word in enumerate(words):
		result.append(words[i:i+n])

	return result

x = "paraparaparadise" 
y = "paragraph"


#参考(ほぼ同じ)　https://qiita.com/segavvy/items/209bf27d4cee51f60f99
#セット型について　https://www.sejuku.net/blog/21923

x_bi_gram = set(n_gram(x, 2))
y_bi_gram = set(n_gram(y, 2))
#print(type(x_bi_gram))

#和集合
result_sum = x_bi_gram | y_bi_gram
print("和集合：", result_sum)

#積集合 
result_mul = x_bi_gram & y_bi_gram
print("積集合：", result_mul)

#差集合
result_diff = x_bi_gram - y_bi_gram
print("差集合：", result_diff)

#追加：排他的論理和集合
result = x_bi_gram ^ y_bi_gram
print("排他的論理和集合：", result)

#seが含まれるかの判定
print("X includes 'se:'", str("se" in x_bi_gram))
print("Y includes 'se:'", str("se" in y_bi_gram))