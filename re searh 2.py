import re
count=0
pattern=re.compile("tcs")
f=open("tcsfile.txt",'r')
data=f.read()
match=pattern.finditer(data)
for i in match:
	count=count+1
print("TCS word is existed for",count,"times")
