#All about the Methods:

#Instance Method:

class bottol:
    def glass(self):
        print("the bottol is made of glass")
a = bottol()
a.glass()

#Class Method:

class honey:

    @classmethod
    def sweet(cls):
        print("honey tastes sweet")
honey.sweet()

#Static Method:

class water:

    @staticmethod
    def glass():
        print("the glass is full of water")
water.glass()
