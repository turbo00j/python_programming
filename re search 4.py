import re
count=0
text=input("Enter your text:")
word=input("what is the word you wanna search:")
pattern=re.compile("word")
match=pattern.finditer("text")
for i in match:
	count=count+1
print("jai word is existed for",count,"times")


