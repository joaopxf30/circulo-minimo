import time
from src.algoritmo.heuristico import Heuristico
from src.algoritmo.incremental_randomico import IncrementalRandomico
from src.dominio import Ponto, Circulo
from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_circulo_envolvente


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
    print(f"Algoritmo incremental randômico finalizado para nuvem de {len(pontos)} pontos em {tempo_execucao}s\n")
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