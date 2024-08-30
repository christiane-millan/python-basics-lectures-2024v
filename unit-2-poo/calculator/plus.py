from calculator.calculator_poo import Operation

class Plus(Operation):
    
    def operation(self):
        self.__result = self.number_1 + self.number_2
    
    def show_operation(self):
        return str(self.number_1) + " + " + str(self.number_2) + " = " + str(self.__result)
    