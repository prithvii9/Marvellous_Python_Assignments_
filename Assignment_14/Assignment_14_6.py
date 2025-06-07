class Calculator:
    def __init__(self, no1, no2):
        self.No1 = no1
        self.No2 = no2
    
    def Add(self):
        ans = 0
        ans = self.No1 + self.No2
        return ans
    
    def Subtract(self):
        ans = 0
        ans = self.No1 - self.No2
        return ans
    
    def Multiply(self):
        ans = 0
        ans = self.No1 * self.No2
        return ans
    
    def Divide(self):
        ans = 0
        ans = self.No1 / self.No2
        return ans
                 

def main():
    print("Enter the two numbers : ")
    no1 = float(input())
    no2 = float(input())

    obj = Calculator(no1, no2)
    Ret = obj.Add()
    print("Addition : ", Ret)
    Ret = obj.Subtract()
    print("Subtraction : ", Ret)
    Ret = obj.Multiply()
    print("Multiplication : ", Ret)
    Ret = obj.Divide()
    print("Division : ", Ret)
    

if __name__ == "__main__":
    main()