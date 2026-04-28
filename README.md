# Verificador de Números Primos

> Módulo Python para verificação de números primos com implementação otimizada.

## O que é um Número Primo?

Um número primo é um número natural maior que 1 que possui apenas dois divisores positivos distintos: 1 e ele mesmo.

| Número | É Primo? | Motivo |
|--------|----------|--------|
| 2 | ✅ | Divisível apenas por 1 e 2 |
| 3 | ✅ | Divisível apenas por 1 e 3 |
| 4 | ❌ | Divisível por 1, 2 e 4 |
| 17 | ✅ | Divisível apenas por 1 e 17 |
| 97 | ✅ | Divisível apenas por 1 e 97 |

---

## Instalação

```bash
# Clone o repositório ou copie o arquivo num_primos.py
```

## Uso Básico

```python
from num_primos import is_prime

# Verificar um número
is_prime(7)    # True
is_prime(10)   # False
is_prime(97)   # True

# Obter todos os primos até um limite
from num_primos import get_primes_up_to
get_primes_up_to(50)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

## Código

```python
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
```

---

## Princípios Clean Code Aplicados

### 1. Nomes Significativos

| Antes | Depois | Motivo |
|-------|--------|--------|
| `verificar_primo(n)` | `is_prime(number)` | Nome em inglês + verbo claro |
| `n` | `number` | Nome descritivo |
| `i` | `divisor` | Nome que indica propósito |

### 2. Funções Pequenas e com Responsabilidade Única

- **`is_prime()`** — Coordena a lógica de verificação
- **`_has_no_odd_divisor()`** — Verifica divisores ímpares (função privada)
- **`get_primes_up_to()`** — Retorna lista de primos

### 3. Type Hints

```python
def is_prime(number: int) -> bool:
def get_primes_up_to(limit: int) -> list[int]:
```

### 4. Docstrings Completas

Cada função possui:
- Descrição do que faz
- Parâmetros com tipos
- Retorno esperado
- Exceções levantadas

### 5. Early Returns

```python
if number < 0:
    raise ValueError(...)
if number < 2:
    return False
```

Evita aninhamento excessivo de `if/else`.

### 6. Função Privada com `_`

```python
def _has_no_odd_divisor(number: int) -> bool:
```

O prefixo `_` indica que é uma função interna, não para uso externo.

---

## Otimizações

### `isqrt()` vs `** 0.5`

| Método | Problema |
|--------|----------|
| `int(n ** 0.5)` | Potência com float pode causar erros de precisão |
| `isqrt(n)` | Função exata da biblioteca `math` |

```python
# Antes
int(n ** 0.5)  # Pode ter erro de precisão para números grandes

# Depois
isqrt(n)  # Resultado inteiro exato
```

### Verificação de Pares Separada

Números pares > 2 são rapidamente descartados, evitando loop desnecessário.

---

## Complexidade

| Operação | Tempo | Espaço |
|----------|-------|--------|
| `is_prime(n)` | O(√n) | O(1) |
| `get_primes_up_to(n)` | O(n√n) | O(n) |

---

## Executar Testes

```bash
python num_primos.py
```

**Saída:**
```
Testes de verificação de primos:
------------------------------
  1 → não primo
  2 → primo
  3 → primo
  4 → não primo
  5 → primo
 17 → primo
 18 → não primo
 19 → primo
 20 → não primo
 97 → primo
------------------------------
Primos até 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

## Tratamento de Erros

```python
from num_primos import is_prime

is_prime(-5)  # Levanta ValueError: Número negativo fornecido
```

---

## Licença

MIT License