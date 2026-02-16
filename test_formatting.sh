#!/bin/bash

echo "=== Test 8: Function Definition (polynomial) ==="
echo "Input: funA(x) = 2*x^5 + 4x^2 - 5*x + 4"
echo "Expected: 2 * x^5 + 4 * x^2 - 5*x + 4"
echo -e "funA(x) = 2*x^5 + 4x^2 - 5*x + 4\nexit" | python computorv2.py 2>&1 | grep "^2" | head -1
echo ""

echo "=== Test 9: Function with division/modulo ==="
echo "Input: funB(y) = 43 * y / (4 % 2 * y)"
echo "Expected: 43 * y / (4 % 2 * y)"
echo -e "funB(y) = 43 * y / (4 % 2 * y)\nexit" | python computorv2.py 2>&1 | grep "^43" | head -1
echo ""

echo "=== Test 14: Function with variable refs ==="
echo "Input: funA(x) = varA + varB * 4 - 1 / 2 + x"
echo "Expected: 238.5 + x"
echo -e "varA = 27\nvarB = 53\nfunA(x) = varA + varB * 4 - 1 / 2 + x\nexit" | python computorv2.py 2>&1 | grep -E "^(x\+|238)" | head -1
echo ""

echo "=== Test 18: Simple function ==="
echo "Input: funA(x) = 2 * 4 + x"
echo "Expected: 8 + x"
echo -e "funA(x) = 2 * 4 + x\nexit" | python computorv2.py 2>&1 | grep -E "^(x\+|8)" | head -1
echo ""

echo "=== Test 19: Quadratic function ==="
echo "Input: funB(x) = 4 -5 + (x + 2)^2 - 4"
echo "Expected: (x + 2)^2 - 5"
echo -e "funB(x) = 4 -5 + (x + 2)^2 - 4\nexit" | python computorv2.py 2>&1 | grep -E "^\(" | head -1
echo ""

echo "=== Test 20: Linear with simplification ==="
echo "Input: funC(x) = 4x + 5 - 2"
echo "Expected: 4 * x + 3"
echo -e "funC(x) = 4x + 5 - 2\nexit" | python computorv2.py 2>&1 | grep "^4" | head -1
