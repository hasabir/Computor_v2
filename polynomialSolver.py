class PolynomialSolver:
    def __init__(self, equation):
        self.equation = equation
        stock = self._get_reduced_form(equation.split("=")[0], 'left')
        self.parsed_equation = self._get_reduced_form(equation.split("=")[1], 'right', stock)


    def _get_reduced_form(self, equation, equation_parts, stock={}):
        equation = equation.split(" ")
        for i in range(len(equation)):
            if equation[i] == '*':
                key = equation[i + 1].split("^")[1]
                value = f"{equation[i - 2]}{equation[i - 1]}"
                if equation_parts == 'right':
                    stock[key] = str(float(stock.get(key, 0)) - float(value))
                    if float(stock[key]) == 0:
                        del stock[key]
                else:
                    if float(value) != 0:
                        stock[key] = value
        
        return stock
    
    def get_parsed_equation(self):
        return self.parsed_equation


    @staticmethod
    def solve_degree_2(parsed_equation):
        a = float(parsed_equation['2'])
        b = float(parsed_equation.get('1', 0))
        c = float(parsed_equation.get('0', 0))
    
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(f"Discriminant is strictly positive, the two solutions are:\n{x1}\n{x2}")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"Discriminant is equal to zero, the solution is:\n{x}")
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(f"Discriminant is strictly negative, the two complex solutions are:\n{x1}\n{x2}")


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
            print(f"The solution is:\n{x}")

