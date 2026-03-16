from root_finding import RootFindingProblem

# x^3 - x - 2
f = lambda x: x**3 - x - 2
df = lambda x: 3 * x**2 - 1
g = lambda x: (x + 2) ** (1 / 3)
p1 = RootFindingProblem(f=f, df=df, g=g)
print("\n+ The Root of The Equation x^3 - x - 2 = 0 Using Each Method Below is:\n")
print(f"=> Bisection: {p1.solve('bisection',a=1,b=2)}")
print(f"=> Fixed Point: {p1.solve('fixed_point',x0=1.5)}")
print(f"=> Newton: {p1.solve('newton',x0=1.5)}")
print(f"=> Secant: {p1.solve('secant',x0=1,x1=2)}")
print(f"=> False Position: {p1.solve('false_position',a=1,b=2)}")
print(f"=> Steffensen: {p1.solve('steffensen',x0=1.5)}\n")
# 2x^3 - 6x + 2
coeffs = [2, 0, -6, 2]
print(
    "+ Polynomial Evaluation Using Horner Method for The Equation 2x^3 - 6x + 2 = 3 is:\n"
)
print(f"=> Horner: {p1.solve('horner',coeffs=coeffs,x=3)}\n")
# x^2 + 1
p2 = RootFindingProblem(f=lambda x: x**2 + 1)
print("+ The Root of The Equation x^2 + 1 = 0 is:\n")
print(f"=> Muller: {p2.solve('muller',x0=1,x1=1.5,x2=2)}\n")
