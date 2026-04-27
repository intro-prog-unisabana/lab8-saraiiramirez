"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    file_path = sys.argv[1]

    
    if len(sys.argv) > 2:
        command = sys.argv[2]

        if command == "view":
            tasks = read_todo_file(file_path)

            print("Tasks:")
            for task in tasks:
                print(task)

        else:
            raise ValueError("Command not found!")

   

except IndexError as e:
    print(e)
except ValueError as e:
    print(e)