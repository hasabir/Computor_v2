from fractions import Fraction
from polynomialSolver import PolynomialSolver

class AdvancedPolynomialSolver(PolynomialSolver):
    def __init__(self, equation):
        self.equation = equation.strip()
        self.stock = {}
        self.variable = self._parse_equation()
        
        stock = self._get_reduced_form(equation.split("=")[0], 'left')
        self.parsed_equation = self._get_reduced_form(equation.split("=")[1], 'right', stock)
        


    def _parse_equation(self):
        if self.equation == '':
            raise SyntaxError(("Invalid equation, empty equation"))

        variables = ''.join([c for c in set(self.equation) if c.isalpha()])
        if len(variables) > 1:
            raise SyntaxError(("Invalid equation, only one variable is allowed"))
        for var in self.equation:
            if var not in "*-+^ =." and var.isdigit() == False and var not in variables:
                raise SyntaxError(("Syntax error"))
        if self.equation.count('=') != 1:
            raise SyntaxError(("Invalid equation, only one equal sign is allowed"))
        if (not self.equation[0].isalnum() or self.equation[0] not in '+-') \
                and not self.equation[-1].isalnum():
            raise SyntaxError(("Invalid equation"))
        
        equation_str = "".join(self.equation.split(" "))
        for i in range(len(equation_str)):
            if equation_str[i]  == '^' and(equation_str[i + 1] == '' or equation_str[i + 1].isdigit() == False):
                raise SyntaxError("Incorrect format")
            if equation_str[i] == '/' and equation_str[i + 1] and (equation_str[i + 1] == '0' \
                or equation_str[i + 1].isdigit() == False):
                raise SyntaxError("Incorrect format")
            if equation_str[i] == '*' and equation_str[i + 1].isdigit() == False and equation_str[i + 1] != variables:
                raise SyntaxError("Incorrect format")
            if equation_str[i] in '+-' and equation_str[i + 1].isdigit() == False:
                raise SyntaxError("Incorrect format")


    @staticmethod
    def solve_degree_2(parsed_equation):
        a = float(parsed_equation['2'])
        b = float(parsed_equation.get('1', 0))
        c = float(parsed_equation.get('0', 0))
        delta = b ** 2 - 4 * a * c
        print(f"""calculating discriminant:
            delta = (b^2 + 4ac)
            delta = {b}^2 - 4 * {a} * {c}
            delta = {delta}""")
        if delta > 0:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(f"""
            Discriminant is strictly positive, the two solutions are:
                    x1 = (-b - delta ** 0.5) / (2 * a)
                    x1 = ({-b} - {delta} ** 0.5) / (2 * {a})
                    x1 = {x1}
                    
                    x2 = (-b + delta ** 0.5) / (2 * a)
                    x2 = ({-b} + {delta} ** 0.5) / (2 * {a})
                    x2 = {x2}""")
            try:
                x1_fraction = Fraction(x1).limit_denominator()
                x2_fraction = Fraction(x2).limit_denominator()
                print(f"""
            The irreducible fraction of x1 and x2 are:
                    x1 = {x1_fraction}
                    x2 = {x2_fraction}""")
            except Exception as e:
                raise Exception(e)
        elif delta == 0:
            x = -b / (2 * a)
            print(f"""
            Discriminant is equal to zero, the solution is:
                    x = -b / (2 * a)
                    x = {-b} / (2 * {a})
                    x = {x}""")
            x_fraction = Fraction(x).limit_denominator()
            print(f"""
The irreducible fraction of x is:
                  x = {x_fraction}""")
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(f"""
            Discriminant is strictly negative, the two complex solutions are:
                    x1 = (-b - delta ** 0.5) / (2 * a)
                    x1 = ({-b} - {delta} ** 0.5) / (2 * {a})
                    x1 = {x1}
                    
                    x2 = (-b + delta ** 0.5) / (2 * a)
                    x2 = ({-b} + {delta} ** 0.5) / (2 * {a})
                    x2 = {x2}""")




    @staticmethod
    def solve_degree_1(parsed_equation):
        b = float(parsed_equation.get('1', 0))
        c = float(parsed_equation.get('0', 0))
        if b == 0:
            if c == 0:
                print("All real numbers are solutions")
            else:
                print("No solution")
        else:
            x = -c / b
            print(f"""The solution is:
                  x = -c / b
                  x = {-c} / {b}
                  x = {x}""")
            x_fraction = Fraction(x).limit_denominator()
            print(f"""
The irreducible fraction of x is:
                  x = {x_fraction}""")