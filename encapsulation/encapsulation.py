class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def gender(self):
        return self.__gender 
    
    @gender.setter
    def gender(self, value):
        self.__gender= value

    @staticmethod
    def divider():
        print("===" * 4)

p1 = Person("Mohamed", 20, "m")

print("Name:", p1.name)
Person.divider()
print("Age:", p1.age)
Person.divider()
print("Gender:", p1.gender)