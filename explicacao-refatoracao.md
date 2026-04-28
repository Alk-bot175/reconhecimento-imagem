# Refatoração: Estatísticas Básicas

## Código Original

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Problemas do Código Original

| Problema | Descrição |
|----------|-----------|
| Nomes incompreensíveis | `c`, `l`, `t`, `m`, `mx`, `mn`, `a`, `b`, `c2`, `d` |
| Sem type hints | Não há indicação dos tipos de dados |
| Função giant | Tudo em uma única função |
| Sem docstrings | Não há documentação |
| Loop manual | Usar `range(len())` em vez de iterar diretamente |
| Sem tratamento de erros | Não verifica lista vazia |
| Retorno confuso | Retorna tupla sem nomear campos |

---

## Código Refatorado

```python
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
```

---

## Melhorias Aplicadas

### 1. Nomes Significativos

| Antes | Depois |
|-------|--------|
| `c()` | `calcular_estatisticas()` |
| `l` | `numeros` |
| `t` | `total` |
| `m` | `media` |
| `mx` | `maximo` |
| `mn` | `minimo` |
| `x` | `numeros` |
| `a, b, c2, d` | `estatisticas.total, .media, .maximo, .minimo` |

### 2. Funções Pequenas (SRP)

Cada função agora tem **uma única responsabilidade**:

- `calcular_estatisticas()` — Coordena o cálculo
- `somar()` — Soma valores
- `calcular_media()` — Calcula média
- `encontrar_maximo()` — Encontra máximo
- `encontrar_minimo()` — Encontra mínimo

### 3. Type Hints

```python
def calcular_estatisticas(numeros: list[float]) -> Estatisticas:
def somar(numeros: list[float]) -> float:
```

### 4. NamedTuple para Retorno

```python
class Estatisticas(NamedTuple):
    total: float
    media: float
    maximo: float
    minimo: float
```

Acesso claro: `estatisticas.total`, `estatisticas.media`, etc.

### 5. Docstrings Completas

Cada função documentada com:
- Descrição
- Parâmetros
- Retorno
- Exceções

### 6. Tratamento de Erros

```python
if not numeros:
    raise ValueError("Lista vazia fornecida")
```

### 7. Built-in Functions

```python
# Antes (manual)
for i in range(len(l)):
    t = t + l[i]

# Depois (Pythonic)
return sum(numeros)
return max(numeros)
return min(numeros)
```

---

## Saída

```
Total: 346
Média: 34.60
Maior: 89
Menor: 2
```

---

## Princípios Clean Code Aplicados

| Princípio | Aplicação |
|-----------|-----------|
| **Nomes significativos** | Funções e variáveis com nomes descritivos |
| **SRP** | Cada função faz uma coisa |
| **DRY** | Lógica de soma/media/max/min reutilizável |
| **Early returns** | Verificação de lista vazia no início |
| **Type hints** | Tipagem explícita |
| **Docstrings** | Documentação completa |