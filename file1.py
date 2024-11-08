def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def main(a,b):
    res_add=add(a,b)
    res_sub=sub(a,b)
    print(f"the addition of {a} and {b} is: {res_add}")
    print(f"the substraction of {a} and {b} is: {res_sub}")
main(2,4)