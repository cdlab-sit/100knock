def cipher(sentence):
	'''
	英小文字ならば(219 - 文字コード)の文字に置換
	その他の文字はそのまま出力
	参考: https://note.nkmk.me/python-capitalize-lower-upper-title/
	参考: https://tanishiking24.hatenablog.com/entry/python-charset

	引数：文字列
	戻り値：変換した文字列
	'''
	for char in sentence:
		result = ""
		print("変換前: ", end = "")
		for char in sentence:
			print(char, end = "")

			if char.islower():
				#ord()により、ある文字に対応するコードポイント(の10進数表記を得ることができる)
				#chr()により、あるコードポイント(の10進数整数)から対応する文字を得ることができる
	 			result = result + chr(219 - ord(char))
			#その他
			else:
				result = result + char

		print("")		#end = "" との対応のため
		return result

print("変換後:", cipher("Hikaru_Morita"))