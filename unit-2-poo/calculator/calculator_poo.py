class Operation():
    number_1 = float
    number_2 = float
    __result = float

    def __init__(self):
        self.get_numbers()
        self.__result = 0

    def get_numbers(self):
        self.number_1 = float(input("Ingresar número a: "))
        self.number_2 = float(input("Ingresar número b: "))



class Sustraction(Operation):

    def operation(self):
        self.__result = self.number_1 - self.number_2

    def show_operation(self):
        return str(self.number_1) + " - " + str(self.number_2) + " = " + str(self.__result)

class Multi(Operation):
    def operation(self):
        self.__result = self.number_1 * self.number_2 

    def show_operation(self):
        return str(self.number_1) + " * " + str(self.number_2) + " = " + str(self.__result)
    
class Calculator():

    history = []

    def menu(self):
        menu = """Calculadora de Cesar

        1.- Suma
        2.- Resta
        3.- Multiplicación
        4.- División
        5.- Residuo
        6.- Potencia
        7.- Lista el historial de operaciones
        8.- Borrar la última operación del historial
        9.- Borrar todo el historial de operaciones
        10.-Salir de la calculadora
        """
        
        option = int(input(menu))
        return(option)
    
    def show_history(self):
        for h in self.history:
            print(h)

    def pop_history(self):
        self.history.pop()

    def delete_history(self):
        self.history = []

