# All Tests from the Subject with Expected Results

Here are all the example tests provided in the Computor v2 subject:

---

## **Test 1: Basic Rational Number Assignment**

```
> varA = 2
```
**Expected Result:**
```
2
```
  

---

## **Test 2: Decimal Rational Number**

```
> varB = 4.242
```
**Expected Result:**
```
4.242
```
  

---

## **Test 3: Negative Rational Number**

```
> varC = -4.3
```
**Expected Result:**
```
-4.3
```
  

---

## **Test 4: Complex Number Assignment (positive imaginary)**

```
> varA = 2*i + 3
```
**Expected Result:**
```
3 + 2i
```
  

---

## **Test 5: Complex Number Assignment (negative imaginary)**

```
> varB = -4i - 4
```
**Expected Result:**
```
-4 - 4i
```
  

---

## **Test 6: Matrix Assignment (2x2)**

```
> varA = [[2,3];[4,3]]
```
**Expected Result:**
```
[ 2, 3 ]
[ 4, 3 ]
```
  

---

## **Test 7: Matrix Assignment (1x2)**

```
> varB = [[3,4]]
```
**Expected Result:**
```
[ 3, 4 ]
```
  

---

## **Test 8: Function Definition (polynomial)**

```
> funA(x) = 2*x^5 + 4x^2 - 5*x + 4
```
**Expected Result:**
```
2 * x^5 + 4 * x^2 - 5*x + 4
```
  

---

## **Test 9: Function Definition (with division and modulo)**

```
> funB(y) = 43 * y / (4 % 2 * y)
```
**Expected Result:**
```
43 * y / (4 % 2 * y)
```
  

---

## **Test 10: Function Definition (linear)**

```
> funC(z) = -2 * z - 5
```
**Expected Result:**
```
-2 * z - 5
```
  

---

## **Test 11: Variable Reassignment and Type Change**

```
> x = 2
2
> y = x
2
> y = 7
7
> y = 2 * i - 4
```
**Expected Result:**
```
-4 + 2i
```
     

---

## **Test 12: Complex Expression Assignment**

```
> varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)
```
**Expected Result:**
```
27
```
  

---

## **Test 13: Expression with Variable Reference**

```
> varB = 2 * varA - 5 %4
```
**Expected Result (assuming varA = 27):**
```
53
```
  

---

## **Test 14: Function with Variable References**

```
> funA(x) = varA + varB * 4 - 1 / 2 + x
```
**Expected Result (assuming varA = 27, varB = 53):**
```
238.5 + x
```
  

---

## **Test 15: Variable Computation**

```
> varC = 2 * varA - varB
```
**Expected Result (assuming varA = 27, varB = 53):**
```
1
```
  

---

## **Test 16: Function Evaluation with Variable**

```
> varD = funA(varC)
```
**Expected Result (assuming funA(x) = 238.5 + x, varC = 1):**
```
239.5
```
  

---

## **Test 17: Simple Query**

```
> a = 2 * 4 + 4
12
> a + 2 =?
```
**Expected Result:**
```
14
```
   

---

## **Test 18: Function Definition for Evaluation**

```
> funA(x) = 2 * 4 + x
```
**Expected Result:**
```
8 + x
```
  

---

## **Test 19: Function Definition (quadratic)**

```
> funB(x) = 4 -5 + (x + 2)^2 - 4
```
**Expected Result:**
```
(x + 2)^2 - 5
```
  

---

## **Test 20: Function Definition (linear with simplification)**

```
> funC(x) = 4x + 5 - 2
```
**Expected Result:**
```
4 * x + 3
```
  

---

## **Test 21: Function Evaluation Query**

```
> funA(2) + funB(4) =?
```
**Expected Result (assuming funA(x) = 8 + x, funB(x) = (x + 2)^2 - 5):**
```
41
```
  

---

## **Test 22: Simple Function Evaluation**

```
> funC(3) =?
```
**Expected Result (assuming funC(x) = 4 * x + 3):**
```
15
```
  

---

## **Test 23: Quadratic Equation Solving**

```
> funA(x) = x^2 + 2x + 1
x^2 + 2x + 1
> y = 0
0
> funA(x) = y?
```
**Expected Result:**
```
x^2 + 2x + 1 = 0
One solution in R:
-1
```
     

---

## **Test 24: Variable Assignment with Flexible Spacing**

```
> varA = 2
2
> varB= 2 * (4 + varA + 3)
18
> varC =2 * varB
36
> varD=2 *(2 + 4 *varC -4 /3)
```
**Expected Result:**
```
289.333333333
```
     

---

## **Test 25: Matrix with Multiple Rows**

```
> matA = [[1,2];[3,2];[3,4]]
```
**Expected Result:**
```
[ 1, 2 ]
[ 3, 2 ]
[ 3, 4 ]
```
  

---

## **Test 26: Single Row Matrix**

```
> matB=[[1,2]]
```
**Expected Result:**
```
[ 1, 2 ]
```
  

---

## **Test 27: Function with Flexible Spacing**

```
> funA(b) = 2*b+b
2 * b + b | or 3 * b if you simplify it
> funB(a)=2 * a
2 * a
> funC(y) =2* y + 4 -2 * 4+1/3
2 * y + 4 - 8 + 0.333333...
> funD(x)=2 *x
```
**Expected Result:**
```
2 * x
```
    

---

