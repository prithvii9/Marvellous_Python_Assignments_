class Demo:
    Value = 100                                 #class variable

    def __init__(self, value1, value2):         # parameterised constructor
        self.No1 = value1                       # instance variable
        self.No2 = value2                       # instance variable

    # instance method
    def Fun(self):
        print("Inside Fun function")
        print("Value of instance variables are ", self.No1, "and", self.No2)

    # instance method
    def Gun(self):
        print("Inside Gun function")


def main():
   
   
   
    print("Value of class variable Value : ", Demo.Value)

    obj1 = Demo(11,21)          # object created
    obj2 = Demo(51, 101)        #object created

    obj1.Fun()
    obj1.Gun()

    obj2.Fun()
    obj2.Gun() 





if __name__ == "__main__":
    main()