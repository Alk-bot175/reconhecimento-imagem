# Explicação do Código: Verificador de Números Primos

## Visão Geral

Este módulo Python verifica se um número é primo e retorna todos os primos até um limite especificado.

---

## Código Completo

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
```

---

## Explicação Linha por Linha

### Linha 1: Docstring do Módulo

```python
"""Módulo para verificação de números primos."""
```

Descrição breve do que o arquivo faz. Usado por ferramentas de documentação.

---

### Linha 3: Importação

```python
from math import isqrt
```

Importa a função `isqrt` (integer square root) da biblioteca `math`. Retorna a parte inteira da raiz quadrada de forma precisa, sem erros de ponto flutuante.

---

### Linha 6: Definição da Função Principal

```python
def is_prime(number: int) -> bool:
```

Define a função `is_prime` que:
- Recebe um parâmetro `number` do tipo `int`
- Retorna um valor do tipo `bool` (True ou False)

---

### Linhas 7-17: Docstring

```python
    """
    Verifica se um número é primo.
    
    Args:
        number: Número inteiro positivo a ser verificado.
        
    Returns:
        True se o número for primo, False caso contrário.
        
    Raises:
        ValueError: Se o número for negativo.
    """
```

Documentação da função seguindo o padrão Google:
- **Args**: descrição do parâmetro de entrada
- **Returns**: o que a função retorna
- **Raises**: exceções que podem ser lançadas

---

### Linha 19: Validação de Número Negativo

```python
    if number < 0:
        raise ValueError("Número negativo fornecido")
```

Verifica se o número é negativo. Se for, lança uma exceção `ValueError` com mensagem explicativa.

---

### Linha 21-22: Números Menores que 2

```python
    if number < 2:
        return False
```

Por definição, números menores que 2 (0 e 1) **não são primos**. Retorna `False` imediatamente.

---

### Linha 24-25: Caso Especial do 2

```python
    if number == 2:
        return True
```

O número 2 é o **único número primo par**. Retorna `True` diretamente.

---

### Linha 27-28: Descarte de Números Pares

```python
    if number % 2 == 0:
        return False
```

Se o número for divisível por 2 (par), não é primo. Retorna `False`.

---

### Linha 30: Delegação para Função Auxiliar

```python
    return _has_no_odd_divisor(number)
```

Se chegou até aqui, o número é ímpar e maior que 2. Chama a função auxiliar para verificar divisores ímpares.

---

### Linha 33: Função Auxiliar Privada

```python
def _has_no_odd_divisor(number: int) -> bool:
```

Define função auxiliar (privada, prefixo `_`) que verifica divisores ímpares.

---

### Linha 34: Docstring

```python
    """Verifica se o número não possui divisores ímpares."""
```

Descrição simples do propósito da função.

---

### Linha 36: Cálculo do Limite

```python
    limit = isqrt(number)
```

Calcula a raiz quadrada inteira do número. Por exemplo:
- `isqrt(36)` → 6
- `isqrt(97)` → 9

**Por que até a raiz quadrada?** Se um número tem um divisor maior que sua raiz quadrada, o outro divisor必然 é menor. Então basta verificar até √n.

---

### Linha 38: Loop pelos Divisores Ímpares

```python
    for divisor in range(3, limit + 1, 2):
```

Loop que percorre números ímpares de 3 até `limit`:
- `range(3, limit + 1, 2)` gera: 3, 5, 7, 9, 11...
- O passo `2` pula números pares (já descartados)

---

### Linha 39-40: Verificação de Divisibilidade

```python
        if number % divisor == 0:
            return False
```

Se o número for divisível por qualquer divisor (resto zero), não é primo. Retorna `False` imediatamente.

---

### Linha 42: Retorno Verdadeiro

```python
    return True
```

Se o loop terminou sem encontrar divisores, o número é primo. Retorna `True`.

---

### Linha 45: Função para Listar Primos

```python
def get_primes_up_to(limit: int) -> list[int]:
```

Define função que retorna todos os primos até um limite.

---

### Linha 46-52: Docstring

```python
    """
    Retorna todos os números primos até o limite especificado.
    
    Args:
        limit: Limite superior (inclusive).
        
    Returns:
        Lista de números primos até o limite.
    """
```

Documentação da função.

---

### Linha 54: List Comprehension

```python
    return [n for n in range(2, limit + 1) if is_prime(n)]
```

Cria uma lista com todos os números de 2 até `limit` que passam no teste `is_prime()`.

---

### Linha 57: Bloco de Testes

```python
if __name__ == "__main__":
```

Garante que o código abaixo só executa quando o arquivo é rodado diretamente (não quando importado como módulo).

---

### Linha 58: Casos de Teste

```python
    test_cases = [1, 2, 3, 4, 5, 17, 18, 19, 20, 97]
```

Lista de números para testar a função.

---

### Linha 60-61: Cabeçalho

```python
    print("Testes de verificação de primos:")
    print("-" * 30)
```

Imprime cabeçalho com linha decorativa.

---

### Linha 63-65: Loop de Testes

```python
    for num in test_cases:
        result = "primo" if is_prime(num) else "não primo"
        print(f"{num:>3} → {result}")
```

Para cada número, verifica se é primo e exibe o resultado. O `:>3` alinha à direita com 3 caracteres.

---

### Linha 67-68: Teste da Função get_primes_up_to

```python
    print("-" * 30)
    print(f"Primos até 50: {get_primes_up_to(50)}")
```

Exibe todos os primos até 50.

---

## Saída Esperada

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

## Conceitos Importantes

### O que é um Número Primo?

Número natural maior que 1 que possui apenas dois divisores: 1 e ele mesmo.

Exemplos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31...

### Por que verificar até a raiz quadrada?

Se `n = a × b` e `a ≤ b`, então `a ≤ √n`. Se não existe divisor até √n, não existe divisor algum.

### Por que usar `isqrt` em vez de `n ** 0.5`?

- `n ** 0.5` usa potência de float e pode ter erros de precisão para números grandes
- `isqrt(n)` retorna resultado inteiro exato

### Por que passo 2 no loop?

Números pares já foram descartados. Verificar apenas ímpares reduz pela metade as iterações.

---

## Complexidade

| Função | Tempo | Espaço |
|--------|-------|--------|
| `is_prime(n)` | O(√n) | O(1) |
| `get_primes_up_to(n)` | O(n√n) | O(n) |

---

## Boas Práticas Aplicadas

| Princípio | Aplicação |
|-----------|-----------|
| **Nomes significativos** | `is_prime`, `_has_no_odd_divisor` |
| **Type hints** | `number: int` → `bool` |
| **Docstrings** | Documentação completa |
| **SRP** | Funções com responsabilidade única |
| **Early returns** | Retorno antecipado em casos especiais |
| **Função privada** | Prefixo `_` para funções auxiliares |
| **Tratamento de erros** | `ValueError` para entrada inválida |