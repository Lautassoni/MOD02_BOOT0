def sumatodos(limitto):
    resultado = 0
    for i in range(0,limitto+1):
        resultado += 1
        
    return resultado
print(sumatodos(100))