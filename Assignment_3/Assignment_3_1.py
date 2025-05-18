
def addData(value):
    ans = 0
    for num in value:
        ans = ans + num
    return ans



def main():
    print("Enter Size: ")
    size = int(input())

    data = list()

    print("Enter Numbers: ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)

    ret = addData(data)

    print("Addition of all Number is: ",ret)



if __name__ == "__main__":
    main()