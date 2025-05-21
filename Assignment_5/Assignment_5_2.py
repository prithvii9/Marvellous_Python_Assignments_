def CheckVowel(value):
    if (value == "a" or value == "e" or value =="o"  or value == "u"):
        return True
    else:
        return False

def main():
    print("Enter Characters :")
    Char = input()

    ret = CheckVowel(Char)

    if ret == True:
        print(Char,"is Vowel: ")
    else:
        print(Char,"is a Cosonant")


if __name__ == "__main__":
    main()