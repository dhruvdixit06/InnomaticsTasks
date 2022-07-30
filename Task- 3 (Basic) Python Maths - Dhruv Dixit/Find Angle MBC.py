import math
ab = int(input())
bc = int(input())
h = math.sqrt(ab**2+bc**2)
t = math.acos(bc/h)
print(str(round(math.degrees(t)))+"\N{DEGREE SIGN}")