from sympy import sympify, simplify, Symbol
import re

class Function:
    def __init__(self, name, variable, expression, predefined_vars=None):
        """
        Initialize a function
        Args:
            name: function name
            variable: parameter variable (e.g., 'x')
            expression: function expression
            predefined_vars: dict of predefined variables to substitute
        """
        self.name = name
        self.variable = variable  # The parameter variable (e.g., 'x')
        self.predefined_vars = predefined_vars if predefined_vars is not None else {}
        
        # Substitute predefined variables before simplification
        self.expression = self._simplify_expression(expression=expression)
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
            
            # Add explicit multiplication operators
            expr_str = self._add_implicit_multiplication(expr_str)
            
            # Create a symbol for the function variable
            var_symbol = Symbol(self.variable)
            
            # Create symbols dict with the function variable
            symbols_dict = {self.variable: var_symbol}
            
            # Substitute predefined variables with their values
            # Build a substitution dict for SymPy
            subs_dict = {}
            for var_name, var_value in self.predefined_vars.items():
                # Skip the function parameter variable
                if var_name.lower() != self.variable.lower():
                    # Create a temporary symbol for this variable
                    temp_symbol = Symbol(var_name)
                    symbols_dict[var_name] = temp_symbol
                    # Store value for substitution after parsing
                    subs_dict[temp_symbol] = var_value
            
            # Parse the expression with all symbols
            sympy_expr = sympify(expr_str, locals=symbols_dict)
            
            # Substitute predefined variable values
            if subs_dict:
                sympy_expr = sympy_expr.subs(subs_dict)
            
            # Simplify the expression
            simplified = simplify(sympy_expr)
            
            # Convert back to string and replace ** with ^
            result = str(simplified).replace('**', '^')
            
            return result.replace(' ', '')
        except Exception as e:
            # If simplification fails, just remove spaces
            print(f"Error simplifying expression for {self.name}: {e}")
            return expression.replace(' ', '')