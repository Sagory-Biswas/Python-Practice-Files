#list:

li = [1,2,4,6]
print(li[2])

li[3]=9
li[1]=6
print(li)

l = ["ami","tumi","se"]
print(l)

lis = [True,False,False,True]
lis[2]=True
print(lis)

print(type(lis))

#Add list Items:
Newlist = ["sagor","samudro","saikat",123,345]
Newlist.append(3456)
print(Newlist)

Newlist.insert(3,9123)
print(Newlist)

Newlist[3]=("bela")
print(Newlist)

#Remove Lists Items:
Newlist.remove('saikat')
print(Newlist)

Newlist.pop(3)
Newlist.pop()
print(Newlist)

del Newlist[1]
print(Newlist)

Newlist.clear()
print(Newlist)



