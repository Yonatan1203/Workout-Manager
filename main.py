import pathlib as path
import os
import json


class Main:

    def __init__(self,days,name):
        self.days = days
        self.name = name
        self.workouts = []

    #printing a weekly routine
    def display_weekly(self):
        print('------' + self.name + '------')
        for workout in range(len(self.workouts)):
            print('----'  + ' Workout ' + str(workout +1) + '----' )
            display_workout(self.workouts[workout])
        print('------------------------------')

    #reading a program from file
    def read_weekly(self, name):
        with open(name + ".json", "r") as f:
            self_dict = json.load(f)
        self.name = self_dict['name']
        self.days = self_dict['days']
        self.workouts = []
        for day in range(int(self.days)):
            work = 'Workout ' + str(day + 1)
            self.workouts.append(self_dict[work])

    #saving a program in a file
    def save_weekly(self):
        self_dict = {'name': self.name, 'days': self.days}
        for day in range(int(self.days)):
            work = 'Workout ' + str(day + 1)
            dict = {work : self.workouts[day]}
            self_dict.update(dict)
        with open(self.name + ".json", "w") as f:
            json.dump(self_dict, f)



#defining what exercises
def create_workout(num_exe):
    workout = {}
    for i in range(int(num_exe)):
        print('Exercise ' + str(i+1) + ':')
        exercise = create_exercise()
        workout.update(exercise)
    return workout


def create_exercise():
    name = input('Enter the name of the exercise : ')
    for letter in name:
        if letter == ' ':
            name = name.replace(" ", "-")
    sets = input('Enter the number of sets : ')
    if not num_error(sets):
        return create_exercise()
    reps = input('Enter the number of repetitions : ')
    if not num_error(reps):
        return create_exercise()
    jump = input('Enter the weight of every jump : ')
    try:
        float(jump)
    except:
        return create_exercise()
    weight = input('Current weight on the exercise : ')
    try:
        float(weight)
    except:
        return create_exercise()
    exercise = { name : [sets, reps, weight, jump]}
    return exercise

# display function for the whole program
def display_workout(workout):
    for key, value in workout.items():
        print(key + ' - ' + str(value[0]) + ' x ' + str(value[1])+ ' Weight: ' + str(value[2]) + 'kg')

#saving the list of programs there is to a file
def save_list(list):
    programs_list = {'programs' : list}
    with open('list.json' , "w") as f:
        json.dump(programs_list, f)

#reading the list of programs there is to a list
def read_list():
    with open("list.json", "r") as f:
        dict_list = json.load(f)
    print(dict_list)
    list = dict_list['programs']
    return list

#deleting a file of a program
def delete_program(name):
    p = path.Path(name + ".json")
    os.remove(p)


def num_error(num):
    if (not num.isnumeric()) or (int(num) < 1):
        print("Error. Please try again.")
        return False
    else:
        return True











