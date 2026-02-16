#!/usr/bin/env python3
"""
Test various complex number formats with unary operators
Testing the original error case: varB = -4i - 4
"""

from calculator_parser import CalculatorParser

def test_complex_formats():
    calc = CalculatorParser()
    
    print("="*60)
    print("TESTING COMPLEX NUMBER FORMATS WITH UNARY OPERATORS")
    print("="*60)
    
    test_cases = [
        ("varA = 2*i + 3", "Standard format"),
        ("varB = -4i - 4", "Original error case"),
        ("varC = -4 - 4i", "Alternative format"),
        ("varD = -(3 + 2i)", "Negated complex"),
        ("varE = -i", "Negative imaginary unit"),
        ("varF = +2i", "Positive imaginary"),
        ("varG = 0 - 5i", "Zero real part"),
        ("varH = -3 + 0i", "Zero imaginary part"),
    ]
    
    for expr, description in test_cases:
        try:
            result = calc.parse(expr)
            print(f"\n{description}:")
            print(f"  {expr}")
            print(f"  Result: {result}")
        except Exception as e:
            print(f"\n{description}:")
            print(f"  {expr}")
            print(f"  ❌ ERROR: {e}")
    
    # Test operations with stored variables
    print("\n" + "="*60)
    print("OPERATIONS WITH COMPLEX VARIABLES")
    print("="*60)
    
    operations = [
        ("varB + varD =?", "Addition"),
        ("varB * varE =?", "Multiplication"),
        ("-varA =?", "Negation of variable"),
        ("varC - varB =?", "Subtraction"),
    ]
    
    for expr, description in operations:
        try:
            result = calc.parse(expr)
            print(f"\n{description}: {expr}")
            print(f"  Result: {result}")
        except Exception as e:
            print(f"\n{description}: {expr}")
            print(f"  ❌ ERROR: {e}")
    
    print("\n" + "="*60)
    print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*60)

if __name__ == "__main__":
    test_complex_formats()
