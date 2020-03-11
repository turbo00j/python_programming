drive=input("Enter the drive:")
file_name=input("Enter the file name:")
file_mode=input("Enter the operation that u want to do on the file:")
file_path=drive+file_name
f=open(file_path,file_mode)
data=input("Enter data:")
f.write(data)
print("Your data is printed succesfully")
f.close()
