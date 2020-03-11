smart_phone_models=eval(input("Enter the models of smart phone:"))
smart_phone_prices=eval(input("Enter smart_phone  prices:"))
smart_phone_dict={}
for i in range(0,4):
    smart_phone_dict[smart_phone_models[i]]=smart_phone_prices[i]
for i in smart_phone_dict:
    print(i,"     ",smart_phone_dict[i])
    
    
