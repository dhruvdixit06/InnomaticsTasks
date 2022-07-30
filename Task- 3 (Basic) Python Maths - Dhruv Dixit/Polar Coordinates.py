import cmath
n=complex(input())
r=(n.real**2 + n.imag**2)**0.5
print(r)
print(cmath.phase(n))