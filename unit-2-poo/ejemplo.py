class Student():
    """Modelo del estudiante para sistema de control escolar"""

    def __init__(self, f_name = "", l_name="", control=0, program=""):
        self.first_name =  f_name
        self.last_name = l_name
        self.control_number = control
        self.program = program

    def add_student(self):
        print("Ingresar datos del estudiante")
        self.first_name = input("Ingresar nombre:")
        self.last_name = input("Ingresar apellido: ")
        self.control_number = int(input("Ingresar número de control: "))
        self.program = input("Ingresar programa de posgrado: ")

    def show_data(self):
        print("Datos alumno:")
        print(f'Nombre: {self.first_name}')
        print(f'Apellido: {self.last_name}')
        print(f'No. Control: {self.control_number}')
        print(f'Programa de posgrado: {self.program}')

class Classroom():
    name = str
    classroom = int
    student_list = []

    def __init__(self, name, classroom, student_list):
        self.name = name
        self.classroom = classroom
        self.student_list = student_list

    def add_student(self, student):
        self.student_list.append(student)

    def show_studen_list(self):
        for student in self.student_list:
            student.show_data()


if __name__ == "__main__":
    programming_classroom = Classroom("Programación", 11, [])

    num = int(input("Numero de estudiantes a ingresar:"))
    for i in range(num):
        student = Student()
        student.add_student()

        programming_classroom.add_student(student)
    
    programming_classroom.show_studen_list()