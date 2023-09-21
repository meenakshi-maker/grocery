import random

fruits = [ "melon", "apricot", "kiwi", "apple","orange"]

nums = [23, 12,54, 25, 76]
bools = [True, False]

biglist = [fruits, nums,bools]

#print(fruits[2:])

#print("what is a",fruits[2])
#for x in fruits:
    #print (x)
 #fruits.sort()
 #print(fruits)
 #print(len(fruits))
 #x = fruits.index("kiwi")
# print(x)

fruits.append("grapes")
fruits.insert(2,"mango")
fruits.append("banana")
fruits.sort()
print (fruits)


#fruits.remove("melon")
z = len(fruits) - 1
fruits.pop(z)
print(fruits)
random.shuffle(fruits)
print(fruits)




