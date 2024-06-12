"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehículo:
    """
    Implementación de la superclase 'Vehículo'.
    """
    def __init__(self, num_serie, color, fabricante):
        """
        Constructor de la clase 'Vehículo'.
        :param num_serie: Número de serie del vehículo.
        :param color: Color del vehículo.
        :param fabricante: Fabricante del vehículo.
        """
        self.__num_serie = num_serie
        self.__color = color
        self.__fabricante = fabricante


class Coche(Vehículo):
    """
    Implementación de una clase 'Coche' que hereda de la superclase 'Vehículo'.
    """

    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';

    def __init__(self):
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase 'Coche'.
        :param num_serie: Número de serie del coche.
        :param cilindrada: Cilindrada del coche.
        :param fabricante: Fabricante del coche.
        :param color: Color del coche.
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """
        Método getter del atributo 'número de serie' del coche.
        :return: Se devuelve el número de serie del coche.
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Método setter del atributo 'número de serie' del coche.
        :param value: Valor del nuevo número de serie del coche.
        """
        self.__num_serie = value

    @property
    def color(self):
        """
        Método getter del atributo 'color' del coche.
        :return: Se devuelve el color del coche.
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Método setter del atributo 'color' del coche.
        :param value: Valor que indica el nuevo color del coche.
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Método getter del atributo 'cilindrada' del coche.
        :return:  Se devuelve la cilindrada del coche.
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Método setter del atributo 'cilindrada' del coche.
        :param value: Se indica el nuevo valor que se le quiera dar al campo 'cilindrada'.
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Método getter del atributo 'fabricante' del coche.
        :return: Se devuelve el fabricante del coche.
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Método setter del atributo 'fabricante' del coche.
            :param value: Se pasa como parámetro el nuevo valor que indica cuál es el fabricante del coche.
        """
        self.__fabricante = value
