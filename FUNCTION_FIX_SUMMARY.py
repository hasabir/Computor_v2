"""
FUNCTION HANDLING WITH PREDEFINED VARIABLES - SUMMARY
======================================================

PROBLEM:
--------
When defining a function like f(x) = x + a, if 'a' was a predefined variable,
it was not being replaced with its value during function definition.

SOLUTION:
---------
Modified the Function class to accept predefined variables and substitute them
(except the function parameter) at the time of function definition.

EXAMPLES OF WHAT NOW WORKS:
----------------------------

1. SIMPLE SUBSTITUTION:
   a = 5
   f(x) = x + a
   → f(x) = x + 5.0
   f(3) = 8.0 ✓

2. MULTIPLE VARIABLES:
   a = 5, b = 2, c = 3
   g(x) = a*x + b*c
   → g(x) = 5.0*x + 6.0
   g(2) = 16.0 ✓

3. COMPLEX NUMBERS:
   z = 2 + 3i
   f(x) = x * z
   → f(x) = x * (2.0 + 3.0i)
   f(2) = 4.0 + 6.0i ✓

4. VALUE AT DEFINITION TIME:
   m = 10
   p(x) = x * m
   → p(x) = 10.0*x
   m = 5  (changed later)
   p(2) = 20.0  (still uses m=10 from definition) ✓

5. PARAMETER SHADOWS VARIABLE:
   x = 100
   q(x) = x + 1
   → q(x) = x + 1  (parameter 'x' not replaced)
   q(5) = 6 ✓

6. FUNCTION REDEFINITION:
   constant = 7
   k(x) = x + constant
   → k(x) = x + 7.0
   
   constant = 20
   k(x) = x + constant  (redefined)
   → k(x) = x + 20.0  (uses new value) ✓

FILES MODIFIED:
---------------
1. calculator_parser.py:
   - Pass self.variables to Function() constructor
   
2. functions.py:
   - Added predefined_vars parameter to __init__
   - Modified _simplify_expression to:
     * Handle different variable types (numbers, complex, matrices)
     * Substitute predefined variables before simplification
     * Skip the function parameter variable (shadowing)
     * Convert complex numbers to SymPy compatible format

KEY FEATURES:
-------------
✓ Variables are replaced at function DEFINITION time
✓ Function parameters are NOT replaced (proper shadowing)
✓ Works with regular numbers, complex numbers, and matrices
✓ Changing a variable after function definition doesn't affect the function
✓ Functions can be redefined with new variable values

TESTS:
------
- test_function_vars.py: Complete test suite for all scenarios
- test_function_types.py: Tests with different variable types
- All tests pass successfully ✓
"""

if __name__ == "__main__":
    print(__doc__)
