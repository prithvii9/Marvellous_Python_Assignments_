import sys
import os
import filecmp


def CompareFile(Fname1,Fname2):
    if(os.path.isabs(Fname1) == False):
        Fname1 = os.path.abspath(Fname1)
    if(os.path.isabs(Fname2) == False):
        Fname1 = os.path.abspath(Fname2)

    if(os.path.exists(Fname1) == False):
        print("path does not exists : ", Fname1)
        exit()
    if(os.path.exists(Fname2) == False):
        print("path does not exists : ", Fname2)
        exit()

    if(os.path.isfile(Fname1) == False):
        print("Path is valid but it is not a file: ", Fname1)
    if(os.path.isfile(Fname2) == False):
        print("Path is valid but it is not a file: ", Fname2)

    ret = filecmp.cmp(Fname1, Fname2)
    return ret 

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("--u : Usage")
            print("ScriptName.py Argument1 Argument2")
            
        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("Usage for copying the contents of the file using Command Line Arguments")
            print("ScriptName.py Argument1 Argument2")
        else:
            print("No such command. Use the commands below for instructions:")
            print('--h : Help')
            print('--u : Usage')
    elif(len(sys.argv) == 3):
        ret = CompareFile(sys.argv[1], sys.argv[2]) 
        if(ret == True):
            print("Same ")
        elif(ret == False):
            print("Not same")                  
    else:
        print("Invalid number of Command Line Arguements")
        print("use --h for help")
        print("use --u for usage")


if __name__ == "__main__":
    main()
    