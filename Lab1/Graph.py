import numpy as np
from sympy import*
x,y,t  = symbols('x y t')

print("1.1.5")
buf = ((1 - I)/(I + 1)) - ((2- 3*I)/(1 - 2*I))
buf = expand(buf)
print(buf)

print("1.2.5")
buf2 = (-(1/2) + (sqrt(3)/2)* I)**12
buf2 = expand(buf2)
print(buf2)

print("1.2.5")
x = symbols('x')
buf3 = solve(x**6 - 729, x)
print(buf3)

print("2.1.5")
x,y,z,t = symbols('x, y, z, t')
expr = (x**2 + x - 12)/(2*x**2-7*x+3)
print(limit(expr,x,3))

expr2 = (sqrt(4*x - 5) - sqrt(x + 1))/2 * x**2 - 5*x + 2
print(limit(expr2, x ,2))

print("2.2.5")

p = 3.14
expr3 = (x*2 - p*2)/tan(5*x)
print(limit(expr3,x,3.14))

expr4 = (1 - cos(4*x))/(2*x*sin(5*x))
print(limit(expr4,x,0))

print("2.3.5")

expr5 = (2*x - 1)* abs(ln(x-2) - ln(x+1))
print(limit(expr5,x,0))

expr6 = ((x + 3)/(2*x-1))**((2*x**2-1)/x)
print(limit(expr6,x,0))

print("4.1.5")

pprint(diff(cos(sin(3*x)**5)))

pprint(diff(1+cos(x**5)**2)*sin(4*x))

pprint(diff(ln(x + acos(sqrt(1 - x**2)))))

pprint(diff(ln(atan(1/x))**5))

print("4.3.5")

pprint(diff(ln(1+t**4)))

pprint(diff(atan(t**2)))

print("4.4.5")

pprint(diff(sin(sqrt(x)))**1/x)