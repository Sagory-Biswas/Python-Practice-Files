#Multilevel Inheritance:

class rahim:
    house = "10th floor"
    car = "BMW"
    phone = "iphone 14"

class jodu(rahim):
    frize = "samsung"
    tv = "sony"

class modhu(jodu):
    AC = "panasonic"
    laptop = "dell"

class kodu(modhu):
    tab = "mac"


class karim(kodu):
    home = "  "
    furniture = "almirah"

a = karim()
b = kodu()
c = jodu()
d = rahim()

print(a.tab)
print(a.tv)
print(b.frize)
print(b.car)
print(c.phone)
print(d.house)
