def add(a,b):
    return a+b

def mul(a,b):
    return a*b
def sub(a,b):
    return a-b

def main(a,b):
    res_add=add(a,b)
    res_mul=mul(a,b)
    res_sub = sub(a, b)
    print(f"the addition of {a} and {b} is: {res_add}")
    print(f"the multiplication of {a} and {b} is: {res_mul}")
    print(f"the substraction of {a} and {b} is: {res_sub}")

main(2,4)