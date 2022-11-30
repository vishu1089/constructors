class Test:
    # default constructor: it is a simple constructor which does not accept any arguments. it's definition has only one arg which is a reference to the instance being constructed.
    def __init__(self):
        self.test = "testing"
    
    # defining method for printing data members
    def print_testing(self):
        print(self.test)


#  creating object of a class
obj = Test() # this will call default constructor: here self.test will get the value

# calling the instance method using the object obj
obj.print_testing()
