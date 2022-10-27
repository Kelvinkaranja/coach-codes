''''
create a class called calculator which holds all the required operations for 
simple mathematical applications.

'''

class Calculator:
    #initialize the class and define attributes.
    def __init__(self):
        self.total = 0

    #create an adder
    def add(self,*args):
        for val in args:
            self.total += val
        return self.total

    #create a subtractor.
    def subtract(self,*args):
        for val in args:
            self.total -= val
        return self.total

    #create a multiplier
    def multiply(self,*args):
        self.total=1
        for val in args:
            self.total *= val
        return self.total

    #create a divider. The first arg is held as the value being divided...
    #...with the rest of the args being the divisors.
    def divide (self,*args):
        self.total = args[0]
        for i in args[1:]:
            self.total /= i
        return self.total
