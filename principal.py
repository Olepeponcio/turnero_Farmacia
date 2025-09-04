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
          f"[C] COSMETICA\n"
          f"[S] SALIR")


def seleccion_seccion(lista: list):
    lista = list(lista)
    seccion = '0'
    while seccion not in lista:
        try:
            seccion = input("Introduzca el codigo de departamento: ").upper()
        except ValueError as e:
            print("Entrada no valida, debes introducir 'P', 'F', 'C' o 'S")
        else:
            pass
        return seccion


def fun_vuelve_al_menu():
    try:
        tecla = input("Pulsa cualquier tecla para volver al menú... ")
    except TypeError as e:
        print(f"error {e}")
    except ValueError as e:
        print(f"error {e}")
    else:
        pass


"""funcion principal"""


def inicio():
    """variables del programa"""

    salir_turnero = False
    seccion_elegida = None
    lista_seccion = ['P', 'F', 'C', 'S']

    """generarmos los objetos y asignamos valor a su atributo correspondiente"""
    seccion_perfumeria = numeros.GeneradorTurnos(None, "Perfumeria")
    seccion_perfumeria.asigna_seccion()
    seccion_farmacia = numeros.GeneradorTurnos(None, "Farmacia")
    seccion_farmacia.asigna_seccion()
    seccion_cosmeticos = numeros.GeneradorTurnos(None, "Cosmeticos")
    seccion_cosmeticos.asigna_seccion()

    while not salir_turnero:
        """bienvenida y seleccion de seccion"""

        saludo_bienvenida()
        muestra_seleccion()
        seccion_elegida = seleccion_seccion(lista_seccion)
        try:
            if seccion_elegida in lista_seccion:
                if seccion_elegida == 'P':
                    next(seccion_perfumeria.genera_turno())
                elif seccion_elegida == 'F':
                    next(seccion_farmacia.genera_turno())
                elif seccion_elegida == 'C':
                    next(seccion_cosmeticos.genera_turno())
                elif seccion_elegida == 'S':
                    salir_turnero = True
        except TypeError as e:
            print(f"Error type: {e}")
        except ValueError as e:
            print(f"Error value: {e}")

        if not salir_turnero:
            fun_vuelve_al_menu()

        os.system('cls')


inicio()
