import math
class  nVector:
    def __init__(self, *args):
        self.elements = args

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("nVectors must be of the same dimension to add them.")
        new_elements = [x + y for x, y in zip(self.elements, other.elements)]
        return nVector(*new_elements)
    
    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("nVectors must be of the same dimension to add them.")
        new_elements = [x - y for x, y in zip(self.elements, other.elements)]
        return nVector(*new_elements)
    
    def __mul__(self, other):
        if isinstance(other, nVector):
            return sum(x * y for x, y in zip(self.elements, other.elements))  # Dot product
        elif isinstance(other, (int, float)):
            new_elements = [other * x for x in self.elements]  # Scalar multiplication
            return nVector(*new_elements)
    
    def __rmul__(self, other):
        if isinstance(other, nVector):
            return sum(x * y for x, y in zip(self.elements, other.elements))  # Dot product
        elif isinstance(other, (int, float)):
            new_elements = [other * x for x in self.elements]  # Scalar multiplication
            return nVector(*new_elements)
    
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.elements))

    def normalize(self):
        mag = self.magnitude()
        new_elements = [x / mag for x in self.elements]
        return nVector(*new_elements)
    def __str__(self):
        return f"nVector{self.elements}"

# Create vectors
v1 = nVector(1, 2, 3)
v2 = nVector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)

