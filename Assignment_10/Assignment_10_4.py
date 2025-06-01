from functools import reduce


def main():
    print("Enter total no of elements in the list: ")
    size = int(input())

    inputData = []

    print("Enter", size, " elements : ")
    for i in range(size):
        value = int(input())
        inputData.append(value)
    
    print(inputData)
    
    FData = list(filter(lambda no : (no % 2 == 0), inputData))
    print("List after filter : ", FData)

    MData = list(map(lambda no : (no*no), FData))
    print("List after map : ", MData)

    RData = reduce(lambda A, B : A + B, MData)
    print("Output of reduce : ", RData)



if __name__ == "__main__":
    main()