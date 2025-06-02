Sum = 0
def DigitsSum(no):
    global Sum
    Digit = 0
    if(no > 0):
        Digit = no % 10
        print(Digit)
        Sum = Sum + Digit
        no = int(no / 10)
        DigitsSum(no)
    return Sum
    

def main():
    print("Enter the number: ")
    value = int(input())
    
    Ret = DigitsSum(value)
    print("Sum of Digits of ", value, " is : ", Ret)



if __name__ == "__main__":
    main()