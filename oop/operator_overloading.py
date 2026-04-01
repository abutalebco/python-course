class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)
    
vector1 = Vector(3, 5)
vector2 = Vector(5, 3)

print(vector1)
print(vector1.__add__(vector2))
print(vector1.__sub__(vector2))

# class Vector3D(Vector):
#     def __init__(self, x, y, z):
#         super(Vector3D, self).__init__(x, y)
#         self.z = z

#     def __add__(self, z, other):
#         super(Vector3D, self).__add__(z)
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

#     def __sub__(self, z, other):
#         super(Vector3D, self).__sub__(z)
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
#     def __str__(self):
#         return "X: {}, Y: {}, Z: {}".format(self.x, self.y, self.z)
    
# vector3 = Vector3D(3, 5, 5)
# vector4 = Vector3D(4, 6, 6)

# print(vector3)
# print(vector4)
# print(vector3.__add__(vector4))
# print(vector3.__sub__(vector4))