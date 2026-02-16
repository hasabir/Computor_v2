#!/usr/bin/env python3
"""
Test function handling with predefined variables
Verify that predefined variables are replaced when defining functions
"""

from calculator_parser import CalculatorParser

def test_function_with_predefined_vars():
    calc = CalculatorParser()
    
    print("="*70)
    print("TESTING FUNCTION DEFINITION WITH PREDEFINED VARIABLES")
    print("="*70)
    
    # Test 1: Simple variable substitution
    print("\n1. SIMPLE VARIABLE SUBSTITUTION")
    print("-"*70)
    calc.parse("a = 5")
    print("a = 5")
    result = calc.parse("f(x) = x + a")
    print(f"f(x) = x + a")
    print(f"Result: f(x) = {result}")
    print(f"Expected: f(x) = x + 5")
    
    eval_result = calc.parse("f(3) =?")
    print(f"f(3) =? → {eval_result}")
    print(f"Expected: 8")
    
    # Test 2: Multiple variables
    print("\n2. MULTIPLE VARIABLES")
    print("-"*70)
    calc.parse("b = 2")
    calc.parse("c = 3")
    print("b = 2, c = 3")
    result = calc.parse("g(x) = a*x + b*c")
    print(f"g(x) = a*x + b*c")
    print(f"Result: g(x) = {result}")
    print(f"Expected: g(x) = 5*x + 6")
    
    eval_result = calc.parse("g(2) =?")
    print(f"g(2) =? → {eval_result}")
    print(f"Expected: 16")
    
    # Test 3: Complex expression with predefined var
    print("\n3. COMPLEX EXPRESSION")
    print("-"*70)
    calc.parse("k = 4")
    print("k = 4")
    result = calc.parse("h(t) = t^2 + k*t - 1")
    print(f"h(t) = t^2 + k*t - 1")
    print(f"Result: h(t) = {result}")
    print(f"Expected: h(t) = t^2 + 4*t - 1")
    
    eval_result = calc.parse("h(2) =?")
    print(f"h(2) =? → {eval_result}")
    print(f"Expected: 4 + 8 - 1 = 11")
    
    # Test 4: Variable changed after function definition
    print("\n4. VARIABLE CHANGED AFTER FUNCTION DEFINITION")
    print("-"*70)
    print("Note: Function should use value at definition time, not current value")
    calc.parse("m = 10")
    print("m = 10")
    result = calc.parse("p(x) = x * m")
    print(f"p(x) = x * m")
    print(f"Result: p(x) = {result}")
    
    eval_result1 = calc.parse("p(2) =?")
    print(f"p(2) =? → {eval_result1} (should be 20)")
    
    calc.parse("m = 5")
    print("\nm = 5 (changed)")
    eval_result2 = calc.parse("p(2) =?")
    print(f"p(2) =? → {eval_result2} (should still be 20)")
    
    # Test 5: Function parameter shadows variable
    print("\n5. FUNCTION PARAMETER SHADOWS VARIABLE")
    print("-"*70)
    calc.parse("x = 100")
    print("x = 100")
    result = calc.parse("q(x) = x + 1")
    print(f"q(x) = x + 1")
    print(f"Result: q(x) = {result}")
    print(f"Expected: x + 1 (parameter 'x' should NOT be replaced)")
    
    eval_result = calc.parse("q(5) =?")
    print(f"q(5) =? → {eval_result}")
    print(f"Expected: 6")
    
    # Test 6: Mixed parameter and predefined variable
    print("\n6. MIXED PARAMETER AND PREDEFINED VARIABLE")
    print("-"*70)
    calc.parse("n = 7")
    print("n = 7")
    result = calc.parse("r(x) = x^2 + n")
    print(f"r(x) = x^2 + n")
    print(f"Result: r(x) = {result}")
    print(f"Expected: x^2 + 7")
    
    eval_result = calc.parse("r(3) =?")
    print(f"r(3) =? → {eval_result}")
    print(f"Expected: 9 + 7 = 16")
    
    print("\n" + "="*70)
    print("✓ ALL FUNCTION VARIABLE SUBSTITUTION TESTS COMPLETED!")
    print("="*70)

if __name__ == "__main__":
    test_function_with_predefined_vars()
