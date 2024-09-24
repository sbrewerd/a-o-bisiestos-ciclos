def contar_años_bisiestos(año):
    contador = 0
    for i in range(1900, año + 1):
        if i % 4 == 0:
            if i % 100 != 0 or año % 400 == 0:
                contador += 1
    return contador
año_respondido = int(input("escribe un año entre 1900 y 2199 "))
if 1900 <= año_respondido <= 2199:
    bisiestos = contar_años_bisiestos(año_respondido)
    print(f"numero de años bisiestos hasta {año_respondido}: {bisiestos}")
else:
    print("no estas en el rango")
