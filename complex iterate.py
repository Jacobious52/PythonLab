import csv

def mod(z):
    if type(z) == complex:
        return ((z.real**2)+(z.imag**2))**0.5

def iterate(z, c, i):

    l = [["zi", "z", "|z|"], ["","",""]]

    for j in range(1, i+1):
        z=(z*z)+c
        l.append(["z{0}".format(j), z, mod(z)])
        print("z{0} = {1:.4f}".format(j ,z))
        print("|z{0}| = {1:.4f}".format(j, mod(z)))
        print("")

    return l

def write_sheet(fname, data):
    with open(fname, "w") as f:
        w = csv.writer(f)
        w.writerows(data)

if __name__ == "__main__":
	write_sheet("iterations.csv", iterate((0.6+0.8j), (0.5+0.3j), 10))