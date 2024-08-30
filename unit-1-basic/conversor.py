

def conversor(currency, value):
    dollar = round(currency / value, 2)
    return dollar

menu = """Conversor de pesos a dollares

1.- Pesos mexicanos a dolares
2.- Pesos argentinos a dolares
3.- Pesos colombianos a dolares
4.- Salir
"""

def run():
    print(menu)
    opcion = int(input("Ingresar opción:"))
    if opcion == 1:
        pesos = float(input("Ingresar cantidad en pesos mexicanos: "))
        dollars = conversor(pesos, 18.90)
        print(f'${pesos} MXN en dollares es igual a ${dollars}')
    elif opcion == 2:
        pesos = float(input("Ingresar cantidad en pesos argentinos: "))
        dollars = conversor(pesos, 939.27)
        print(f'${pesos} ARS en dollares es igual a ${dollars}')
    elif opcion == 3:
        pesos = float(input("Ingresar cantidad en pesos colombianos: "))
        dollars = conversor(pesos, 4065.41)
        print(f'${pesos} COP en dollares es igual a ${dollars}')
    elif opcion == 4:
        return(False)
    else:
        print("Opción invalida")   
    return(True)

if __name__ == "__main__":
    while(True):
        if not run():
            break

