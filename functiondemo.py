

# 第一个参数要传的，第2个参数不传默认eggs
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs



print(f('one','two'))
