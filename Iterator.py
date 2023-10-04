#iterator:

L = [1,2,3,4,5,"ami","tumi"]
j = iter(L)

print(j.__next__())
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))