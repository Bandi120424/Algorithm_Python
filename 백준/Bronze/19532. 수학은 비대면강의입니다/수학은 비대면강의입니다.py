import sys
a, b, c, d, e, f = map(int, input().split())

det = a*e-b*d
x = (e*c-b*f)//det
y = (-d*c+a*f)//det

print(x, y)