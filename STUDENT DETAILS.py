class csstudent:

    # class variable
    stream = "cse"

    # the init method or constructer
    def __init__(self,roll):

        # intance variable
        self.roll = roll

    def setAddress(self,address):
        self.address = address

    # rotrieves instance variable
    def getAddress(self):
        return self.address

# driver code
add = csstudent(101)
add.setAddress("time, munchig")
print(add.getAddress())

# objects of csstudent class
a = csstudent(101)
b = csstudent(102)

print(a.stream) # prints "cse"

print(b.stream) # prints "cse"

print(a.roll) # prints 101


# Class variables can be accessed using class

# name also
print(csstudent.stream) # prints "cse"