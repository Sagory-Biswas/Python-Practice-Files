#Remove Set Items:

set = {"hello",True,False ,"2",0,1,2,3,1,22,5,6,3,1}
set.remove("hello")
print(set)

set.discard(9)
print(set)

set.pop()
print(set)

set.clear()
print(set)

#Set Loop:

for j in set:
    print(j)


#Join Set Items:

set1 = {1,2,3}
set2 = {3,4,5}
x= set1.union(set2)
print(x)

set2.update(set1)
print(set2)
