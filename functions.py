from sympy import sympify, simplify, Symbol
import re

class Function:
    def __init__(self, name, variable, expression):
        self.name = name
        self.variable = variable  # The parameter variable (e.g., 'x')
        
        self.expression = self._simplify_expression(expression=expression) # The function body as a string
        print(f"Created function: {self.name}({self.variable}) = {self.expression}")
    
    def __str__(self):
        return f"{self.name}({self.variable}) = {self.expression}"
    
    def _add_implicit_multiplication(self, expr_str):
        """Convert implicit multiplication to explicit (e.g., 3x -> 3*x, 2(x+1) -> 2*(x+1))"""
        # Insert * between number and variable: 3x -> 3*x
        expr_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr_str)
        
        # Insert * between ) and (: )(  -> )*(
        expr_str = re.sub(r'\)\s*\(', r')*(', expr_str)
        
        # Insert * between number and (: 2( -> 2*(
        expr_str = re.sub(r'(\d)\s*\(', r'\1*(', expr_str)
        
        # Insert * between ) and variable: )x -> )*x
        expr_str = re.sub(r'\)([a-zA-Z])', r')*\1', expr_str)
        
        # Insert * between variable and (: x( -> x*(
        expr_str = re.sub(r'([a-zA-Z])\s*\(', r'\1*(', expr_str)
        
        return expr_str
    
    def _simplify_expression(self, expression):
        """Simplify mathematical expression using SymPy"""
        
        try:
            # Replace ^ with ** for Python exponentiation
            expr_str = expression.replace('^', '**')
            print(f"After replacing ^: {expr_str}")
            
            # Add explicit multiplication operators
            expr_str = self._add_implicit_multiplication(expr_str)
            print(f"After adding implicit multiplication: {expr_str}")
            
            # Create a symbol for the variable
            var_symbol = Symbol(self.variable)
            
            # Parse and simplify the expression
            sympy_expr = sympify(expr_str, locals={self.variable: var_symbol})
            print(f"Parsed expression for {self.name}: {sympy_expr}")
            
            simplified = simplify(sympy_expr)
            print(f"Simplified expression for {self.name}: {simplified}")
            
            # Convert back to string and replace ** with ^
            result = str(simplified).replace('**', '^')
            
            print(f"Final simplified expression: {result}")
            
            return result.replace(' ', '')
        except Exception as e:
            # If simplification fails, just remove spaces
            print(f"Error simplifying expression for {self.name}: {e}")
            return expression.replace(' ', '')