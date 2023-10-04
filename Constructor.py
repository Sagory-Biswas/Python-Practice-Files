#Constructor:

class vase:
    def plant(self,name,number,color):
        print(f"the flower name is {name},the number of flower: {number},the color of flower is {color}")

v1 = vase()
v1.plant("rose",4,"red")
v1.plant("marigold",10,"yellow")
v1.plant("jasmin",14,"white")


#Parameterized Constructor:

class top:
    def __init__(self,name,number,color):
        print(f"flower name: {name},number of flowers: {number},color of flower: {color}")
t1 = top("rangan",23,"red")
t1 = top("belly",34,"white")
