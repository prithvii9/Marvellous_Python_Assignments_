import os

def main():
    print("Enter the name of file: ")
    filename = input()

    fobj = open(filename,'r')
    dataf = fobj.read()

    print(dataf)
    

if __name__ == "__main__":
    main()