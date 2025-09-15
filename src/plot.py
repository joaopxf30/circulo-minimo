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

    plt.show()