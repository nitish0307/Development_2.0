def main():
    usr_input = input("m: ")
    inp = energy(usr_input)
    print(inp)

def energy(m):
    mass = int(m)
    c = 300000000
    e = mass * (c ** 2)
    return e

main()
