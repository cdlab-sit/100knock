msg = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
msg2 = msg.split()
#print(msg2)

l = list()

for i in range(0,len(msg2)):
	word = msg2[i].replace("," , "").replace("." , "")
	#print(word)
	l.append(len(word))

print(l)