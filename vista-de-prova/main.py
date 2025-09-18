from q1 import *
from q2 import *
from q6 import *
from q7 import *

from arrays import *

if __name__ == "__main__":
    print("Verificar Vetor Ordenado (Já ordenado):\n")

    print(f"Vetor: {dicionarios["already_sorted"]}")
    print(f"Ordenado?", verifica(dicionarios["already_sorted"]), "\n")

    print("Verificar Vetor Ordenado (Reverso):\n")

    print(f"Vetor: {dicionarios["inversed"]}")
    print(f"Ordenado?", verifica(dicionarios["inversed"]), "\n")

    print("Bubble Sort:\n")

    for nome, lista in dicionarios.items():
        print(f"Original '{nome}': {lista}")
        bubble_sort(lista)
        print(f"Ordenado '{nome}': {lista}\n")

    print("Insertion Sort:\n")

    for nome, lista in dicionarios.items():
        print(f"Original '{nome}': {lista}")
        insertion_sort(lista)
        print(f"Ordenado '{nome}': {lista}\n")

    print("Insertion Sort Recursivo:\n")

    for nome, lista in dicionarios.items():
        print(f"Original '{nome}': {lista}")
        insertion_sort_recursive(lista)
        print(f"Ordenado '{nome}': {lista}\n")