Sum = 0
i = 1
def CalculateSum(no):
    global Sum
    global i
    if(i <= no):
        Sum += i
        i += 1
        CalculateSum(no)

    return Sum
        
    
    

def main():
    print("Enter the number: ")
    value = int(input())
    
    Ret =  CalculateSum(value)
    print("Sum of first ", value, " Natural numbers is : ", Ret)



if __name__ == "__main__":
    main()