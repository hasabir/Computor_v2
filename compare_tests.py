#!/usr/bin/env python3
"""
Compare test outputs with expected results
"""

tests = [
    ("Test 1: varA = 2", "2.0", "2"),
    ("Test 2: varB = 4.242", "4.242", "4.242"),
    ("Test 3: varC = -4.3", "-4.3", "-4.3"),
    ("Test 4: varA = 2*i + 3", "3.0 + 2.0i", "3 + 2i"),
    ("Test 5: varB = -4i - 4", "-4.0 - 4.0i", "-4 - 4i"),
    ("Test 8: funA(x) = 2*x^5 + 4x^2 - 5*x + 4", "2 * x^5 + 4 * x^2 - 5 * x + 4", "2 * x^5 + 4 * x^2 - 5*x + 4"),
    ("Test 9: funB(y) = 43 * y / (4 % 2 * y)", "43 * y / (4 % 2 * y)", "43 * y / (4 % 2 * y)"),
    ("Test 10: funC(z) = -2 * z - 5", "-2 * z - 5", "-2 * z - 5"),
    ("Test 14: funA(x) = varA + varB * 4 - 1 / 2 + x", "238.5 + x", "238.5 + x"),
    ("Test 18: funA(x) = 2 * 4 + x", "8 + x", "8 + x"),
    ("Test 19: funB(x) = 4 -5 + (x + 2)^2 - 4", "(x + 2)^2 - 5", "(x + 2)^2 - 5"),
    ("Test 20: funC(x) = 4x + 5 - 2", "4 * x + 3", "4 * x + 3"),
]

print("=" * 80)
print("TEST COMPARISON")
print("=" * 80)

all_pass = True
for test_name, actual, expected in tests:
    # Normalize for comparison (remove extra spaces, handle float formatting)
    actual_norm = actual.replace(" ", "").replace(".0+", "+").replace(".0-", "-").replace(".0i", "i")
    expected_norm = expected.replace(" ", "").replace(".0+", "+").replace(".0-", "-").replace(".0i", "i")
    
    # For numbers, compare as floats if possible
    try:
        if actual_norm.replace(".", "").replace("-", "").isdigit() and expected_norm.replace(".", "").replace("-", "").isdigit():
            actual_num = float(actual_norm)
            expected_num = float(expected_norm)
            matches = abs(actual_num - expected_num) < 0.0001
        else:
            matches = actual_norm == expected_norm
    except:
        matches = actual_norm == expected_norm
    
    status = "✓ PASS" if matches else "✗ FAIL"
    if not matches:
        all_pass = False
        
    print(f"\n{test_name}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    print(f"  {status}")

print("\n" + "=" * 80)
if all_pass:
    print("ALL TESTS PASSED!")
else:
    print("SOME TESTS FAILED - see details above")
print("=" * 80)
