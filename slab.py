cno=int(input("Enter the construction number:"))
cname=input("Enter the construction name:")
srno=int(input("Enter the serial number:"))
erno=int(input("Enter the er no:"))
slab_type=input("Enter the slab type(i/c/r):")
if(slab_type=='i'):
    print(cno)
    print(cname)
    print(srno)
    print(erno)
    unit_rate=5.0
    print("For industry unit rate is:",unit_rate)
    units_comsumed=int(input("Enter the no of units consumed:"))
    total_cost=unit_rate*units_comsumed
    print("Total cost :",total_cost)
elif (slab_type=='c'):
    unit_rate=4.0
    print("For commertial unit rate is:",unit_rate)
    units_comsumed=int(input("Enter the no of units consumed:"))
    total_cost=unit_rate*units_comsumed
    print("Total cost :",total_cost)
elif(slab_type=='r'):
    unit_rate=5.0
    print("For residence unit rate is:",unit_rate)
    units_comsumed=int(input("Enter the no of units consumed:"))
    total_cost=unit_rate*units_comsumed
    print("Total cost :",total_cost)
else:
    print("Enter the correct slab type")