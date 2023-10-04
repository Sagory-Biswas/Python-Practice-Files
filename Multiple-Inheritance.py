#Multiple Inheritance:

class rahim():
    house = "10th floor"
    car = "BMW"
    phone = "iphone 14"

class jodu():
    frize = "samsung"
    tv = "sony"

class modhu():
    AC = "panasonic"
    laptop = "dell"

class kodu():
    tab = "mac"


class karim(rahim,jodu,modhu,kodu):
    home = "  "
    furniture = "almirah"

a = karim()

print(a.car)
print(a.home)
print(a.phone)
print(a.tab)
print(a.AC)
print(a.frize)
print(a.home)
