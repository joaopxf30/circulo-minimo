import time
from src.algoritmo.heuristico import Heuristico
from src.algoritmo.incremental_randomico import IncrementalRandomico
from src.dominio import Ponto, Circulo
from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_circulo_envolvente, plota_tempo_execucao_algoritmos

NUMERO_MAXIMO_AMOSTRAS = 500
NUMEROS_PONTOS = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]


def compara_algoritmos(circulo: Circulo):
    tempos_heuristico = []
    tempos_incremental_randomico = []
    tempos_incremental_randomico_medio = []

    for numero_pontos in NUMEROS_PONTOS:
        print(f"Gerando círculo mínimo envolvente para nuvem de {numero_pontos} pontos")
        pontos = gera_nuvem_pontos(
            numero_pontos=numero_pontos,
            circulo=circulo,
        )

        _, tempo_execucao_heuristico = usa_algoritmo_heuristico(pontos)
        tempos_heuristico.append(tempo_execucao_heuristico)
        print("Algoritmo heurístico finalizado")

        tempos_incremental_randomico_amostral = []
        for amostra in range(0, NUMERO_MAXIMO_AMOSTRAS):
            _, tempo_incremental_randomico_amostral = (
                usa_alogirtmo_incremental_randomico(pontos)
            )
            print(f"Amostra número {amostra} do algoritmo incremental randômico finalizada")
            tempos_incremental_randomico_amostral.append(tempo_incremental_randomico_amostral)

        tempos_incremental_randomico.append(tempos_incremental_randomico_amostral)
        tempos_incremental_randomico_medio.append(
            sum(tempos_incremental_randomico_amostral) / len(tempos_incremental_randomico_amostral)
        )

    plota_tempo_execucao_algoritmos(NUMEROS_PONTOS, tempos_heuristico, tempos_incremental_randomico_medio, tempos_incremental_randomico)


def usa_algoritmo_heuristico(pontos: list[Ponto]) -> tuple[Circulo, float]:
    print("\nIniciando algoritmo heuristico")
    algoritmo = Heuristico(pontos)
    tempo_inicial = time.perf_counter()
    circulo_minimo = algoritmo.determina_circulo_minimo_envolvente()
    tempo_final = time.perf_counter()
    tempo_execucao = tempo_final - tempo_inicial
    print(circulo_minimo)
    print(f"Algoritmo heurístico finalizado para nuvem de {len(pontos)} pontos em {tempo_execucao}s\n")
    return circulo_minimo, tempo_execucao


def usa_alogirtmo_incremental_randomico(pontos: list[Ponto]) -> tuple[Circulo, float]:
    print("\nIniciando algoritmo incremental randomico")
    algoritmo = IncrementalRandomico(pontos)
    tempo_inicial = time.perf_counter()
    circulo_minimo = algoritmo.determina_circulo_minimo_envolvente()
    tempo_final = time.perf_counter()
    tempo_execucao = tempo_final - tempo_inicial
    print(circulo_minimo)
    print(f"Algoritmo incremental randômico finalizado para nuvem de {len(pontos)} pontos em {tempo_execucao}s")
    return circulo_minimo, tempo_execucao


if __name__ == '__main__':
    circulo = Circulo(
        centro=Ponto(x=-5.0, y=-5.0),
        raio=3
    )
    nuvem_pontos = gera_nuvem_pontos(
        numero_pontos=500,
        circulo=circulo,
    )

    circulo_heuristico, _ = usa_algoritmo_heuristico(nuvem_pontos)
    plota_circulo_envolvente(nuvem_pontos, circulo_heuristico, circulo, "Algoritmo heurístico")

    circulo_incremental_randomico, _ = usa_alogirtmo_incremental_randomico(nuvem_pontos)
    plota_circulo_envolvente(nuvem_pontos, circulo_incremental_randomico, circulo, "Algoritmo incremental randômico")