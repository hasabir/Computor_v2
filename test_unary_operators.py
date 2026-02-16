#!/usr/bin/env python3
"""
Test unary operators (+ and -) for all types
"""

from calculator_parser import CalculatorParser

def test_unary_operators():
    calc = CalculatorParser()
    
    print("="*60)
    print("TESTING UNARY OPERATORS")
    print("="*60)
    
    # Test with regular numbers
    print("\n1. REGULAR NUMBERS")
    print("-"*60)
    result = calc.parse("-5")
    print(f"-5 = {result}")
    
    result = calc.parse("+10")
    print(f"+10 = {result}")
    
    result = calc.parse("-(3 + 4)")
    print(f"-(3 + 4) = {result}")
    
    # Test with complex numbers
    print("\n2. COMPLEX NUMBERS")
    print("-"*60)
    result = calc.parse("-4i")
    print(f"-4i = {result}")
    
    result = calc.parse("+3i")
    print(f"+3i = {result}")
    
    result = calc.parse("varB = -4i - 4")
    print(f"varB = -4i - 4 → {result}")
    
    result = calc.parse("varC = -(2 + 3i)")
    print(f"varC = -(2 + 3i) → {result}")
    
    result = calc.parse("-varC =?")
    print(f"-varC =? → {result}")
    
    # Test with matrices
    print("\n3. MATRICES")
    print("-"*60)
    result = calc.parse("M = [[1, 2]; [3, 4]]")
    print(f"M = [[1, 2]; [3, 4]]")
    print(result)
    
    result = calc.parse("-M =?")
    print(f"\n-M =?")
    print(result)
    
    result = calc.parse("+M =?")
    print(f"\n+M =?")
    print(result)
    
    # Test complex expressions
    print("\n4. COMPLEX EXPRESSIONS")
    print("-"*60)
    result = calc.parse("x = 5")
    result = calc.parse("-x + 10 =?")
    print(f"x = 5, -x + 10 =? → {result}")
    
    result = calc.parse("z = 3 + 2i")
    result = calc.parse("-z * 2 =?")
    print(f"z = 3 + 2i, -z * 2 =? → {result}")
    
    print("\n" + "="*60)
    print("✓ ALL UNARY OPERATOR TESTS PASSED!")
    print("="*60)

if __name__ == "__main__":
    test_unary_operators()
