def sumatodos(limitto):
    resultado = 0
    for i in range(0,limitto+1):
        resultado += i
        
    return resultado

def sumatodosloscuadrados(limitto):
    resultado = 0
    for i in range(limitto+1):
        resultado += i*i
    return resultado

print(sumatodos(100))
print(sumatodosloscuadrados(3))
