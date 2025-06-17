import os 

def RemoveBlankLines(fname):
    fname = os.path.abspath(fname)

    fobj1 = open('cleanedfile.txt', 'w')
    fobj = open(fname, 'r')

    lines = fobj.readlines()
    for line in lines:
        data = line.strip()         #remove blank lines
        fobj1.write(data)
    
    fobj.close()
    fobj1.close()

    # lines = fobj.readlines()
    # non_blank_lines = list(filter(lambda line: line.strip(), lines))
    # return non_blank_lines

def main():
    print("Enter filename: ")
    filename = input()
    RemoveBlankLines(filename)
    
    fobj1 = open('cleanedfile.txt','r')
    data = fobj1.read()

    print("Cleaned Data : ", data)


if __name__ == "__main__":
    main()