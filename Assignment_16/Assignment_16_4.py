def func(fname):
    fobj = open(fname, 'w')

    print("Enter 10 numbers: ")
    for i in range(10):
        value = input()
        fobj.write(value+"\n")
    
    fobj.close()

def main():
    func('numbers.txt')


if __name__ == "__main__":
    main()