"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:
    """
    Implementación de una clase 'Perro'.
    """

    def ladrar(self):
        """
        Método que hace ladrar a la instancia de 'Perro'.
        """
        self.ladra = 'Guau'
        print(self.ladra);

p = Perro();
p.ladrar();
