Ans = 1
i = 1
def Power(x, y):
    global Ans
    global i
    if(i <= y):
        Ans = Ans * x
        i += 1
        Power(x,y)

    return Ans
    

def main():
    print("Enter the number and its power index: ")
    value1 = int(input())
    value2 = int(input())
    
    Ret = Power(value1, value2)
    print("Result:", Ret)



if __name__ == "__main__":
    main()