#jade rojas
#28-4-25
def funcion(a, b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    for arg in args:
        print("arg=", arg)
    for key, value in kwargs.items():
        print(key, "=", value)
funcion(1,2, 14, 21, 24, 36, 37, x="luis", y="sol", C="mexico")