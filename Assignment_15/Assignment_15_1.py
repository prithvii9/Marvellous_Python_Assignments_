import os

def ChckFile(Fname):
    ret = os.path.exists(Fname)
    return ret

def main():
    print("Enter the Name of the File: ")
    filename = input()

    ret = ChckFile(filename)

    if(ret):
        print(filename,"exits in current Directory")
    else:
        print(filename,"Does not Exits in Current Directory ")


if __name__ == "__main__":
    main()