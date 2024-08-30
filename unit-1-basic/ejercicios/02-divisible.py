# def es_divisible(a, b):
#     return a % b == 0
#     # if a % b == 0:
#     #     return True
#     # else:   
#     #     return False

from utils import es_divisible
import random

def run():
    a = int(input("Ingresar un número entero:"))
    b = int(input("Ingresar otro número entero:"))
    result = es_divisible(a, b)
    if result:
        print(f"El número {a} es divisible entre {b}")
    else:
        print(f"El número {a} no es divisible entre {b}")

if __name__ == '__main__':
    run()