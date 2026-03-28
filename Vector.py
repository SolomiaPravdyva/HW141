import math

class Vector:
    def __init__(self, components):
        if isinstance(components, Vector):
            self.components = components.components.copy()
        else:
            self.components = list(map(float, components))
    def __str__(self):
        return f"Vector({self.components})"
    def dimension(self):
        return len(self.components)
    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.components))
    def average(self):
        return sum(self.components) / len(self.components)
    def max_component(self):
        return max(self.components)
    def min_component(self):
        return min(self.components)

def read_vectors(filename):
    vectors = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            if parts:
                vectors.append(Vector(parts))
    return vectors

def max_dimension_vector(vectors):
    max_dim_vect = vectors[0]
    for el in vectors:
        if el.dimension() > max_dim_vect.dimension():
            max_dim_vect = el
        elif el.dimension() == max_dim_vect.dimension():
            if el.length() < max_dim_vect.length():
                max_dim_vect = el
    return max_dim_vect

def max_length_vector(vectors):
    max_length_vector = vectors[0]
    for el in vectors:
        if el.length() > max_length_vector.length():
            max_length_vector = el
        elif el.length() == max_length_vector.length():
            if el.dimension() < max_length_vector.dimension():
                max_length_vector = el
    return max_length_vector

def average_length(vectors):
    summa = 0
    for v in vectors:
        summa += v.length()
    return summa / len(vectors)

def count_above_average(vectors):
    count=0
    for v in vectors:
        if v.length() > average_length(vectors):
            count+=1
    return count

def max_component_vector(vectors):
    max_v = vectors[0]
    for el in vectors:
        if el.max_component() > max_v.max_component():
            max_v = el
        elif el.max_component() == max_v.max_component():
            if el.min_component() < max_v.min_component():
                max_v = el
    return max_v

def min_component_vector(vectors):
    min_v = vectors[0]
    for el in vectors:
        if el.min_component() < min_v.max_component():
            min_v = el
        elif el.min_component() == min_v.max_component():
            if el.max_component() < min_v.max_component():
                min_v = el
    return min_v
