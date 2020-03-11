import re
count=0
pattern=re.compile("TCS")
match=pattern.finditer("TCS stands for tata consultancy services.TCS is a top rated company")
for i in match:
	count=count+1
print("TCS word is existed for",count,"times")
