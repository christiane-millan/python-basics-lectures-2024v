class Videogame():

    def __init__(self, name : str = "", 
                release_year : int = 1980,
                type_game : str = "") -> None:
        
        self.name = name
        self.release_year = release_year
        self.platform = []
        self.type_game = type_game

    def add_videogame(self) -> None:
        self.name = input("Nombre del juego:")
        n = int(input("Número de plataformas: "))        
        for i in range(n):
            platform = input("Plataforma: ")
            self.platform.append(platform)
        
        self.release_year = int(input("Año de lanzamiento:"))
        self.type_game = input("Tipo de juego:")

    def __str__(self) -> str:
        return f"""Nombre: {self.name}
        Año de lanzameinto: {self.release_year}
        Plataformas: {self.platform}
        Tipo de juego {self.type_game}"""