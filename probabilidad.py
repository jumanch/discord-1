import random

pregunta = str(input("Escribe de que quieres comprobar: "))
probabilidad= int(random.randint(0, 100))
separador = "="

def grafico():
    print("0%                     25%                       50%                     75%                       100%")
    print("|~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print(f"|{separador*probabilidad}|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~|")

if probabilidad >= 90:
    grafico()
    print("-¡Enhorabuena!")
elif probabilidad in range(60,90):
    grafico()
    print("- Ni tan mal.")
elif probabilidad in range(40,60):
    grafico()
    print("- UUUUUUuufff.")
elif probabilidad in range(20,40):
    grafico()
    print("-Lo siento.")  
elif probabilidad in range(0,20):
    grafico()
    print("- F.")

print(f"Hay un {probabilidad}% de probabilidades de {pregunta}.")
