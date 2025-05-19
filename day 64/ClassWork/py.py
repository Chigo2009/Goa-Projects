class MyCat:
    cat = "კატა"

p1 = MyCat()   
print(p1.cat)  

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):     
         return f"{self.name} {self.surname} {self.age}"
    def my_name(self):
        print("My Name is "  + self.name)
            
m1 = Human("Giorgi", "Chigvinadze", 15)  
m1.my_name()    
print(m1)  
print(m1.my_name)


        
        