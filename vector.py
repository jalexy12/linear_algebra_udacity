class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

   
    def x(self):
        return self.coordinates[0]

    
    def y(self):
        return self.coordinates[1]

    def z(self):
        if self.dimension == 3:
           return self.coordinates[2]
        else:
            return None

    def add(self, other_vector):
        new_x = self.x() + other_vector.x()
        new_y = self.y() + other_vector.y()
        if self.z() is not None and other_vector.z() is not None:
            new_z = self.z() + other_vector.z()
            return tuple([new_x, new_y, new_z])
        else:
            return tuple([new_x, new_y])

    def subtract(self, other_vector):
        new_x = self.x() - other_vector.x()
        new_y = self.y() - other_vector.y()
        if self.z() is not None and other_vector.z() is not None:
            new_z = self.z() - other_vector.z()
            return tuple([new_x, new_y, new_z])
        else:
            return tuple([new_x, new_y])

    def multiply(self, scalar):
        return tuple([z * scalar for z in self.coordinates])

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])

v3 = v1.add(v2)
print v3

v4 = Vector([7.119, 8.215])
v5 = Vector([-8.223, 0.878])
v6 = v4.subtract(v5)
print v6

v7 = Vector([1.671, -1.012, -0.318])
print v7.multiply(7.41)

