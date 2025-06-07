class Product:
    def __init__(self, name, price):
        self.Name = name
        self.Price = price
    
    def __eq__(self, value):
        if (self.Price == value.Price):
            return True
        
        return False
    
    
def main():
    obj1 = Product('pen', 10)
    obj2 = Product('pencil', 10)
    obj3 = Product('eraser', 5)

    print(obj1 == obj2)
    print(obj1 == obj3)
    print(obj2 == obj3)

if __name__ == "__main__":
    main()