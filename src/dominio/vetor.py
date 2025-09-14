import math


class Vetor:
    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y

    def __mul__(self, escalar: float) -> "Vetor":
        if isinstance(escalar, float):
            vetor = self.__calcula_produto_escalar(escalar)

            return vetor

        raise TypeError("Somente operações envolvendo escalar estão implementadas")

    def calcula_norma_euclidiana(self) -> float:
        p_norma_2 = math.sqrt(self.coord_x**2 + self.coord_y**2)

        return p_norma_2

    def __calcula_produto_escalar(self, escalar: float) -> "Vetor":
        if escalar < 0 or escalar > 1:
            raise ValueError("Parâmetro deve estar entre 0 e 1")

        coord_x = escalar * self.coord_x
        coord_y = escalar * self.coord_y

        return Vetor(coord_x, coord_y)