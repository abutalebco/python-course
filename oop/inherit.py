class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12
    
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text
    
class Student(Person):
    def __init__(self, name, age, height, year):
        super(Student, self).__init__(name, age, height)
        self.year = year

    def get_year(self):
        return self.year
    
    def __str__(self):
        text = super(Student, self).__str__()
        text += ", Year: {}".format(self.year)
        return text
    
worker1 = Worker("Hamza", 23, 180, 3000)
student1 = Student("Vermont", 19, 186, 4)

print(worker1)
print(worker1.yearly_salary())

print(student1)
print(student1.get_year())