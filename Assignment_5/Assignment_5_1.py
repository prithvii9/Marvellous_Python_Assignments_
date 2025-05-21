def Add(value1,value2):
    return value1 + value2

def Difference(value1,value2):
    return value1 - value2

def Product(value1,value2):
    return value1 * value2

def Division(value1,value2):
    return value1 / value2


def main():
    print("Enter First No: ")
    no1 = int(input())

    print("Enter Second Number: ")
    no2 = int(input())

    Aret = Add(no1,no2)
    print("Sum : ",Aret)

    dret = Difference(no1,no2)
    print("Difference : ",dret)

    dret = Product(no1,no2)
    print("Product : ",dret)

    dret = Division(no1,no2)
    print("Division : ",dret)


if __name__ == "__main__":
    main()