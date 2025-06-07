class Vehicle:
    def start(self):
        print("Inside start of Vehicle class")
    
    
class Car(Vehicle):

    def start(self):
        super().start()
        print("Inside start of Car class")
        

    
def main():
    obj1 = Vehicle()
    obj2 = Car()

    obj1.start()
    obj2.start()

    


if __name__ == "__main__":
    main()