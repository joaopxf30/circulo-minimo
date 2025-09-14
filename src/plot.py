import matplotlib.pyplot as plt
from src.dominio import Ponto, Circulo
from matplotlib.patches import Circle


def plota_circulo_envolvente(pontos: list[Ponto], circulo_minimo: Circulo, circulo: Circulo, titulo: str):
    coords_x = [ponto.coord_x for ponto in pontos]
    coords_y = [ponto.coord_y for ponto in pontos]

    fig, ax = plt.subplots()
    ax.plot(coords_x, coords_y, "x", color="blue")
    ax.plot(circulo_minimo.centro.coord_x, circulo_minimo.centro.coord_y, "o", color="red")

    circulo_plot = Circle(
        xy=(circulo_minimo.centro.coord_x, circulo_minimo.centro.coord_y),
        radius=circulo.raio,
        color="red",
        fill=False,
        linewidth=1
    )
    ax.add_patch(circulo_plot)

    ax.set_title(titulo,fontsize=12)
    ax.set_xlabel("x",fontsize=12)
    ax.set_ylabel("y",fontsize=12)

    xlim_inferior = circulo.centro.coord_x - circulo.raio - 0.25
    xlim_superior = circulo.centro.coord_x + circulo.raio + 0.25
    ylim_inferior = circulo.centro.coord_y - circulo.raio - 0.25
    ylim_superior = circulo.centro.coord_y + circulo.raio + 0.25

    ax.set_xlim(xlim_inferior, xlim_superior)
    ax.set_ylim(ylim_inferior, ylim_superior)
    ax.set_aspect("equal")

    fig.savefig(
        f"circulo_envolvente_{titulo}.pdf",
        format="pdf",
        bbox_inches="tight",
        pad_inches=0,
        transparent=True
    )

    plt.show()


def plota_tempo_execucao_algoritmos(
    numeros_pontos: list[int],
    tempos_execucao_heuristico: list[int],
    tempos_execucao_incremental_randomico_medio: list[int],
    tempos_incremental_randomico: list[list[int]]
):
    fig, ax = plt.subplots()

    for i, tempos in enumerate(tempos_incremental_randomico):
        ax.scatter([numeros_pontos[i]] * len(tempos), tempos, marker='s', color='gray', alpha=0.3)

    ax.plot(numeros_pontos, tempos_execucao_heuristico, marker='o', label="Algoritmo Heuristico")
    ax.plot(numeros_pontos, tempos_execucao_incremental_randomico_medio, marker='s', label="Algoritmo Incremental Randomico")

    ax.grid(True)

    ax.set_title("Análise do limite superior assintótico",fontsize=12)
    ax.set_xlabel("n",fontsize=12)
    ax.set_ylabel("Tempo de execução (s)",fontsize=12)

    fig.savefig(
        f"analise_assintotica_media.pdf",
        format="pdf",
        bbox_inches="tight",
        pad_inches=0,
        transparent=True
    )

    plt.show()