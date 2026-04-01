import sqlite3

connection = sqlite3.connect('database/database.db')
cursor = connection.cursor()

class Student:
    def __init__(self, id_number=-1,first_name="", last_name="", year=-1):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.connection = sqlite3.connect('database/database.db')
        self.cursor = self.connection.cursor()

    def load_data(self, id_number):
        self.cursor.execute("SELECT * FROM students WHERE id_number = ?", (id_number,))
        
        result = self.cursor.fetchone()

        if result is None:
            print(f"No student found with id_number {id_number}")

        self.id_number = id_number
        self.first_name = result[1]
        self.last_name = result[2]
        self.year = result[3]

    # def load_all_data(self):
        # self.cursor.fetchall()
        # for row in self.cursor.execute("SELECT * FROM students"):
            # print(row)

    def insert_data(self):
        self.cursor.execute("INSERT INTO students VALUES (?, '?', '?', ?)", self.id_number, self.first_name, self.last_name, self.year)
        self.connection.commit()
        self.connection.close()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id_number INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year INT           
)
""")

# cursor.execute("""
# INSERT INTO students VALUES
#     (1,"Mohamed", "Salah", 3),
#     (2, "Ahmed", "Naser", 4),
#     (3, "Maged", "Kamal", 5)
# """)


# data = [
#     (4, "Ahmed", "Hamed", 4),
#     (5, "Mohsen", "Fady", 5),
#     (6, "Kareem", "Islam", 3)
# ]

# cursor.executemany("INSERT INTO students VALUES(?, ?, ?, ?)", data)


# cursor.execute("""
# SELECT * FROM students
# """)

# rows = cursor.fetchall()
# print(rows)

# for row in cursor.execute("SELECT year, first_name, last_name FROM students ORDER BY year"):
#     print(row)

# connection.commit()
# connection.close()

# s1 = Student()
# s1.load_data(4)
# print("First Name:", s1.first_name)
# print("Last Name:", s1.last_name)
# print("Study Year:", s1.year)
# print("ID:", s1.id_number)


# s2 = Student(7, "Jamal", "Baraka", 4)
# print("First Name:", s2.first_name)
# print("Last Name:", s2.last_name)
# print("Study Year:", s2.year)
# print("ID:", s2.id_number)
 
# s3 = Student(8, "Naser", "Salem", 3)
# # s3 = Student()
# print("First Name:", s3.first_name)
# print("Last Name:", s3.last_name)
# print("Study Year:", s3.year)
# print("ID:", s3.id_number)

# s4 = Student()
# s4.load_data(7)
# print(s4.id_number)
# print(s4.first_name)
# print(s4.last_name)
# print(s4.year)

cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
print(results)

connection.close