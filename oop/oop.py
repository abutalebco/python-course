class Person:
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    # def getPerson(self):
    #     print("Name:", self.name)
    #     print("Age:", self.age)
    #     print("Height:", self.height)

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
    
    def __del__(self):
        Person.amount -= 1

person1 = Person("Mohamed", 20, 132)
person2 = Person("Ahmed", 32, 150)

print(person1.__str__())
print(person2.__str__())

print(Person.amount)

person1.__del__()

print(Person.amount)