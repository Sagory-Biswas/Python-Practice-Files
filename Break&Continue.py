#Break & Continue:

list = ["a","b","c","d","e"]
for x in list:
     if x == "d":
      continue
     print(x)

list = [2,5,7,8,9,3]
for x in range(len(list)):
     if x == 3:
      break
     print(x)