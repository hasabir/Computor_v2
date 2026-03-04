# ComputorV2

<div align="center">

**An advanced computational calculator supporting complex numbers, matrices, functions, and polynomial equation solving**

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)


</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Getting Started](#getting-started)
  - [Data Types](#data-types)
  - [Operations](#operations)
  - [Variables](#variables)
  - [Functions](#functions)
  - [Polynomial Equations](#polynomial-equations)
- [Examples](#-examples)
- [Testing](#-testing)

---

## 🎯 Overview

ComputorV2 is a sophisticated command-line calculator that extends beyond basic arithmetic operations. It provides a powerful computational environment capable of handling:

- **Rational Numbers** (integers and decimals)
- **Complex Numbers** (with imaginary unit `i`)
- **Matrices** (multi-dimensional arrays)
- **Functions** (with automatic simplification)
- **Polynomial Equation Solving** (up to degree 2)

The calculator features an interactive REPL (Read-Eval-Print Loop) shell with history support, making it ideal for mathematical exploration, scientific calculations, and educational purposes.

---

## ✨ Features

### Core Capabilities

- ✅ **4 Data Types**: Rationals, Complex Numbers, Matrices, Functions
- ✅ **8 Mathematical Operators**: `+`, `-`, `*`, `/`, `%`, `^`, `**`, `=?`
- ✅ **Variable Management**: Case-insensitive storage and retrieval
- ✅ **Expression Evaluation**: Query operator `=?` for expression resolution
- ✅ **Function Definitions**: Automatic simplification and symbolic computation
- ✅ **Function Evaluation**: Direct substitution and calculation
- ✅ **Polynomial Solving**: Automatic solving for linear and quadratic equations
- ✅ **Flexible Input Syntax**: Supports various spacing and formatting styles
- ✅ **Interactive Shell**: Command history and user-friendly interface

### Test Coverage

- **27/27 Mandatory Tests**: ✅ All passing
- **Comprehensive Test Suite**: See [TEST_RESULTS.md](TEST_RESULTS.md) for detailed results

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- readline library (usually included with Python)

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Computor_v2
   ```

2. **Run the calculator**:
   ```bash
   python3 computorv2.py
   ```

   Or make it executable:
   ```bash
   chmod +x computorv2.py
   ./computorv2.py
   ```

No additional dependencies required! The project uses only Python standard library modules.

---

## 💡 Usage

### Getting Started

Launch the interactive shell:

```bash
python3 computorv2.py
```

You'll see:
```
Welcome to ComputorV2!
Type 'help' for a list of commands.
> 
```

### Commands

- `help` - Display available commands
- `exit` - Exit the program
- `Ctrl+C` - Exit the program
- Comments: Lines starting with `#` are ignored

### Data Types

#### 1. Rational Numbers

```
> 42
42.0

> -3.14159
-3.14159

> 1/2
0.5
```

#### 2. Complex Numbers

Use `i` as the imaginary unit:

```
> 3 + 2i
3.0 + 2.0i

> -4 - 4i
-4.0 - 4.0i

> 2*i + 5
5.0 + 2.0i
```

#### 3. Matrices

Use `[[...];[...]]` syntax:

```
> [[2,3];[4,5]]
[2.0, 3.0]
[4.0, 5.0]

> [[1,2,3];[4,5,6];[7,8,9]]
[1.0, 2.0, 3.0]
[4.0, 5.0, 6.0]
[7.0, 8.0, 9.0]
```

#### 4. Functions

Define functions with a variable:

```
> f(x) = 2*x + 1
2 * x + 1

> g(y) = y^2 - 3*y + 2
y^2 - 3 * y + 2
```

### Operations

#### Basic Arithmetic

```
> 2 + 3
5.0

> 10 - 4
6.0

> 3 * 7
21.0

> 15 / 3
5.0

> 17 % 5
2.0

> 2^8
256.0
```

#### Order of Operations

ComputorV2 respects standard mathematical precedence:

```
> 2 + 3 * 4
14.0

> (2 + 3) * 4
20.0

> 2^3 * 4 + 1
33.0
```

### Variables

#### Assignment

```
> x = 5
5.0

> y = x * 2
10.0

> z = x + y
15.0
```

#### Variable Lookup

```
> x = ?
5.0
```

#### Type Changes

Variables can change types:

```
> a = 5
5.0

> a = 3 + 2i
3.0 + 2.0i

> a = [[1,2];[3,4]]
[1.0, 2.0]
[3.0, 4.0]
```

### Functions

#### Definition

```
> f(x) = 2*x^2 + 3*x - 5
2 * x^2 + 3 * x - 5
```

#### Automatic Simplification

```
> g(x) = 4*x + 5 - 2
4 * x + 3

> h(x) = 2*x + x
3 * x
```

#### Function Evaluation

Using query operator:

```
> f(x) = 2*x + 1
2 * x + 1

> f(3) =?
7.0

> f(0) =?
1.0
```

Direct assignment:

```
> result = f(5)
11.0
```

#### Using Variables in Functions

```
> a = 10
10.0

> f(x) = a * x + 5
10 * x + 5

> f(2) =?
25.0
```

### Polynomial Equations

Solve equations up to degree 2:

#### Linear Equations

```
> f(x) = 2*x + 4
2 * x + 4

> y = 0
0.0

> f(x) = y?
Solution: x = -2.0
```

#### Quadratic Equations

```
> f(x) = x^2 + 2*x + 1
x^2 + 2 * x + 1

> f(x) = 0?
Solution: x = -1.0
```

Complex solutions:

```
> g(x) = x^2 + 1
x^2 + 1

> g(x) = 0?
Two complex solutions:
x1 = 0.0 + 1.0i
x2 = 0.0 - 1.0i
```

---

## 📚 Examples

### Example 1: Calculate Series

```
> a = 2 + 4 * 2 - 5 % 4 + 2 * (4 + 5)
27.0

> b = 2 * a - 5 % 4
53.0

> c = 2 * a - b
1.0
```

### Example 2: Function Composition

```
> f(x) = 2*x + 3
2 * x + 3

> a = 5
5.0

> result = f(a)
13.0
```

### Example 3: Complex Calculations

```
> z1 = 3 + 4i
3.0 + 4.0i

> z2 = 1 - 2i
1.0 - 2.0i

> z1 + z2 =?
4.0 + 2.0i
```

### Example 4: Matrix Operations

```
> m1 = [[1,2];[3,4]]
[1.0, 2.0]
[3.0, 4.0]

> m2 = [[5,6]]
[5.0, 6.0]
```

### Example 5: Solving Equations

```
> f(x) = x^2 - 5*x + 6
x^2 - 5 * x + 6

> f(x) = 0?
Two solutions in R:
x1 = 2.0
x2 = 3.0
```

---


## License

This project is part of the 42 school curriculum.

---

<div align="center">

**Happy Computing! 🧮**

</div>