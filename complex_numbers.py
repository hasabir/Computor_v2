
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = float(real)
        self.imag = float(imag)
    
    def __str__(self):
        if self.imag == 0:
            return str(self.real)
        elif self.real == 0:
            return f"{self.imag}i" if self.imag != 1 else "i"
        else:
            sign = "+" if self.imag >= 0 else "-"
            imag_part = abs(self.imag)
            imag_str = "i" if imag_part == 1 else f"{imag_part}i"
            return f"{self.real} {sign} {imag_str}"
    
    def __neg__(self):
        """Unary negation: -z returns -real - imag*i"""
        return ComplexNumber(-self.real, -self.imag)
    
    def __pos__(self):
        """Unary positive: +z returns z"""
        return ComplexNumber(self.real, self.imag)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imag)
        elif isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imag)
        elif isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.real, -self.imag)
        elif isinstance(other, ComplexNumber):
            return ComplexNumber(other.real - self.real, other.imag - self.imag)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imag * other)
        elif isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imag / other)
        elif isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imag**2
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return ComplexNumber(real, imag)
        return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            denom = self.real**2 + self.imag**2
            real = (other * self.real) / denom
            imag = (-other * self.imag) / denom
            return ComplexNumber(real, imag)
        return NotImplemented
