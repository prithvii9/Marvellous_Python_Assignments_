Fact = 1

def Factorial(No):
    global Fact
    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)


def main():
    print("Enter the number: ")
    value = int(input())
    
    Ret = Factorial(value)
    print("Factorial of ", value, " is : ", Ret)



if __name__ == "__main__":
    main()