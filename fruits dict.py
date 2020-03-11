fruits_dictionary={1122:'apple',2233:'cherry'}
fruits_dictionary[3344]='mango'
print(fruits_dictionary)           #adding key value pairs to the fruits dict
print(fruits_dictionary.keys())    # keys are returned
print(fruits_dictionary.values())  #values are returned
print(fruits_dictionary.__len__())  #print(len(fruits_dictionary))
fruits_dictionary.pop(1122)
print(fruits_dictionary)
fruits_dictionary.clear()
print(fruits_dictionary)
del fruits_dictionary
print(fruits_dictionary)