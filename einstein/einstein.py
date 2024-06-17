def main():
    m = int(input("m: "))
    e = emc2(m)
    print("E: {}".format(str(e)))

def emc2(m):
    e = (300000000**2) * m
    return e

main()
