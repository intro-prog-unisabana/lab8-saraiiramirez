"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    print("Command-line arguments:")
    for arg in sys.argv[1:]:
        print(arg)

    tasks = read_todo_file(sys.argv[1])

    print("\nTasks:")
    for task in tasks:
        print(task)

except IndexError as e:
    print(e)
