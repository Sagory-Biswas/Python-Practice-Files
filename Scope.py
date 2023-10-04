#Scope:

a = 10
b = 20

def hello():
    global a
    a = 30
    print(a)
print(b)