class Cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def car_description(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")

car = Cars("BMW", "GTR", 2009)
car.car_description()

print("-------------------------")

                                                      # 2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def student_stats(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"grade: {self.grade}")

student_info = Student("Lukas", 21, 9)
student_info.student_stats()

                                               # if passes
def is_passing(self):
    if self.grade > 5:
        return True


print("-------------------------")

                                                       # 3
class Dog:
    def __init__(self, dog_name, dog_age):
        self.dog_name = dog_name
        self.dog_age = dog_age

    def dog_info(self):
        print(f"Dog: {self.dog_name}")
        print(f"Age: {self.dog_age}")

dog_completed = Dog("jeka", 3)
dog_completed.dog_info()

def bark():
    print("bark")

bark()


                                                    # 4

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle_info = Rectangle(5, 10)
print(f"Area: {rectangle_info.area()}")


                                                   # 5

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
