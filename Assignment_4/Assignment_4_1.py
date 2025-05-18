
def main():
    power = lambda A : A**2

    print("Enter Number: ")
    no = int(input())

    ret = power(no)
    print("Power is :",ret)


if __name__ == "__main__":
    main()