from sympy import symbols, Eq, nsolve

x1 = symbols('x1')
equation = [Eq(12+x1, 3)]
firstAns = [0]
decision = nsolve(equation, (x1, ), firstAns)
print(f"x1 = {decision[0]}")