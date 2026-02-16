
# from computorv2 import ComputorV2
import re

from complex_numbers import ComplexNumber
from matrix import Matrix
from functions import Function
from polynomial_equation_solver import PolynomialEquationSolver
# from fractions import Fraction




# class CalculatorParser(ComputorV2):
class CalculatorParser():
    def __init__(self):
        super().__init__()
        self.expression = None
        self.position = 0
        self.variables = {}
        self.functions = {} 

    def parse(self, expression):
        self.position = 0
        self.expression = expression
        
        # Remove most whitespace but keep some for parsing
        self.expression = ' '.join(self.expression.split())
        
        # Check for =? query operator first (before other = checks)
        if '=?' in self.expression or '= ?' in self.expression:
            expr_part = self.expression.split('=')[0].strip()
            self.expression = expr_part.replace(' ', '')
            self.position = 0
            result = self.expr()
            if self.position < len(self.expression):
                raise SyntaxError(f"Unexpected character at position {self.position}")
            return result
        
        # Check for function definition (funName(var) = expression)
        func_match = re.match(r'([a-zA-Z][a-zA-Z0-9]*)\s*\(\s*([a-zA-Z][a-zA-Z0-9]*)\s*\)\s*=\s*(.+)', self.expression)
        if func_match and '?' not in expression:
            func_name, var_name, func_expr = func_match.groups()
            
            self.functions[func_name.lower()] = Function(func_name, var_name, func_expr)
            
            return self.functions[func_name.lower()].expression
        
        # Check for polynomial equation solving: funA(x) = ? or funA(x) = y?
        # Format: function_call = value?
        poly_eq_match = re.match(r'([a-zA-Z][a-zA-Z0-9]*)\s*\(\s*([a-zA-Z][a-zA-Z0-9]*)\s*\)\s*=\s*(.+)\?', self.expression)
        if poly_eq_match:
            func_name, var_name, target_value = poly_eq_match.groups()
            return self._solve_polynomial_equation(func_name, var_name, target_value.strip())
        
        # Check for variable assignment (variable = expression)
        if '=' in self.expression:
            parts = self.expression.split('=', 1)
            var_name = parts[0].strip()
            
            # Variable lookup (var = ?)
            if parts[1].strip() == '?':
                if var_name.lower() in self.variables:
                    return self.variables[var_name.lower()]
                elif var_name.lower() in self.functions:
                    return self.functions[var_name.lower()].expression
                else:
                    raise NameError(f"Variable '{var_name}' is not defined")
            
            # Variable assignment
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', var_name):
                raise SyntaxError(f"Invalid variable name: {var_name}")
            if var_name.lower() == 'i':
                raise SyntaxError("Cannot use 'i' as a variable name (reserved for imaginary unit)")
            
            self.position = 0
            self.expression = parts[1].strip().replace(' ', '')
            result = self.expr()
            self.variables[var_name.lower()] = result
            if self.position < len(self.expression):
                raise SyntaxError(f"Unexpected character at position {self.position}")
            return result
        
        # Regular expression evaluation
        self.expression = self.expression.replace(' ', '')
        self.position = 0
        result = self.expr()
        if self.position < len(self.expression):
            raise SyntaxError(f"Unexpected character at position {self.position}")
        return result

    def expr(self):
        result = self.term()
        while self.position < len(self.expression) and self.expression[self.position] in '+-':
            op = self.expression[self.position]
            self.position += 1
            if op == '+':
                result = self.add(result, self.term())
            else:
                result = self.subtract(result, self.term())
        return result

    def term(self):
        result = self.power()
        while self.position < len(self.expression) and self.expression[self.position] in '*/%':
            op = self.expression[self.position]
            # Check for ** (matrix multiplication)
            if op == '*' and self.position + 1 < len(self.expression) and self.expression[self.position + 1] == '*':
                self.position += 2
                right = self.power()
                if isinstance(result, Matrix) and isinstance(right, Matrix):
                    result = self.matrix_multiply(result, right)
                else:
                    result = result ** right
            else:
                self.position += 1
                if op == '*':
                    result = self.multiply(result, self.power())
                elif op == '/':
                    right = self.power()
                    result = self.divide(result, right)
                else:  # op == '%'
                    right = self.power()
                    if isinstance(result, (int, float)) and isinstance(right, (int, float)):
                        result %= right
                    else:
                        raise TypeError("Modulo operation only supported for numbers")
        return result
    
    def power(self):
        result = self.factor()
        if self.position < len(self.expression) and self.expression[self.position] == '^':
            self.position += 1
            exponent = self.factor()
            if isinstance(result, (int, float)) and isinstance(exponent, (int, float)):
                result = result ** exponent
            else:
                raise TypeError("Power operation only supported for numbers")
        return result

    def factor(self):
        if self.position >= len(self.expression):
            raise SyntaxError("Unexpected end of expression")
        
        # Handle unary + and - operators
        if self.expression[self.position] in '+-':
            op = self.expression[self.position]
            self.position += 1
            result = self.factor()
            return -result if op == '-' else result
        
        if self.expression[self.position].isdigit():
            start = self.position
            while (self.position < len(self.expression) and 
                   (self.expression[self.position].isdigit() or self.expression[self.position] == '.')):
                self.position += 1
            number = float(self.expression[start:self.position])
            
            # Check for implicit multiplication with 'i' (like 2i)
            if (self.position < len(self.expression) and 
                self.expression[self.position] == 'i'):
                self.position += 1
                return ComplexNumber(0, number)
            
            # Check for implicit multiplication with variables (like 2x)
            if (self.position < len(self.expression) and 
                (self.expression[self.position].isalpha() or self.expression[self.position] == '_')):
                var_start = self.position
                while (self.position < len(self.expression) and 
                       (self.expression[self.position].isalnum() or self.expression[self.position] == '_')):
                    self.position += 1
                var_name = self.expression[var_start:self.position]
                
                if var_name.lower() == 'i':
                    return ComplexNumber(0, number)
                elif var_name.lower() in self.variables:
                    var_value = self.variables[var_name.lower()]
                    return self.multiply(number, var_value)
                else:
                    raise NameError(f"Variable '{var_name}' is not defined")
            
            return number
        
        if self.expression[self.position] == '(':
            self.position += 1
            result = self.expr()
            if self.position >= len(self.expression) or self.expression[self.position] != ')':
                raise SyntaxError("Expected ')' at position {}".format(self.position))
            self.position += 1
            return result
        
        # Handle matrices [[1,2];[3,4]]
        if self.expression[self.position] == '[':
            return self.parse_matrix()
        
        # Handle imaginary unit 'i'
        if self.expression[self.position] == 'i':
            self.position += 1
            return ComplexNumber(0, 1)
        
        # Handle variable names and function calls
        if self.expression[self.position].isalpha() or self.expression[self.position] == '_':
            start = self.position
            while (self.position < len(self.expression) and 
                   (self.expression[self.position].isalnum() or self.expression[self.position] == '_')):
                self.position += 1
            var_name = self.expression[start:self.position]
            
            # Check for function call
            if (self.position < len(self.expression) and 
                self.expression[self.position] == '(' and 
                var_name.lower() in self.functions):
                return self.parse_function_call(var_name)
            
            # Handle imaginary unit 'i'
            if var_name.lower() == 'i':
                return ComplexNumber(0, 1)
            
            # Variable lookup
            if var_name.lower() not in self.variables:
                raise NameError(f"Variable '{var_name}' is not defined")
            return self.variables[var_name.lower()]
        
        raise SyntaxError("Unexpected character '{}' at position {}".format(
            self.expression[self.position], self.position))
    
    def add(self, left, right):
        """Handle addition between different types"""
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return left + right
        elif isinstance(left, ComplexNumber) or isinstance(right, ComplexNumber):
            if isinstance(left, (int, float)):
                left = ComplexNumber(left, 0)
            if isinstance(right, (int, float)):
                right = ComplexNumber(right, 0)
            return left + right
        elif isinstance(left, Matrix) and isinstance(right, Matrix):
            return left + right
        else:
            return left + right
    
    def subtract(self, left, right):
        """Handle subtraction between different types"""
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return left - right
        elif isinstance(left, ComplexNumber) or isinstance(right, ComplexNumber):
            if isinstance(left, (int, float)):
                left = ComplexNumber(left, 0)
            if isinstance(right, (int, float)):
                right = ComplexNumber(right, 0)
            return left - right
        elif isinstance(left, Matrix) and isinstance(right, Matrix):
            return left - right
        else:
            return left - right
    
    def multiply(self, left, right):
        """Handle multiplication between different types"""
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return left * right
        elif isinstance(left, ComplexNumber) or isinstance(right, ComplexNumber):
            if isinstance(left, (int, float)):
                left = ComplexNumber(left, 0)
            if isinstance(right, (int, float)):
                right = ComplexNumber(right, 0)
            return left * right
        elif isinstance(left, Matrix) or isinstance(right, Matrix):
            if isinstance(left, Matrix) and isinstance(right, (int, float)):
                return left * right
            elif isinstance(left, (int, float)) and isinstance(right, Matrix):
                return right * left
            elif isinstance(left, Matrix) and isinstance(right, Matrix):
                return left * right
        else:
            return left * right
    
    def divide(self, left, right):
        """Handle division between different types"""
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        elif isinstance(left, ComplexNumber) or isinstance(right, ComplexNumber):
            if isinstance(left, (int, float)):
                left = ComplexNumber(left, 0)
            if isinstance(right, (int, float)):
                right = ComplexNumber(right, 0)
            return left / right
        else:
            return left / right
    
    def matrix_multiply(self, left, right):
        """Handle matrix multiplication (A ** B)"""
        if left.cols != right.rows:
            raise ValueError(f"Cannot multiply {left.rows}x{left.cols} matrix with {right.rows}x{right.cols} matrix")
        
        result = []
        for i in range(left.rows):
            row = []
            for j in range(right.cols):
                sum_val = 0
                for k in range(left.cols):
                    sum_val += left.data[i][k] * right.data[k][j]
                row.append(sum_val)
            result.append(row)
        return Matrix(result)
    
    def parse_matrix(self):
        """Parse matrix syntax: [[1,2];[3,4]]"""
        if self.expression[self.position] != '[':
            raise SyntaxError("Expected '[' at start of matrix")
        
        self.position += 1  # Skip opening '['
        rows = []
        
        while self.position < len(self.expression):
            if self.expression[self.position] == '[':
                # Parse a row
                self.position += 1  # Skip '['
                row = []
                
                while self.position < len(self.expression) and self.expression[self.position] != ']':
                    if self.expression[self.position] == ',':
                        self.position += 1
                        continue
                    
                    # Parse number
                    start = self.position
                    if self.expression[self.position] in '+-':
                        self.position += 1
                    while (self.position < len(self.expression) and 
                           (self.expression[self.position].isdigit() or self.expression[self.position] == '.')):
                        self.position += 1
                    
                    if start == self.position:
                        raise SyntaxError("Expected number in matrix")
                    
                    row.append(float(self.expression[start:self.position]))
                
                if self.position >= len(self.expression) or self.expression[self.position] != ']':
                    raise SyntaxError("Expected ']' to close matrix row")
                
                self.position += 1  # Skip ']'
                rows.append(row)
                
                # Check for semicolon (row separator) or end of matrix
                if self.position < len(self.expression):
                    if self.expression[self.position] == ';':
                        self.position += 1
                    elif self.expression[self.position] == ']':
                        break
            elif self.expression[self.position] == ']':
                break
            else:
                raise SyntaxError(f"Unexpected character '{self.expression[self.position]}' in matrix")
        
        if self.position >= len(self.expression) or self.expression[self.position] != ']':
            raise SyntaxError("Expected ']' to close matrix")
        
        self.position += 1  # Skip closing ']'
        
        if not rows:
            raise SyntaxError("Empty matrix not allowed")
        
        # Validate all rows have same length
        row_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != row_length:
                raise SyntaxError(f"All matrix rows must have same length")
        # print(Matrix(rows))
        return Matrix(rows)
    
    def parse_function_call(self, func_name):
        """Parse and evaluate function call: funA(2)"""
        if func_name.lower() not in self.functions:
            raise NameError(f"Function '{func_name}' is not defined")
        
        self.position += 1  # Skip '('
        
        # Parse argument
        arg_value = self.expr()
        
        if self.position >= len(self.expression) or self.expression[self.position] != ')':
            raise SyntaxError("Expected ')' to close function call")
        
        self.position += 1  # Skip ')'
        
        # Evaluate function
        func = self.functions[func_name.lower()]
        
        # Create a temporary parser with the function's variable set to the argument
        temp_parser = CalculatorParser()
        temp_parser.variables = self.variables.copy()
        temp_parser.variables[func.variable.lower()] = arg_value
        temp_parser.functions = self.functions.copy()
        
        # Parse and evaluate the function expression
        return temp_parser.parse(func.expression)
    
    def _solve_polynomial_equation(self, func_name, var_name, target_value):
        """
        Solve polynomial equation: funA(x) = target_value for x
        If target_value is empty or '0', solves funA(x) = 0
        """
        # Check if function exists
        if func_name.lower() not in self.functions:
            raise NameError(f"Function '{func_name}' is not defined")
        
        func = self.functions[func_name.lower()]
        
        # Get the function expression
        func_expr = func.expression
        
        # If target value is not empty and not 0, create equation: func_expr - target_value = 0
        if target_value and target_value != '0':
            # Parse target value
            try:
                target = float(target_value)
                # Create new expression: func_expr - target
                equation_expr = f"({func_expr})-({target})"
            except ValueError:
                raise SyntaxError(f"Invalid target value: {target_value}")
        else:
            equation_expr = func_expr
        
        # Create polynomial solver
        solver = PolynomialEquationSolver(equation_expr, func.variable)
        
        # Get degree and display info
        degree = solver.get_degree()
        print(f"\nSolving: {func_name}({func.variable}) = {target_value if target_value else '0'}")
        print(f"Equation: {equation_expr} = 0")
        print(f"Polynomial degree: {degree}")
        
        if degree > 2:
            return "Error: Can only solve polynomials of degree ≤ 2"
        
        # Solve the equation
        solutions = solver.solve()
        
        # Format and return solutions
        if isinstance(solutions, str):
            print(f"Result: {solutions}")
            return solutions
        elif len(solutions) == 1:
            result = f"{func.variable} = {solutions[0]}"
            print(f"Solution: {result}")
            return result
        else:
            print("Solutions:")
            results = []
            for i, sol in enumerate(solutions, 1):
                sol_str = f"{func.variable}{i} = {sol}"
                print(f"  {sol_str}")
                results.append(sol_str)
            return "\n".join(results)