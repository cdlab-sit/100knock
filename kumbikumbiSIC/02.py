msg1 = "パトカー"
msg2 = "タクシー"
msg_ans = ""

msg1 = list(msg1)
msg2 = list(msg2)

for i in range(0, len(msg1)):
	msg_ans += msg1[i]
	msg_ans += msg2[i]
	
print(msg_ans)