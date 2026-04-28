"""Módulo para operações estatísticas básicas em listas."""

from typing import NamedTuple


class Estatisticas(NamedTuple):
    """Resultado das operações estatísticas."""
    total: float
    media: float
    maximo: float
    minimo: float


def calcular_estatisticas(numeros: list[float]) -> Estatisticas:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros: Lista de números para análise.
        
    Returns:
        NamedTuple contendo total, média, máximo e mínimo.
        
    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("Lista vazia fornecida")
    
    total = somar(numeros)
    media = calcular_media(total, len(numeros))
    maximo = encontrar_maximo(numeros)
    minimo = encontrar_minimo(numeros)
    
    return Estatisticas(total=total, media=media, maximo=maximo, minimo=minimo)


def somar(numeros: list[float]) -> float:
    """Soma todos os números da lista."""
    return sum(numeros)


def calcular_media(total: float, quantidade: int) -> float:
    """Calcula a média aritmética."""
    return total / quantidade


def encontrar_maximo(numeros: list[float]) -> float:
    """Encontra o maior valor da lista."""
    return max(numeros)


def encontrar_minimo(numeros: list[float]) -> float:
    """Encontra o menor valor da lista."""
    return min(numeros)


# Testes
if __name__ == "__main__":
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    estatisticas = calcular_estatisticas(numeros)
    
    print(f"Total: {estatisticas.total}")
    print(f"Média: {estatisticas.media:.2f}")
    print(f"Maior: {estatisticas.maximo}")
    print(f"Menor: {estatisticas.minimo}")