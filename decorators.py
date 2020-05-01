def div(a,b):
    # main function
    print(a/b)


def smart_div(func):
    # decorator function
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner


div1 = smart_div(div)

div1(4,2)