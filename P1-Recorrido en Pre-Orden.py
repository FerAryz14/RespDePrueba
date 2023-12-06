class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


raiz = Nodo('Abuelo')
raiz.izquierda = Nodo('Papá')
raiz.derecha = Nodo('Mamá')
raiz.izquierda.izquierda = Nodo('Hijo1')
raiz.izquierda.derecha = Nodo('Hijo2')
raiz.derecha.izquierda = Nodo('Hija1')


def preorden(nodo):
    if nodo:
        print(nodo.valor)
        preorden(nodo.izquierda)
        preorden(nodo.derecha)
        
        
print ('El orden del Árbol familiar con recorrido en Pre-orden es:')
preorden(raiz)