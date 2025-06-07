class Person:
    def __init__(self, name, age):
        self.Name = name      
        self.Age = age

    
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)     #constructor
        self.Subject = subject
        self.Salary = salary
   

def main():
    obj = Teacher('Aayush', 19, 'Python-Machine Learning', 50000)
    print(f"{obj.Name}\n{obj.Age}\n{obj.Salary}\n{obj.Subject}")



if __name__ == "__main__":
    main()