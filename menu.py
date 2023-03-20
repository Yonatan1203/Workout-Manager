import main
import menu_fun
import pathlib as path
import os


while True:
    selector = input('Menu:\n' + '1: Creating a new program\n2: Update a program\n3: Display a program\n4: Delete a program\n5: Exit\n')
    try:
        if int(selector) == 1:
            menu_fun.creating_option()

        if int(selector) == 2:
            menu_fun.update_option()

        if int(selector) == 3:
            menu_fun.display_option()

        if int(selector) == 4:
            menu_fun.delete_option()

        if int(selector) == 5:
            break
    except:
            print("Error. Please enter one of the options.")



