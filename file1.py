def add(a,b):
    return a+b

def mul(a,b):
    return a*b


def main(a,b):
    res_add=add(a,b)
    res_mul=mul(a,b)

    print(f"the addition of {a} and {b} is: {res_add}")
    print(f"the multiplication of {a} and {b} is: {res_mul}")


main(2,4)