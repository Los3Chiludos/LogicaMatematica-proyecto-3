class Nodo:
    def __init__(self, izquierda, derecha, abajo, valor, num):
        self.izquierda = izquierda
        self.derecha = derecha
        self.abajo = abajo
        self.valor = valor
        self.numero = num

    def __str__(self):
        return "Nodo " + str(self.valor) + " : IZQ: (" + str(self.izquierda) + ") DER: (" + str(self.derecha) + ") ABJ: (" + str(self.abajo) + ")"
