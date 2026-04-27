"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

import sys

try:
    total = float(sys.argv[1])
    supports = float(sys.argv[2])

    result = total / supports

    print("Load per support point:", round(result, 2), "N")

except:
    print("Error: Invalid input!")