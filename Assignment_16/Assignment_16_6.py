import os 

def FileCopy(fname1, fname2):
    if(os.path.abspath(fname1) == False):
        fname1 = os.path.abspath(fname1)
    
    if(os.path.abspath(fname2) == False):
        fname2 = os.path.abspath(fname2)
    
    if(os.path.isabs(fname1) == False):
        print("Invalid path")
        exit()
    
    if(os.path.isabs(fname2) == False):
        print("Invalid path")
        exit()
    
    if(os.path.isfile(fname1) == False):
        print("Path is valid, but it is not a File")
    
    if(os.path.isfile(fname2) == False):
        print("Path is valid, but it is not a File")

    fobj1 = open(fname1, 'r')
    fobj2 = open(fname2, 'w')

    data = fobj1.read()
    fobj2.write(data)
    print("Data successfully copied from ", fname1, " to ", fname2)

    fobj1.close()
    fobj2.close()

def main():
    FileCopy('source.txt', 'destination.txt')


if __name__ == "__main__":
    main()