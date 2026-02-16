"""
Polynomial Equation Solver for degree <= 2
Solves equations in the form: ax^2 + bx + c = 0
Returns real or complex solutions
"""

from complex_numbers import ComplexNumber
import re

class PolynomialEquationSolver:
    def __init__(self, expression, variable='x'):
        """
        Initialize solver with a polynomial expression
        expression: string like "x^2 + 3*x + 2" or "2*x - 4"
        variable: the variable name (default 'x')
        """
        self.expression = expression
        self.variable = variable
        self.coefficients = self._parse_polynomial()
    
    def _parse_polynomial(self):
        """
        Parse polynomial expression and extract coefficients
        Returns dict: {degree: coefficient}
        """
        # Replace ^ with ** for easier parsing
        expr = self.expression.replace('^', '**')
        
        # Add explicit multiplication: 3x -> 3*x
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        
        # Remove all spaces and parentheses for easier parsing
        expr_clean = expr.replace(' ', '').replace('(', '').replace(')', '')
        
        coefficients = {}
        
        # Extract x**2 terms (degree 2)
        degree_2_pattern = r'([+-]?\d*\.?\d*)\*?' + self.variable + r'\*\*2'
        matches = re.findall(degree_2_pattern, expr_clean)
        coef_2 = 0
        for match in matches:
            if match == '' or match == '+':
                coef_2 += 1
            elif match == '-':
                coef_2 -= 1
            else:
                coef_2 += float(match)
        if coef_2 != 0:
            coefficients[2] = coef_2
        
        # Remove x**2 terms to avoid double counting
        expr_no_x2 = re.sub(degree_2_pattern, '', expr_clean)
        
        # Extract x terms (degree 1)
        degree_1_pattern = r'([+-]?\d*\.?\d*)\*?' + self.variable + r'(?!\*)'
        matches = re.findall(degree_1_pattern, expr_no_x2)
        coef_1 = 0
        for match in matches:
            if match == '' or match == '+':
                coef_1 += 1
            elif match == '-':
                coef_1 -= 1
            else:
                coef_1 += float(match)
        if coef_1 != 0:
            coefficients[1] = coef_1
        
        # Remove all variable terms to extract constant
        expr_no_vars = re.sub(r'[+-]?\d*\.?\d*\*?' + self.variable + r'(\*\*\d+)?', '', expr_clean)
        
        # Parse remaining constant terms
        if expr_no_vars:
            # Handle consecutive +/- signs
            expr_no_vars = expr_no_vars.replace('+-', '-').replace('-+', '-').replace('--', '+')
            
            # Extract all numbers with their signs
            const_pattern = r'[+-]?\d+\.?\d*'
            matches = re.findall(const_pattern, expr_no_vars)
            coef_0 = 0
            for m in matches:
                if m and m not in ['+', '-']:
                    coef_0 += float(m)
            
            if coef_0 != 0:
                coefficients[0] = coef_0
        
        return coefficients
    
    def get_degree(self):
        """Return the degree of the polynomial"""
        if not self.coefficients:
            return 0
        return max(self.coefficients.keys())
    
    def solve(self):
        """
        Solve the polynomial equation
        Returns: list of solutions (real numbers or ComplexNumber objects)
        """
        degree = self.get_degree()
        
        if degree == 0:
            # Constant equation: c = 0
            c = self.coefficients.get(0, 0)
            if c == 0:
                return "All real numbers are solutions"
            else:
                return "No solution"
        
        elif degree == 1:
            # Linear equation: bx + c = 0
            return self._solve_degree_1()
        
        elif degree == 2:
            # Quadratic equation: ax^2 + bx + c = 0
            return self._solve_degree_2()
        
        else:
            raise ValueError(f"Cannot solve polynomial of degree {degree} (only degrees 0, 1, 2 supported)")
    
    def _solve_degree_1(self):
        """Solve linear equation: bx + c = 0"""
        b = self.coefficients.get(1, 0)
        c = self.coefficients.get(0, 0)
        
        if b == 0:
            if c == 0:
                return "All real numbers are solutions"
            else:
                return "No solution"
        else:
            x = -c / b
            return [x]
    
    def _solve_degree_2(self):
        """
        Solve quadratic equation: ax^2 + bx + c = 0
        Returns real or complex solutions
        """
        a = self.coefficients.get(2, 0)
        b = self.coefficients.get(1, 0)
        c = self.coefficients.get(0, 0)
        
        # Calculate discriminant
        delta = b * b - 4 * a * c
        
        if delta > 0:
            # Two distinct real solutions
            sqrt_delta = delta ** 0.5
            x1 = (-b - sqrt_delta) / (2 * a)
            x2 = (-b + sqrt_delta) / (2 * a)
            return [x1, x2]
        
        elif delta == 0:
            # One real solution (repeated root)
            x = -b / (2 * a)
            return [x]
        
        else:
            # Two complex solutions
            sqrt_neg_delta = (-delta) ** 0.5
            real_part = -b / (2 * a)
            imag_part = sqrt_neg_delta / (2 * a)
            
            x1 = ComplexNumber(real_part, -imag_part)
            x2 = ComplexNumber(real_part, imag_part)
            return [x1, x2]
    
    def display_solution(self):
        """Display the solution with clear formatting"""
        degree = self.get_degree()
        
        print(f"\nPolynomial degree: {degree}")
        print(f"Coefficients: {self.coefficients}")
        
        if degree > 2:
            print("Error: Can only solve polynomials of degree ≤ 2")
            return
        
        solutions = self.solve()
        
        if isinstance(solutions, str):
            print(f"Solution: {solutions}")
        elif len(solutions) == 1:
            print(f"Solution: {self.variable} = {solutions[0]}")
        else:
            print("Solutions:")
            for i, sol in enumerate(solutions, 1):
                print(f"  {self.variable}{i} = {sol}")


def solve_polynomial_equation(expression, variable='x'):
    """
    Convenience function to solve a polynomial equation
    """
    solver = PolynomialEquationSolver(expression, variable)
    return solver.solve()
