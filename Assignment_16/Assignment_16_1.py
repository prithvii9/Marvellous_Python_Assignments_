

def main():
    fobj = open('student.txt','w')
    print("Student.txt File is Created in Directory")

    print("Enter the Names of 5 student: ")
    for i in range(5):
        name = input()
        fobj.write(name+"\n")

        

if __name__ == "__main__":
    main()