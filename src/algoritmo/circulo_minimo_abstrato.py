from abc import ABC, abstractmethod
from src.dominio import Ponto


class CirculoMinimo(ABC):
    def __init__(self, pontos: list[Ponto]):
        self.pontos = pontos

    @abstractmethod
    def determina_circulo_minimo_envolvente(self) -> tuple[Ponto, float]:
        pass