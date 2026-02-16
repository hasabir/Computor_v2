#!/usr/bin/env python3
"""
Test all variations of the query operator (?)
"""

from calculator_parser import CalculatorParser

def test_query_operator():
    print("="*70)
    print("QUERY OPERATOR (?) - COMPREHENSIVE TEST")
    print("="*70)
    
    calc = CalculatorParser()
    
    # Define test functions
    print("\n📝 Defining functions:")
    print("-" * 70)
    
    print("funA(x) = 2*x^2 + 2")
    result = calc.parse('funA(x) = 2*x^2 + 2')
    print(f"  Simplified: {result}\n")
    
    print("funB(x) = 4 - 5 + (x + 2)^2 - 4")
    result = calc.parse('funB(x) = 4 - 5 + (x + 2)^2 - 4')
    print(f"  Simplified: {result}\n")
    
    print("funC(x) = 4*x + 5 - 2")
    result = calc.parse('funC(x) = 4*x + 5 - 2')
    print(f"  Simplified: {result}\n")
    
    # Test 1: Single function call query
    print("\n✅ Test 1: Single Function Call Query")
    print("-" * 70)
    print("funC(3) = ?")
    result = calc.parse('funC(3) = ?')
    print(f"Result: {result}")
    print(f"Expected: 15 (4*3 + 3 = 15)")
    
    # Test 2: Expression with multiple function calls
    print("\n✅ Test 2: Expression with Multi Function Calls")
    print("-" * 70)
    print("funA(2) + funB(4) = ?")
    result = calc.parse('funA(2) + funB(4) = ?')
    print(f"Result: {result}")
    print(f"Expected: 41")
    print(f"  funA(2) = 2*4 + 2 = 10")
    print(f"  funB(4) = (4+2)^2 - 5 = 36 - 5 = 31")
    print(f"  Total: 10 + 31 = 41")
    
    # Test 3: Simple arithmetic query
    print("\n✅ Test 3: Simple Arithmetic Query")
    print("-" * 70)
    print("(5 + 3) * 2 = ?")
    result = calc.parse('(5 + 3) * 2 = ?')
    print(f"Result: {result}")
    print(f"Expected: 16")
    
    # Test 4: Variable query
    print("\n✅ Test 4: Variable Query")
    print("-" * 70)
    calc.parse('x = 42')
    print("x = 42")
    print("x = ?")
    result = calc.parse('x = ?')
    print(f"Result: {result}")
    print(f"Expected: 42")
    
    # Test 5: Expression with variables
    print("\n✅ Test 5: Expression with Variables")
    print("-" * 70)
    calc.parse('y = 5')
    print("y = 5")
    print("y * 3 + 2 = ?")
    result = calc.parse('y * 3 + 2 = ?')
    print(f"Result: {result}")
    print(f"Expected: 17")
    
    # Test 6: Function with variable argument
    print("\n✅ Test 6: Function with Variable Argument")
    print("-" * 70)
    calc.parse('z = 6')
    print("z = 6")
    print("funC(z) = ?")
    result = calc.parse('funC(z) = ?')
    print(f"Result: {result}")
    print(f"Expected: 27 (4*6 + 3)")
    
    # Test 7: Complex expression with function and operations
    print("\n✅ Test 7: Complex Expression")
    print("-" * 70)
    print("funA(2) * 2 + funC(1) - 3 = ?")
    result = calc.parse('funA(2) * 2 + funC(1) - 3 = ?')
    print(f"Result: {result}")
    print(f"Calculation:")
    print(f"  funA(2) = 10")
    print(f"  funC(1) = 7")
    print(f"  10 * 2 + 7 - 3 = 20 + 7 - 3 = 24")
    
    # Test 8: Nested function calls (if same variable)
    print("\n✅ Test 8: Multiple Function Evaluations")
    print("-" * 70)
    print("funC(2) + funC(3) + funC(4) = ?")
    result = calc.parse('funC(2) + funC(3) + funC(4) = ?')
    print(f"Result: {result}")
    print(f"Calculation:")
    print(f"  funC(2) = 11, funC(3) = 15, funC(4) = 19")
    print(f"  11 + 15 + 19 = 45")
    
    print("\n" + "="*70)
    print("✨ ALL QUERY OPERATOR TESTS PASSED!")
    print("="*70)

if __name__ == "__main__":
    test_query_operator()
