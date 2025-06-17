import sys
import os 

def CopyFile(Fname):
    fobj1 = open("Demo.txt", 'w')
    fobj2 = open(Fname,'r')

    data = fobj2.read()
    fobj1.write(data)

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("--u : Usage")
            print("ScriptName.py Argument1 Argument2")
            
        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("Usage for copying the contents of the file using Command Line Arguments")
            print("ScriptName.py Argument1 Argument2")
        else:
            CopyFile(sys.argv[1])   
            print("Contents copied in the file Demo.txt")         
    else:
        print("Invalid number of Command Line Arguements")
        print("use --h for help")
        print("use --u for usage")


if __name__ == "__main__":
    main()