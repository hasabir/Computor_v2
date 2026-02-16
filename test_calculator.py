#!/usr/bin/env python3

from calculator_parser import CalculatorParser

def test_calculator():
    calc = CalculatorParser()
    
    print("=== Testing Basic Operations ===")
    print(f"2 + 3 = {calc.parse('2 + 3')}")
    print(f"10 - 4 = {calc.parse('10 - 4')}")
    print(f"5 * 6 = {calc.parse('5 * 6')}")
    print(f"15 / 3 = {calc.parse('15 / 3')}")
    print(f"2 ^ 3 = {calc.parse('2 ^ 3')}")
    print(f"10 % 3 = {calc.parse('10 % 3')}")
    
    print("\n=== Testing Unary Operators ===")
    print(f"-5 = {calc.parse('-5')}")
    print(f"+5 = {calc.parse('+5')}")
    print(f"-(2+3) = {calc.parse('-(2+3)')}")
    
    print("\n=== Testing Complex Numbers ===")
    print(f"i = {calc.parse('i')}")
    print(f"2i = {calc.parse('2i')}")
    print(f"3 + 4i = {calc.parse('3 + 4i')}")
    print(f"(2+3i) + (1+2i) = {calc.parse('(2+3i) + (1+2i)')}")
    print(f"(2+3i) * (1+2i) = {calc.parse('(2+3i) * (1+2i)')}")
    
    print("\n=== Testing Variables ===")
    print(f"x = 5: {calc.parse('x = 5')}")
    print(f"x =?: {calc.parse('x =?')}")
    print(f"y = 2x: {calc.parse('y = 2x')}")
    print(f"y =?: {calc.parse('y =?')}")
    
    print("\n=== Testing Matrices ===")
    print(f"A = [[1,2];[3,4]]: {calc.parse('A = [[1,2];[3,4]]')}")
    print(f"A =?: {calc.parse('A =?')}")
    print(f"B = [[2,0];[1,2]]: {calc.parse('B = [[2,0];[1,2]]')}")
    print(f"A + B = {calc.parse('A + B =?')}")
    print(f"A * B = {calc.parse('A * B =?')}")
    print(f"A ** B = {calc.parse('A ** B =?')}")
    
    print("\n=== Testing Functions ===")
    print(f"funA(x) = 2*x + 1: {calc.parse('funA(x) = 2*x + 1')}")
    print(f"funA(5) =?: {calc.parse('funA(5) =?')}")
    print(f"funB(t) = t^2 - 3*t + 2: {calc.parse('funB(t) = t^2 - 3*t + 2')}")
    print(f"funB(4) =?: {calc.parse('funB(4) =?')}")

if __name__ == "__main__":
    test_calculator()