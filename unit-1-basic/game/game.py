import random 

def input_options():
    options = ('piedra', 'papel', 'tijera')

    while(True):
        user_option = input('piedra, papel o tijera:')
        user_option = user_option.lower()

        if user_option in options:
            break

    cpu_option = random.choice(options)
    return user_option, cpu_option

def validate_winner(user_option, cpu_option):
    if user_option == cpu_option:
        print("Empate!!!")

    elif user_option == 'piedra':
        if cpu_option == 'papel':
            print("CPU win")
        else:
            print("User win")

    elif user_option == 'papel':
        if cpu_option == 'piedra':
            print("User win")
        else:
            print("CPU win")
        
    elif user_option == 'tijera':
        if cpu_option == 'piedra':
            print("CPU win")
        else:
            print("User win")

def run():
    user, cpu = input_options()
    validate_winner(user, cpu)

if __name__ == '__main__':
   run() 