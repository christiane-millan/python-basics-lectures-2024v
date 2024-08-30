from calculator.calculator_poo import Calculator, Plus, Sustraction, Multi

if __name__ == "__main__":

    calculator = Calculator()
    while(True):
        option = calculator.menu()

        if option == 1:
            operation = Plus()
        elif option == 2:
            operation = Sustraction()
        elif option == 3:
            operation = Multi()

        elif option == 7:
            calculator.show_history()
            input("Presionar cualquier tecla para continuar...")
            continue
        elif option == 8:
            calculator.pop_history()
            continue
        elif option == 9:
            calculator.delete_history()
            continue
        elif option == 10:
            break

        operation.operation()
        operation.__result = 0
        result = operation.show_operation()
        print(result)
        calculator.history.append(result) 
        input("Presionar cualquier tecla para continuar...")