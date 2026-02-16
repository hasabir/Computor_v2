#!/usr/bin/env python3
"""
Comprehensive test for all missing features:
1. Matrix display in clear format
2. Polynomial equation solving (degree <= 2)
"""

from calculator_parser import CalculatorParser

def test_matrix_display():
    """Test improved matrix display format"""
    print("="*60)
    print("TEST 1: MATRIX DISPLAY FORMAT")
    print("="*60)
    
    calc = CalculatorParser()
    
    print("\n1.1 Single row matrix:")
    result = calc.parse('A = [[1, 2, 3]]')
    print(f"A = [[1, 2, 3]]")
    print(f"Result:\n{result}")
    
    print("\n1.2 Multi-row matrix:")
    result = calc.parse('B = [[1, 2]; [3, 4]]')
    print(f"B = [[1, 2]; [3, 4]]")
    print(f"Result:\n{result}")
    
    print("\n1.3 3x3 matrix:")
    result = calc.parse('C = [[1, 2, 3]; [4, 5, 6]; [7, 8, 9]]')
    print(f"C = [[1, 2, 3]; [4, 5, 6]; [7, 8, 9]]")
    print(f"Result:\n{result}")
    
    print("\n1.4 Matrix lookup:")
    result = calc.parse('B =?')
    print(f"B =?")
    print(f"Result:\n{result}")

def test_polynomial_solving():
    """Test polynomial equation solving"""
    print("\n" + "="*60)
    print("TEST 2: POLYNOMIAL EQUATION SOLVING")
    print("="*60)
    
    calc = CalculatorParser()
    
    print("\n2.1 Linear equation: f(x) = 2x - 4, solve f(x) = 0?")
    calc.parse('f(x) = 2*x - 4')
    result = calc.parse('f(x) = 0?')
    print(f"Expected: x = 2.0")
    
    print("\n2.2 Quadratic with two real solutions: g(x) = x^2 - 5x + 6, solve g(x) = 0?")
    calc.parse('g(x) = x^2 - 5*x + 6')
    result = calc.parse('g(x) = 0?')
    print(f"Expected: x1 = 2.0, x2 = 3.0")
    
    print("\n2.3 Quadratic with one solution: h(x) = x^2 - 4x + 4, solve h(x) = 0?")
    calc.parse('h(x) = x^2 - 4*x + 4')
    result = calc.parse('h(x) = 0?')
    print(f"Expected: x = 2.0 (double root)")
    
    print("\n2.4 Quadratic with complex solutions: k(x) = x^2 + x + 1, solve k(x) = 0?")
    calc.parse('k(x) = x^2 + x + 1')
    result = calc.parse('k(x) = 0?')
    print(f"Expected: complex solutions")
    
    print("\n2.5 Quadratic from example: p(x) = x^2 + 3x + 2, solve p(x) = 0?")
    calc.parse('p(x) = x^2 + 3*x + 2')
    result = calc.parse('p(x) = 0?')
    print(f"Expected: x1 = -2.0, x2 = -1.0")
    
    print("\n2.6 Solving with target value: m(x) = x^2, solve m(x) = 9?")
    calc.parse('m(x) = x^2')
    result = calc.parse('m(x) = 9?')
    print(f"Expected: x1 = -3.0, x2 = 3.0")

def test_edge_cases():
    """Test edge cases and special scenarios"""
    print("\n" + "="*60)
    print("TEST 3: EDGE CASES")
    print("="*60)
    
    calc = CalculatorParser()
    
    print("\n3.1 Constant equation (no solution): f(x) = 5, solve f(x) = 0?")
    calc.parse('f(x) = 5')
    result = calc.parse('f(x) = 0?')
    
    print("\n3.2 Identity equation: g(x) = 0, solve g(x) = 0?")
    calc.parse('g(x) = 0')
    result = calc.parse('g(x) = 0?')
    
    print("\n3.3 Complex function evaluation combined with solving:")
    calc.parse('h(t) = t^2 - 2*t + 1')
    print("  h(3) =?")
    eval_result = calc.parse('h(3) =?')
    print(f"  Evaluation result: {eval_result}")
    print("  h(t) = 0?")
    solve_result = calc.parse('h(t) = 0?')

def main():
    print("\n" + "="*60)
    print("COMPUTOR V2 - COMPREHENSIVE FEATURE TEST")
    print("="*60)
    
    try:
        test_matrix_display()
        test_polynomial_solving()
        test_edge_cases()
        
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
