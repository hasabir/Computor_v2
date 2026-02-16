#!/usr/bin/env python3
"""
Test function handling with different types of predefined variables
(complex numbers, matrices, etc.)
"""

from calculator_parser import CalculatorParser

def test_function_with_different_types():
    calc = CalculatorParser()
    
    print("="*70)
    print("TESTING FUNCTIONS WITH DIFFERENT VARIABLE TYPES")
    print("="*70)
    
    # Test 1: Complex number in function
    print("\n1. COMPLEX NUMBER VARIABLE")
    print("-"*70)
    calc.parse("z = 2 + 3i")
    print("z = 2 + 3i")
    result = calc.parse("f(x) = x * z")
    print(f"f(x) = x * z")
    print(f"Result: f(x) = {result}")
    
    # Since complex numbers can't be simplified to a simple form, 
    # let's test evaluation
    eval_result = calc.parse("f(2) =?")
    print(f"f(2) =? → {eval_result}")
    print(f"Expected: 2 * (2 + 3i) = 4 + 6i")
    
    # Test 2: Regular number operations
    print("\n2. MULTIPLE PREDEFINED VARIABLES")
    print("-"*70)
    calc.parse("p = 10")
    calc.parse("q = 5")
    print("p = 10, q = 5")
    result = calc.parse("g(t) = p * t + q")
    print(f"g(t) = p * t + q")
    print(f"Result: g(t) = {result}")
    
    eval_result = calc.parse("g(3) =?")
    print(f"g(3) =? → {eval_result}")
    print(f"Expected: 10 * 3 + 5 = 35")
    
    # Test 3: Function with no predefined variables
    print("\n3. FUNCTION WITH NO PREDEFINED VARIABLES")
    print("-"*70)
    result = calc.parse("h(x) = x^2 + 2*x + 1")
    print(f"h(x) = x^2 + 2*x + 1")
    print(f"Result: h(x) = {result}")
    
    eval_result = calc.parse("h(3) =?")
    print(f"h(3) =? → {eval_result}")
    print(f"Expected: 9 + 6 + 1 = 16")
    
    # Test 4: Redefinition with different variable values
    print("\n4. FUNCTION REDEFINITION")
    print("-"*70)
    calc.parse("constant = 7")
    print("constant = 7")
    result1 = calc.parse("k(x) = x + constant")
    print(f"k(x) = x + constant")
    print(f"Result: k(x) = {result1}")
    
    eval_result1 = calc.parse("k(5) =?")
    print(f"k(5) =? → {eval_result1}")
    
    calc.parse("constant = 20")
    print("\nconstant = 20 (changed)")
    result2 = calc.parse("k(x) = x + constant")
    print(f"k(x) = x + constant (redefined)")
    print(f"Result: k(x) = {result2}")
    
    eval_result2 = calc.parse("k(5) =?")
    print(f"k(5) =? → {eval_result2}")
    print("Note: Function was redefined, so it now uses constant = 20")
    
    print("\n" + "="*70)
    print("✓ ALL TESTS WITH DIFFERENT TYPES COMPLETED!")
    print("="*70)

if __name__ == "__main__":
    test_function_with_different_types()
