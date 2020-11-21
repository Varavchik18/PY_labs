import numpy as np
from sympy import*
x,y,t  = symbols('x y t')

#2.1
expr = (3*x**2-7*x+2)/(3*x**2+2*x-1)
print("Task 2.1")
print(limit(expr,x,1/3))


expr = (4*x**2+3*x-1)/(sqrt(5*x+6) - sqrt(3*x+4))
print(limit(expr,x,1))

#2.2
print("Task  2.2")
expr = (sin(3*x)+sin(7*x)/(sin(3*x)-sin(5*x)))
print(limit(expr,x,0))

expr = (cos(2*x)+1)/(1-sin(x))
print(limit(expr,x,pi/2))  

#2.3
print("Task 2.3")
expr = pow((2*x+5), (2/x**2-4))
print(limit(expr,x,-2))  

expr = (exp(3*x) - exp(x))/(ln(cos(sqrt(x))))
print(limit(expr,x,0))  

#4.1
print("Task 4.1")
cotan = cos(x)/sin(x)
pprint(diff(pow((cotan+tan(x**2)), 1/3),x))
pprint(diff( log( (x / (sqrt(1-x**2))), 3 ),x))
pprint(diff(pow(10, sqrt(ln(x))) * pow(3, tan(x)) ) )

pprint(diff( (5*atan(ln(x)**2)-1),x))

pprint(diff( ( atan(x)-atan(y) ) ,x) )

#4.3
print("Task 4.3")
x=ln(tan(t))
y=(1/(pow(cos(t),2)) )

dydx = diff(y, t)/diff(x, t)
pprint(dydx)

#4.4
print("Task 4.4")
x  = symbols('x')
pprint(diff( pow(log(x),(x/2) ) ,x) )

#1.1
print("Task 1.1")
buf = (((2+I)/(3*I-1))+pow(2*I-1,3))
buf= expand(buf)
print(buf)

#1.2
print("Task 1.2")
buf = pow( -1*((1/sqrt(2)))-(1/sqrt(2))*I ,11)
buf= expand(buf)
print(buf)

#1.3
print("Task 1.3")
x=symbols('x')
buf = solve(x**3+8, x)
print(buf)
