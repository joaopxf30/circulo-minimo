from src.algoritmo.circulo_minimo_abstrato import CirculoMinimo
from src.dominio import Ponto, Circulo


class Heuristico(CirculoMinimo):
    def determina_circulo_minimo_envolvente(self) -> Circulo:
        ponto_1, ponto_2 = self._acha_par_extremo_mais_distante()

        circulo = Circulo.inicializa_por_dois_pontos(ponto_1, ponto_2)

        for ponto in self.pontos:
            vetor = ponto - circulo.centro
            distancia = vetor.calcula_norma_euclidiana()

            if distancia > circulo.raio:
                centro = circulo.centro + vetor * ((distancia - circulo.raio) / 2)
                raio = (distancia + circulo.raio) / 2
                circulo = Circulo(centro, raio)

        return circulo

    def _acha_par_extremo_mais_distante(self) -> tuple[Ponto, Ponto]:
        ponto_min_coord_x = min(self.pontos, key=lambda ponto: ponto.coord_x)
        ponto_max_coord_x = max(self.pontos, key=lambda ponto: ponto.coord_x)
        distancia_coord_x = (ponto_min_coord_x - ponto_max_coord_x).calcula_norma_euclidiana()

        ponto_min_coord_y = min(self.pontos, key=lambda ponto: ponto.coord_y)
        ponto_max_coord_y = max(self.pontos, key=lambda ponto: ponto.coord_y)
        distancia_coord_y = (ponto_min_coord_y - ponto_max_coord_y).calcula_norma_euclidiana()

        if distancia_coord_y >= distancia_coord_x:
            return ponto_min_coord_y, ponto_max_coord_y
        else:
            return ponto_min_coord_x, ponto_max_coord_x