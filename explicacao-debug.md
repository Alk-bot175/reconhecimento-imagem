# Explicação do Código: Refatoração de Estatísticas

## Código Original (Sem Refatoração)

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

---

## Explicação Linha por Linha

### Linha 1: Definição da Função

```python
def c(l):
```

- `def` → palavra-chave para definir função
- `c` → nome da função (muito curto, não descritivo)
- `(l)` → parâmetro (lista de números)

**Problema:** Nome `c` não diz nada sobre o que a função faz. Parâmetro `l` também não é descritivo.

---

### Linha 2: Inicialização do Total

```python
    t=0
```

- Inicializa variável `t` (total) com zero
- Será usada para acumular a soma de todos os elementos

---

### Linha 3-4: Loop para Somar Elementos

```python
    for i in range(len(l)):
        t=t+l[i]
```

- `range(len(l))` → gera índices de 0 até len(l)-1
- `len(l)` → quantidade de elementos na lista
- `l[i]` → acessa o elemento na posição i
- `t = t + l[i]` → soma cada elemento ao total

**Equivalente a:** `t = sum(l)`

---

### Linha 5: Cálculo da Média

```python
    m=t/len(l)
```

- Divide o total pela quantidade de elementos
- `m` = média aritmética

---

### Linha 6-7: Inicialização de Máximo e Mínimo

```python
    mx=l[0]
    mn=l[0]
```

- `mx` → variável para armazenar o maior valor
- `mn` → variável para armazenar o menor valor
- Inicializa ambos com o primeiro elemento da lista (`l[0]`)

---

### Linha 8-12: Loop para Encontrar Máximo e Mínimo

```python
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
```

- Percorre todos os elementos da lista
- Se `l[i]` > `mx` → atualiza o máximo
- Se `l[i]` < `mn` → atualiza o mínimo

**Equivalente a:** `mx = max(l)` e `mn = min(l)`

---

### Linha 13: Retorno da Função

```python
    return t,m,mx,mn
```

- Retorna 4 valores em uma tupla:
  1. `t` → total
  2. `m` → média
  3. `mx` → máximo
  4. `mn` → mínimo

---

### Linha 15: Definição da Lista de Teste

```python
x=[23,7,45,2,67,12,89,34,56,11]
```

- Lista com 10 números para testar a função

---

### Linha 16: Chamada da Função

```python
a,b,c2,d=c(x)
```

- Chama a função `c` passando a lista `x`
- Desempacota o retorno em 4 variáveis:
  - `a` → total
  - `b` → média
  - `c2` → máximo
  - `d` → mínimo

**Problema:** Variáveis `a`, `b`, `c2`, `d` não são descritivas.

---

### Linha 17-20: Impressão dos Resultados

```python
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

- Imprime cada resultado com um rótulo

---

## Fluxo de Execução

```
Entrada: lista [23,7,45,2,67,12,89,34,56,11]
         │
         ▼
┌────────────────────┐
│ 1. Soma elementos │
│    23+7+45+2+67+12 │
│    +89+34+56+11    │
│    = 346           │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 2. Calcula média   │
│    346 / 10 = 34.6 │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 3. Encontra máximo │
│    89              │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 4. Encontra mínimo │
│    2               │
└─────────┬──────────┘
          ▼
Saída: (346, 34.6, 89, 2)
```

---

## Problemas do Código

| Problema | Descrição |
|----------|-----------|
| **Nomes incompreensíveis** | `c`, `l`, `t`, `m`, `mx`, `mn`, `a`, `b`, `c2`, `d` |
| **Sem type hints** | Não indica os tipos de dados |
| **Sem docstrings** | Não há documentação |
| **Loop manual** | Usa `range(len())` em vez de funções built-in |
| **Função giant** | Tudo em uma única função |
| **Retorno confuso** | Tupla sem campos nomeados |

---

## Saída do Programa

```
total: 346
media: 34.6
maior: 89
menor: 2
```

---

## Versão Refatorada (Sugestão)

```python
from typing import NamedTuple

class Estatisticas(NamedTuple):
    total: float
    media: float
    maximo: float
    minimo: float

def calcular_estatisticas(numeros: list[float]) -> Estatisticas:
    if not numeros:
        raise ValueError("Lista vazia")
    
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return Estatisticas(total=total, media=media, maximo=maximo, minimo=minimo)

# Uso
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
resultado = calcular_estatisticas(numeros)

print(f"Total: {resultado.total}")
print(f"Média: {resultado.media:.2f}")
print(f"Maior: {resultado.maximo}")
print(f"Menor: {resultado.minimo}")
```