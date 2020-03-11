
ans="yes"
while(ans=="yes"):
    try:
        file_name=input("Enter your file name")
        f=open(file_name,'r')
        data=f.read()
        print(data)
        f.close()
    except:
        print("your file is not found")
    ans=input("do you want to enter again (yes/no):")
