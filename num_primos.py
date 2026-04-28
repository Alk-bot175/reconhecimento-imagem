"""Módulo para verificação de números primos."""

from math import isqrt


def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        number: Número inteiro positivo a ser verificado.
        
    Returns:
        True se o número for primo, False caso contrário.
        
    Raises:
        ValueError: Se o número for negativo.
    """
    if number < 0:
        raise ValueError("Número negativo fornecido")
    
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    return _has_no_odd_divisor(number)


def _has_no_odd_divisor(number: int) -> bool:
    """Verifica se o número não possui divisores ímpares."""
    limit = isqrt(number)
    
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    
    return True


def get_primes_up_to(limit: int) -> list[int]:
    """
    Retorna todos os números primos até o limite especificado.
    
    Args:
        limit: Limite superior (inclusive).
        
    Returns:
        Lista de números primos até o limite.
    """
    return [n for n in range(2, limit + 1) if is_prime(n)]


# Testes
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 17, 18, 19, 20, 97]
    
    print("Testes de verificação de primos:")
    print("-" * 30)
    
    for num in test_cases:
        result = "primo" if is_prime(num) else "não primo"
        print(f"{num:>3} → {result}")
    
    print("-" * 30)
    print(f"Primos até 50: {get_primes_up_to(50)}")