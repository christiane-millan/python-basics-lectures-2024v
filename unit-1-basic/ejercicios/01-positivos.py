def determinar_positividad(n):
    if n > 0:
        return 'P'
    else:
        return 'N'

def run():
    n = int(input("Ingresar un número entero:"))
    result = determinar_positividad(n)
    print(result)

if __name__ == '__main__':
    run()