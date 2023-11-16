class Person:
    name = ""
    age = 0
    country = ""
    def description(self):
        print(f"hi my name is {self.name}, and i am {self.age} years old and i am from {self.country}")
        
person1 = Person()
person1.name = "Mikkel"
person1.age = 24
person1.country = "Denmark"

person1.description()