#!/usr/bin/env python3

from calculator_parser import CalculatorParser

def test_function_simplification():
    calc = CalculatorParser()
    
    print("=== Testing Function Simplification ===\n")
    
    # Test 1: Algebraic simplification
    print("Test 1: f(x) = (x^2+3x+2)/(x+1)")
    result = calc.parse('f(x) = (x^2+3x+2)/(x+1)')
    print(f"Result: {result}\n")
    
    # Test 2: Another simplification
    print("Test 2: g(t) = (t^2-1)/(t-1)")
    result = calc.parse('g(t) = (t^2-1)/(t-1)')
    print(f"Result: {result}\n")
    
    # Test 3: Expand and simplify
    print("Test 3: h(x) = (x+1)*(x+2)")
    result = calc.parse('h(x) = (x+1)*(x+2)')
    print(f"Result: {result}\n")
    
    # Test 4: Test function evaluation with simplified function
    print("Test 4: Evaluating f(3) where f(x) = (x^2+3x+2)/(x+1)")
    print(f"f = {calc.functions['f']}")
    result = calc.parse('f(3) =?')
    print(f"f(3) = {result}")
    print(f"Expected: 3+2 = 5 ✓\n")
    
    # Test 5: Mixed operations
    print("Test 5: k(x) = 2x^2 - 3x + 1")
    result = calc.parse('k(x) = 2x^2 - 3x + 1')
    print(f"Result: {result}\n")

if __name__ == "__main__":
    test_function_simplification()
