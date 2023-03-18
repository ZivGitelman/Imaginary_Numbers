class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}j"
        else:
            return f"{self.real} - {-self.imag}j"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imag)
        elif isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise ValueError(f"Unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imag)
        elif isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise ValueError(f"Unsupported operand type(s) for -: '{type(self)}' and '{type(other)}'")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imag * other)
        elif isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        else:
            raise ValueError(f"Unsupported operand type(s) for *: '{type(self)}' and '{type(other)}'")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imag / other)
        elif isinstance(other, ComplexNumber):
            conj = ComplexNumber(other.real, -other.imag)
            num = self * conj
            denom = other.real**2 + other.imag**2
            return ComplexNumber(num.real / denom, num.imag / denom)
        else:
            raise ValueError(f"Unsupported operand type(s) for /: '{type(self)}' and '{type(other)}'")

# Create two complex numbers
a = ComplexNumber(1, 2)
b = ComplexNumber(3, -4)

# Print the two complex numbers
print(a) # Output: 1 + 2j
print(b) # Output: 3 - 4j

# Add two complex numbers
c = a + b
print(c) # Output: 4 - 2j

# Subtract two complex numbers
d = a - b
print(d) # Output: -2 + 6j

# Multiply two complex numbers
e = a * b
print(e) # Output: 11 - 2j

# Divide two complex numbers
f = a / b
print(f) # Output: (-0.2 + 0.4j)

# Add a complex number and a float
g = a + 2.5
print(g) # Output: 3.5 + 2j

# Divide a complex number by a float
h = a / 2
print(h) # Output: 0.5 + 1j
