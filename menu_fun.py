import main


default_days = '0'
default_name = 'None'
programs_list = main.read_list()




# option 1 in the menu
def creating_option():
    name = input('Enter the name of the program : ')
    for n in range(len(programs_list)):
        if str(name) == str(programs_list[n]):
            print("This name is already taken. Please try again")
            return
    days = input('Enter the number of days : ')
    if (not main.num_error(days)):
        return
    program2 = main.Main(days, name)
    for w in range(int(program2.days)):
        num_exe = input('Enter the number of exercises for Workout ' + str(w+1) + ' : ')
        if not main.num_error(num_exe):
            return main.create_exercise()
        program2.workouts.append(main.create_workout(num_exe))

    program2.display_weekly()
    program2.save_weekly()
    programs_list.append(program2.name)
    main.save_list(programs_list)

# option 2 in the menu
def update_option():
    program2 = main.Main(default_days, default_name)
    print('Select the program you want to update.')
    print('0: Return to menu.')
    # printing all the programs that are saved
    for n in range(len(programs_list)):
        print(str(n + 1) + ': ' + programs_list[n])
    val = input()
    if val == '0':
        return
    elif (int(val) > len(programs_list)) or (int(val) < 0):
        print("Please choose one of the options.")
        return update_option()
    name = programs_list[int(val) - 1]
    program2.read_weekly(name)
    print( 'If you want to up the weight enter +\nIf you want to decrease the weight enter - \nIf you want to keep the weight enter 0')
    for i in range(int(program2.days)):
        print('Workout ' + str(i + 1))
        for key, value in program2.workouts[i].items():
            jump = float(value[3])
            value[2] = float(value[2])
            print(key + ': ')
            answer = input()
            if answer == '+':
                value[2] += jump
            if answer == '-':
                value[2] -= jump
            if answer == '0':
                continue

    program2.display_weekly()
    program2.save_weekly()

# option 3 in the menu
def display_option():
    program2 = main.Main(default_days, default_name)
    print('Select the program you want to display.')
    print('0: Return to menu.')
    for n in range(len(programs_list)):
        print(str(n + 1) + '. ' + programs_list[n])
    val = input()
    if val == '0':
        return
    elif (int(val) > len(programs_list)) or (int(val) < 0):
        print("Please choose one of the options.")
        return display_option()
    name = programs_list[int(val) - 1]
    program2.read_weekly(name)
    program2.display_weekly()




def delete_option():
    print('Select the program you want to delete.')
    print('0: Return to menu.')
    for n in range(len(programs_list)):
        print(str(n + 1) + '. ' + programs_list[n])
    val = input()
    if val == '0':
        return
    elif (int(val) > len(programs_list)) or (int(val) < 0):
        print("Please choose one of the options.")
        return delete_option()
    name = programs_list[int(val) - 1]
    main.delete_program(name)
    programs_list.remove(name)
    main.save_list(programs_list)

