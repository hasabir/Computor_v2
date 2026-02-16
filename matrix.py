
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __str__(self):
        """Display matrix in clear multiline format"""
        if self.rows == 0:
            return "[]"
        
        # Single row matrix - display on one line
        if self.rows == 1:
            return "[" + ", ".join(str(x) for x in self.data[0]) + "]"
        
        # Multi-row matrix - display in multiline format
        result = "[\n"
        for i, row in enumerate(self.data):
            result += " [" + ", ".join(str(x) for x in row) + "]"
            if i < self.rows - 1:
                result += "\n"
        result += "\n]"
        return result
    
    def compact_str(self):
        """Return compact string representation: [[2,3];[4,3]]"""
        result = "["
        for i, row in enumerate(self.data):
            if i > 0:
                result += ";"
            result += "[" + ",".join(str(x) for x in row) + "]"
        result += "]"
        return result
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions must match for addition")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions must match for subtraction")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] - other.data[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result.append([x * other for x in row])
            return Matrix(result)
        elif isinstance(other, Matrix):
            # Element-wise multiplication
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions must match for element-wise multiplication")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] * other.data[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
