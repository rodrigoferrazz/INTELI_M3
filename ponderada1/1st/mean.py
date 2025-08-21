import numpy as np

def calculate(list):
    # É necessário criar essa condicional para garantir que a lista tenha exatamente 9 números
    ## Tentei criar essa condicional apenas na área de test mas não deu certo
    if len(list) != 9:
        raise ValueError("A lista esta pequena, deve conter nove números.")

    # Criando a matriz 3x3
    matriz = np.array(list).reshape(3, 3)

    # Criando o dicionário
    calculations = {
        'mean': [
            matriz.mean(axis=0).tolist(),   # média das colunas
            matriz.mean(axis=1).tolist(),   # média das linhas 
            matriz.mean().item()            # média geral
        ],
        'variance': [
            matriz.var(axis=0).tolist(),
            matriz.var(axis=1).tolist(),
            matriz.var().item()
        ],
        'standard deviation': [
            matriz.std(axis=0).tolist(),
            matriz.std(axis=1).tolist(),
            matriz.std().item()
        ],
        'max': [
            matriz.max(axis=0).tolist(),
            matriz.max(axis=1).tolist(),
            matriz.max().item()
        ],
        'min': [
            matriz.min(axis=0).tolist(),
            matriz.min(axis=1).tolist(),
            matriz.min().item()
        ],
        'sum': [
            matriz.sum(axis=0).tolist(),
            matriz.sum(axis=1).tolist(),
            matriz.sum().item()
        ]
    }

    return calculations
