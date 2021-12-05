from pprint import pprint
from calculations import *
x = [0, 0, 0, 0, 1, 1, 1, 1]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 1, 0, 1, 0, 1, 0, 1]
f = [0, 0, 0, 0, 0, 0, 0, 1]
df = dual(f)
#Task1-2
print("Printing the whole table")
for i, _ in enumerate(x):
    print(str(x[i]) + "\t" + str(y[i]) + "\t" + str(z[i]) + "\t" +  str(f[i]) + "\t" + str(df[i]))
print()
#Task3
print("PDNF: " + PDNF(x,y,z,f))
print("PCNF: " + PCNF(x,y,z,f))
#Task4
print("Zhegalkin polynomial: " + polynomial(x,y,z,f))
#Task5
print("Function " + ("is " if is_linear(polynomial(x,y,z,f)) else "isn't ") + "linear")
print("Function " + ("is " if is_self_dual(f, df) else "isn't ") + "self-dual")
print("Function " + ("is " if is_monotone(f) else "isn't ") + "monotone")
print("Function " + ("does " if does_contain_const0(x,y,z,f) else "doesn't ") + "contain " + "0")
print("Function " + ("does " if does_contain_const1(x,y,z,f) else "doesn't ") + "contain " + "1")