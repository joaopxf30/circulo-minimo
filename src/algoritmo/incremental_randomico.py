import random
from src.algoritmo.circulo_minimo_abstrato import CirculoMinimo
from src.dominio import Ponto, Circulo


class IncrementalRandomico(CirculoMinimo):
    def determina_circulo_minimo_envolvente(self) -> Circulo:
        random.shuffle(self.pontos)

        circulo = Circulo.inicializa_por_dois_pontos(self.pontos[0], self.pontos[1])
        pontos_contemplados = [self.pontos[0], self.pontos[1]]

        for ponto in self.pontos[2:]:
            vetor = ponto - circulo.centro
            distancia = vetor.calcula_norma_euclidiana()

            if distancia > circulo.raio:
                circulo = self._obtem_circulo_minimo_que_atende_um_ponto(
                    pontos_contemplados=pontos_contemplados,
                    ponto_fronteira=ponto
                )

            pontos_contemplados.append(ponto)

        return circulo

    def _obtem_circulo_minimo_que_atende_um_ponto(
        self,
        pontos_contemplados: list[Ponto],
        ponto_fronteira: Ponto
    ) -> Circulo:
        circulo = Circulo.inicializa_por_dois_pontos(pontos_contemplados[0], ponto_fronteira)
        _pontos_contemplados = [pontos_contemplados[0]]

        for ponto in pontos_contemplados[1:]:
            vetor = ponto - circulo.centro
            distancia = vetor.calcula_norma_euclidiana()

            if distancia > circulo.raio:
                circulo = self._obtem_circulo_minimo_que_atende_dois_pontos(
                    pontos_contemplados=_pontos_contemplados,
                    ponto_fronteira_1=ponto,
                    ponto_fronteira_2=ponto_fronteira
                )

            _pontos_contemplados.append(ponto)

        return circulo

    @staticmethod
    def _obtem_circulo_minimo_que_atende_dois_pontos(
        pontos_contemplados: list[Ponto],
        ponto_fronteira_1: Ponto,
        ponto_fronteira_2: Ponto
    ) -> Circulo:
        circulo = Circulo.inicializa_por_dois_pontos(ponto_fronteira_1, ponto_fronteira_2)

        for ponto in pontos_contemplados:
            vetor = ponto - circulo.centro
            distancia = vetor.calcula_norma_euclidiana()

            if distancia > circulo.raio:
                circulo = Circulo.inicializa_por_tres_pontos(ponto, ponto_fronteira_1, ponto_fronteira_2)

        return circulo