"""Clase de la que hereda generador, tiene un atributo para controlar
los tickets cargados en la maquina"""


class Turnero:
    MAX_TICKETS = 300

    def __init__(self, tickets_disponibles=None):
        self.tickets_disponibles = tickets_disponibles or self.MAX_TICKETS


"""hereda de Turnero, inicializa la constante para determinar los turnos que le corresponden
a cada seccion y añade un atributo seccon pasa por argumento tickets_disponibles por si 
se quiere modificar manualmente"""


class GeneradorTurnos(Turnero):
    condificador = None

    def __init__(self, tickets_disponibles, seccion):
        super().__init__(tickets_disponibles)
        self.seccion = seccion
        self.tickets_generador = self.MAX_TICKETS // 3

    def __str__(self):
        return f"seccion: {self.seccion}. num.Tickets: {self.tickets_generador}"

    def asigna_seccion(self):  # asigna el codificador dependiendo de la seccion introducida
        try:
            var = str(self.seccion.upper())
        except TypeError as e:
            print(f"imposible conversion. error: {e}")
        else:
            match str(self.seccion.upper()):
                case "PERFUMERIA":
                    self.condificador = 'P-'
                case "FARMACIA":
                    self.condificador = 'F-'
                case "COSMETICOS":
                    self.condificador = 'C-'

    def genera_turno(self):  # se resta tickets al cupo y se imprime seccion y num de espera
        if int(self.tickets_generador) == 0:
             print(f"Turnos para {self.seccion} a gotados.\n")
        else:
            self.tickets_generador -= 1
            print (f"{self.condificador} {(self.MAX_TICKETS // 3) - self.tickets_generador}")
        yield self.tickets_generador


generador_perfumeria = GeneradorTurnos(None, 'Perfumeria')
generador_perfumeria.asigna_seccion()
next(generador_perfumeria.genera_turno())
