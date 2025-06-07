class Rectangle:
    def __init__(self, length, width):
        self.Length = length
        self.Width = width
    
    def Area(self):
        ans = 0
        ans = self.Length * self.Width
        return ans

    def Perimeter(self):
        ans = 0
        ans = 2*(self.Length + self.Width)
        return ans


def main():
    obj = Rectangle(5, 10)
    Ret = obj.Area()
    print("Area is ", Ret)

    Ret = obj.Perimeter()
    print("Perimeter is ", Ret)
      

if __name__ == "__main__":
    main()