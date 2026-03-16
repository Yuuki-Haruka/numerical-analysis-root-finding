# Root Finding Project

## Project description

This project implements a `RootFindingProblem` class for solving equations of the form:

\[
f(x) = 0
\]

using classical numerical methods written manually in Python.

## Implemented methods

- Bisection Method
- Fixed-point Iteration
- Newton's Method
- Secant Method
- False Position Method (Regular Falsi)
- Horner's Method
- Muller's Method
- Steffensen's Method (included because it appears in the required class structure)

## How the project solves the assignment

The class exposes exactly one public interface:

```python
solve(method, **kwargs)
```

The `solve()` method internally dispatches to private methods:

- `_bisection(...)`
- `_fixed_point(...)`
- `_newton(...)`
- `_secant(...)`
- `_false_position(...)`
- `_steffensen(...)`
- `_horner(coeffs, x)`
- `_muller(...)`

This follows the assignment structure.

## File structure

```text
root-finding-project/
│── root_finding.py
│── examples.py
│── README.md
```

## How to run the examples

From the project folder:

```bash
python examples.py
```

## Short example using solve()

```python
from root_finding import RootFindingProblem

f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1
g = lambda x: (x + 2)**(1/3)

coeffs=[2,0,-6,2]

p1 = RootFindingProblem(f=f, df=df, g=g)
p2 = RootFindingProblem(f=lambda x: x**2+1)

print(p.solve("bisection", a=1, b=2))
print(p.solve("newton", x0=1.5))
print(p.solve("secant", x0=1, x1=2))
```

## Notes

- No library root solvers are used.
- Only standard Python and `cmath` are used.
- Meaningful errors are raised for invalid intervals, missing derivative, missing fixed-point function, division by zero, and non-convergence.
