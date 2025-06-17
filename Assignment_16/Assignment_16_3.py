def func(fname):
    fobj = open(fname, 'r')
    lines = fobj.readlines()
    
    count_words = 0
    count_char = 0
    for line in lines:
        count_char += len(line)
        words = line.split(" ")
        for word in words:
            count_words += 1
    
    print("Total lines are : ", len(lines))
    print("Total words in the file are : ", count_words)
    print("Total characters in the file are : ", count_char)




def main():
    func('student.txt')


if __name__ == "__main__":
    main()