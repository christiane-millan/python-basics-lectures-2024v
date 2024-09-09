from videogame import Videogame

def menu():
    menu = """
    1. Agregar juego a la colección
    2. Eliminar juego de la colección
    3. Imprimir colección
    4. Salir

    
    """
    print(menu)
    option = int(input("Ingrese una opción: "))
    return option

def run():
    videogame_list = []  

    while(True):
        option = menu()    
        
        if option == 1:
            new_videogame = Videogame()
            new_videogame.add_videogame()
            videogame_list.append(new_videogame)

        elif option == 2:
            del_videogame = videogame_list.pop()
            print(f"{del_videogame.name} borrado...")

        elif option == 3:
            for v in videogame_list:
                print(v)
        elif option == 4:
            break

if __name__ == "__main__":
    run()