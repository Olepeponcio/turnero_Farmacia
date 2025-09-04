import os
import sys
import numeros

"""para saber donde va, mensaje de bienvenida
mostramos cuadro seleccion. y solicitamos seccion
por input"""


def saludo_bienvenida():
    texto = "BIENVENIDO"
    for i in range(3):
        if i == 1:
            print(f"{texto:^20}")  # centrado
        else:
            print(("#") * 20)


def muestra_seleccion():
    print(f"[P] PERFUMERIA.\n"
          f"[F] FARMACIA.\n"
          f"[C] COSMETICA\n")


def seleccion_seccion(lista):
    lista = list(lista)
    seccion = str(input("Introduzca el codigo de departamento: ")).upper()
    while seccion not in lista_seccion:
        try:
            seccion = input("Introduzca el codigo de departamento: ")
        except ValueError as e:
            print("Entrada no valida, debes introducir 'P', 'F', 'C'")
        else:
            pass
        return seccion


"""funcion principal"""
def inicio():
    """variables del programa"""
    seccion_elegida = None
    lista_seccion = ['P', 'F', 'C']
    """generarmos los objetos"""
    seccion_perfumeria = numeros.GeneradorTurnos(None, "Perfumeria")
    seccion_farmacia = numeros.GeneradorTurnos(None, "Farmacia")
    seccion_cosmeticos = numeros.GeneradorTurnos(None, "Cosmeticos")
    """bienvenida y seleccion de seccion"""

    saludo_bienvenida()
    muestra_seleccion()
    # seccion_elegida = seleccion_seccion(lista_seccion)
    try:
        if seccion_elegida in lista_seccion:
            if seccion_elegida == 'P':
                seccion_perfumeria.genera_turno()
            elif seccion_elegida == 'F':
                seccion_farmacia.genera_turno()
            elif seccion_elegida == 'C':
                seccion_cosmeticos.genera_turno()
                pass
    except TypeError as e:
        print(f"Error type: {e}")
    except ValueError as e:
        print(f"Error value: {e}")

    os.system('cls')


inicio()
