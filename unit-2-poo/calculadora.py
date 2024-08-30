class Calculator():

    operator_1 = float
    operator_2 = float
    result = float

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

    def plus(self, op1, op2):
        return op1 + op2
    
    def sustraction(self, op1, op2):
        return op1 - op2

    def get_operators(self, option):
        self.operator_1 = float(input("Ingesar valor uno:"))
        self.operator_2 = float(input("Ingesar valor dos:"))
        if option == 1:
            return self.plus(self.operator_1, self.operator_2)

        elif option == 2:
            return  self.sustraction(self.operator_1, self.operator_2)


if __name__ == "__main__":
    my_calculator = Calculator()
    my_calculator.menu()
