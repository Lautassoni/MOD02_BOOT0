def normal(i):
    return i

def cuadrado(x):
    return x* x


def sumatodos(limitto, f):
    resultado = 0
    for i in range(limitto+1):
        resultado += f(i)
        
    return resultado

print(sumatodos(100, normal))
print(sumatodos(3, cuadrado))