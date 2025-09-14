from src.dominio.vetor import Vetor
import math


class Ponto:
    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y

    def __add__(self, outro: Vetor) -> "Ponto":
        if not isinstance(outro, Vetor):
            raise TypeError("Operando deve ser da classe Vetor")

        coord_x = self.coord_x + outro.coord_x
        coord_y = self.coord_y + outro.coord_y

        return Ponto(coord_x, coord_y)

    def __sub__(self, outro: "Ponto") -> Vetor:
        if not isinstance(outro, Ponto):
            raise TypeError("Operando deve ser da classe Ponto")

        coord_x = self.coord_x - outro.coord_x
        coord_y = self.coord_y - outro.coord_y

        return Vetor(coord_x, coord_y)

    def busca_ponto_medio(self, outro: "Ponto") -> "Ponto":
        if not isinstance(outro, Ponto):
            raise TypeError("Operando deve ser da classe Ponto")

        ponto = self + (outro - self) * 0.5

        return ponto

    @staticmethod
    def inicializa_com_coordenadas_polares(centro: "Ponto", theta: float, raio: float) -> "Ponto":
        coord_x = centro.coord_x + raio * math.cos(theta)
        coord_y = centro.coord_y + raio * math.sin(theta)

        return Ponto(coord_x, coord_y)
