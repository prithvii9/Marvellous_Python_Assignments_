import Arithmatic 

def main():
    print("Enter First Number:")
    no1 = int(input())

    print("Enter Second Number: ")
    no2 = int(input())

    print("Enter Your Choice")
    print("Addition")
    print("Substraction")
    print("Multiplication")
    print("Division")

    choice = int(input())

    if choice == 1:
        ret = Arithmatic.Add(no1,no2)
        print("Addition is :",ret)
    elif choice == 2:
        ret = Arithmatic.Sub(no1,no2)
        print("Subtraction is: ",ret)
    elif choice == 3:
        ret = Arithmatic.Mult(no1,no2)
        print("Multiplication is : ",ret)
    elif choice == 4:
        ret = Arithmatic.Div(no1,no2)
        print("Division is : ",ret)
    else:
        print("Enter correct Choice")


if __name__ == "__main__":
    main()