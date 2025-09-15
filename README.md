# API do projeto de controlador de treinos 

Este projeto, intitulado círculo mínimo, implementa dois algoritmos utilizados para a determinação de um círculo de raio mínimo que engloba uma nuvem de pontos. A versão utilizada para desenvolvimento é Python 3.12.3.


---
## Ambientes virtuais

É fortemente recomendado a utilização de ambientes virtuais. Para tal, execute no terminal a partir de um path desejado o seguinte comando de acordo com o sistema operacional:

**WINDOWS**:
```
python -m venv env
```

**OS/LINUX**:
```
python3 -m venv env
```

Para ativação do ambiente virutal, execute o seguinte comando de acordo com a platafoma:

**WINDOWS**:
```
<path>\env\Scripts\Activate.ps1
```

**POSIX**:
```
source <path>/env/bin/activate
```

O ambiente virtual será criado.

## Instalando dependências

Todas as dependências do projeto se encontram no arquivo `requirements.txt`. A obtenção é feita a partir da execução do seguinte comando na raiz do projeto:

```
pip install -r requirements.txt
```

As dependências são instaladas.

## Recomendações de uso

Para acionar o código basta rodar da raiz do projeto

```
python main.py
```

O código realizará a determinação do círculo envolvente de raio mínimo comparando o algoritmo heurístico e o algoritmo incremental randômico. 
A nuvem de pontos é gerada a partir da instância de círculo e do número de pontos definido em:

```python
if __name__ == '__main__':
    circulo = Circulo(
        centro=Ponto(x=-5.0, y=-5.0),
        raio=3
    )
    nuvem_pontos = gera_nuvem_pontos(
        numero_pontos=500,
        circulo=circulo,
    )
```

As características dos círculos mínimos de acordo com cada algoritmo e tempo de execução são apresentadas no terminal.

```
Iniciando algoritmo heuristico
Centro: (-4.990941353095286, -5.068255927707532), Raio: 3.0756290358915166
Algoritmo heurístico finalizado para nuvem de 500 pontos em 0.0005526999884750694s


Iniciando algoritmo incremental randomico
Centro: (-4.964762255996484, -4.973848228473623), Raio: 2.996875380558187
Algoritmo incremental randômico finalizado para nuvem de 500 pontos em 0.01232829998480156s
```

Além disso, o plot de cada um dos círculos mínimos é gerado.


