#Unpack Tuple:

tup = ('cat','dog','cow','goat','ox')
(b,c,a,r,d) = tup
print(a)

(a,*c,b,e)=tup
print(c)

#Loop Tuple:

tup = ('cat','dog','cow','goat','ox')
for a in tup:
    print(a)

a = 0
while a < len(tup):

    print(tup[a])
    a += 1

for a in range(len(tup)):
    print(tup[a])

#Join Tuple:

tup1 = (1,3,5,7)
tup2 = (2,4,6,8)
tup3 = tup1 + tup2
print(tup3)

#Multiply Tuple:

print(tup3*3)

#Counting Tuple:

tpl = (1,2,1,3,4,5,3,2,5)
print(tpl.count(1))

#Indexing Tuple:

print(tpl.index(4))