
class Arithmetic:

    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0
        self.Result = 0.0

    def Accept(self):
        print("Enter first value : ")
        self.Value1 = float(input())

        print("Enter second value : ")
        self.Value2 = float(input())

    def Addition(self):
        self.Result = self.Value1 + self.Value2
        return self.Result
    
    def Multiplication(self):
        self.Result = self.Value1 * self.Value2
        return self.Result

    def Subtraction(self):
        self.Result = self.Value1 - self.Value2
        return self.Result

    def Division(self):
        self.Result = self.Value1 / self.Value2
        return self.Result

   
def main():
    obj1 = Arithmetic()
    obj1.Accept()
    Ret = obj1.Addition()
    print("Addition is ", Ret)
    Ret = obj1.Subtraction()
    print("Subtraction is ", Ret)
    Ret = obj1.Division()
    print("Division is ", Ret)
    Ret = obj1.Multiplication()
    print("Multiplication is ", Ret)


if __name__ == "__main__":
    main()