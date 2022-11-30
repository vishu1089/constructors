class Add:
    first = 0
    second = 0
    third = 0

    # parametrized constructor: constructor with parameter is always known as parametrized constructor. 
    # the parametrized constructor taked its first argument as a reference to the instance being constructed known as self and the rest of the args are provided by the programmer

    # definin parametrized constructors
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def display(self):
        print("first number: "+str(self.first))
        print("Addition = "+str(self.answer))
    
    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
# this will invoke parametrized constructor

n = input()
m = input()
obj = Add(m,n)

# perfom addition
obj.calculate()

# display ans
obj.display()
