#Set:

set = {"hello",True,False ,"2",0,1,2,3,1,22,5,6,3,1}
print(set)
print(len(set))

#Access Set Items:

for i in set:
    print(i)

print(3 in set)

#Add Set Items:

set.add("hi")
print(set)

set2 = {0,1,8,9}
set.update(set2)
print(set)

list1 = ["jug","glass"]
tuple1 = ("bread","banana")

set2.update(list1)
print(set2)

set2.update(tuple1)
print(set2)