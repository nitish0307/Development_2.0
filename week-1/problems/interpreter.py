exp = input("Expression: ")
x, y, z = exp.split(" ")
x1 = float(x)
z1 = float(z)

if y == "+":
    print(x1 + z1)
elif y == "-":
    print(x1 - z1)
elif y == "*":
    print(x1 * z1)
elif y == "/":
    print(x1 / z1)


