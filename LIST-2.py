#Loop List:

#Loop Comprehension:

Loop = [3,5,6,8,3]
new = [i*3 for i in Loop]
print(new)

#Sort List:

name = ['ami','rumi','promi','sami','isha']
name.sort(reverse=True)
print(name)

num = [2,5,7,2,8,0,1,5]
num.sort()
print(num)

#Copy List:
hello = [3,6,8,3,2,9,0]
hello.sort(reverse=True)
hi = hello.copy()
print(hi)
print(hello)

#Join Two Lists:
list1 = [12,34,56,76]
list2 = ['mango','jackfruit','berry']
list3 = list2 + list1
print(list3)

list1.extend(list2)
print(list1)
