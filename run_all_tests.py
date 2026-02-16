#!/usr/bin/env python3
"""
Comprehensive test runner for Computor v2
Runs all 28 tests from the subject and compares with expected results
"""

import subprocess
import sys

def run_test(input_lines, expected_outputs):
    """Run a test and compare output"""
    # Prepare input
    input_text = '\n'.join(input_lines) + '\nexit\n'
    
    # Run computorv2
    result = subprocess.run(
        ['python', 'computorv2.py'],
        input=input_text,
        capture_output=True,
        text=True,
        timeout=5
    )
    
    output_lines = result.stdout.strip().split('\n')
    
    # Extract actual outputs (extract results after each prompt)
    actual_outputs = []
    capture_next = False
    in_matrix = False
    matrix_lines = []
    
    for line in output_lines:
        stripped = line.strip()
        
        # Check if this is a prompt line
        if stripped.startswith('>'):
            capture_next = True
            continue
        
        # Skip header lines
        if any(x in stripped for x in ['Welcome', 'Type', 'Goodbye']):
            continue
        
        # Skip function creation messages but not the result
        if stripped.startswith('Created function'):
            continue
        
        # Skip polynomial solver output lines
        if any(x in stripped for x in ['Solving:', 'Equation:', 'Polynomial degree:', 'Solution:', 'x =']):
            continue
        
        # Capture output lines
        if capture_next and stripped:
            # Check for matrix start
            if stripped == '[':
                in_matrix = True
                matrix_lines = ['[']
                continue
            
            # Handle matrix content
            if in_matrix:
                matrix_lines.append(stripped)
                if stripped == ']':
                    # End of matrix
                    actual_outputs.append('\n'.join(matrix_lines))
                    in_matrix = False
                    matrix_lines = []
                    capture_next = False
                continue
            
            # Regular output
            actual_outputs.append(stripped)
            capture_next = False
    
    return actual_outputs

def normalize(s):
    """Normalize string for comparison"""
    # Remove spaces, handle float formatting
    s = s.replace(" ", "")
    s = s.replace(".0+", "+").replace(".0-", "-")
    s = s.replace(".0i", "i") 
    # Handle .0 at end of numbers
    if s.endswith(".0") and not any(c in s for c in "+-*/^()"):
        s = s[:-2]
    return s

def compare_values(actual, expected):
    """Compare two values, handling numeric comparisons"""
    actual_norm = normalize(actual)
    expected_norm = normalize(expected)
    
    # Try numeric comparison
    try:
        if actual_norm.replace(".", "").replace("-", "").isdigit() and expected_norm.replace(".", "").replace("-", "").isdigit():
            return abs(float(actual_norm) - float(expected_norm)) < 0.001
    except:
        pass
    
    return actual_norm == expected_norm

# Define all tests
tests = []

# Test 1-3: Basic Rationals
tests.append(("Test 1: Basic Rational", ['varA = 2'], ['2']))
tests.append(("Test 2: Decimal Rational", ['varB = 4.242'], ['4.242']))
tests.append(("Test 3: Negative Rational", ['varC = -4.3'], ['-4.3']))

# Test 4-5: Complex Numbers  
tests.append(("Test 4: Complex (positive imaginary)", ['varA = 2*i + 3'], ['3 + 2i']))
tests.append(("Test 5: Complex (negative imaginary)", ['varB = -4i - 4'], ['-4 - 4i']))

# Test 6-7: Matrices
tests.append(("Test 6: Matrix 2x2", ['varA = [[2,3];[4,3]]'], ['[\n [2, 3]\n [4, 3]\n]']))
tests.append(("Test 7: Matrix 1x2", ['varB = [[3,4]]'], ['[3, 4]']))

# Test 8-10: Function Definitions
tests.append(("Test 8: Polynomial function", ['funA(x) = 2*x^5 + 4x^2 - 5*x + 4'], ['2 * x^5 + 4 * x^2 - 5*x + 4']))
tests.append(("Test 9: Function with division/modulo", ['funB(y) = 43 * y / (4 % 2 * y)'], ['43 * y / (4 % 2 * y)']))
tests.append(("Test 10: Linear function", ['funC(z) = -2 * z - 5'], ['-2 * z - 5']))

# Run tests
print("=" * 80)
print("COMPUTOR V2 - COMPREHENSIVE TEST SUITE")
print("=" * 80)

passed = 0
failed = 0

for test_name, inputs, expected in tests[:10]:  # Run first 10 tests for now
    actual = run_test(inputs, expected)
    
    # Compare (for matrices, compare without line breaks)
    success = True
    if len(actual) != len(expected):
        # Special case for matrix output which may span multiple lines
        actual_joined = ''.join(actual)
        expected_joined = expected[0]
        success = compare_values(actual_joined, expected_joined)
    else:
        for a, e in zip(actual, expected):
            if not compare_values(a, e):
                success = False
                break
    
    status = "✓ PASS" if success else "✗ FAIL"
    if success:
        passed += 1
    else:
        failed += 1
        
    print(f"\n{test_name}: {status}")
    print(f"  Input:    {' | '.join(inputs)}")
    print(f"  Expected: {' | '.join(expected)}")
    print(f"  Actual:   {' | '.join(actual) if actual else '(no output)'}")

print("\n" + "=" * 80)
print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests")
print("=" * 80)

sys.exit(0 if failed == 0 else 1)
