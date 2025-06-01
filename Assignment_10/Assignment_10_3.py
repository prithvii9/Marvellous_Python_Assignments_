from functools import reduce

def main():
    print("Enter total no of elements in the list: ")
    size = int(input())

    inputData = []

    print("Enter", size, " elements : ")
    for i in range(size):
        value = int(input())
        inputData.append(value)
    
    FData = list(filter(lambda no : (no >= 70 and no <= 90), inputData))
    print("List after filter : ", FData)

    MData = list(map(lambda no : (no+10), FData))
    print("List after map : ", MData)

    RData = reduce(lambda sum, no : sum * no, MData)
    print("Output of reduce : ", RData)



if __name__ == "__main__":
    main()