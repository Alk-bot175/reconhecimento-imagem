#                                      CÓDIGO COM ANOTAÇÕES
# =============================================================================
# Sistema de Calculadora de Compras com Desconto e Imposto
# =============================================================================

# -----------------------------------------------------------------------------
# ENTRADA DE DADOS
# -----------------------------------------------------------------------------

# Pede o nome do cliente (input sempre retorna string)
cliente = input("Qual é seu nome? ")

# Item 1: quantidade (int) e preço (float)
qtd1 = int(input("Quantidade do item 1: "))          # Converte para inteiro
item1 = float(input("Preço do item 1? "))             # Converte para decimal

# Item 2: quantidade (int) e preço (float)
qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

# Item 3: quantidade (int) e preço (float)
qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# -----------------------------------------------------------------------------
# CÁLCULOS DOS ITENS
# -----------------------------------------------------------------------------

# Calcula o total de cada item (quantidade × preço)
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# Calcula o subtotal (soma dos totais dos itens)
subtotal = total_item1 + total_item2 + total_item3

# Calcula o imposto (10% sobre o subtotal)
imposto = subtotal * 0.10

# -----------------------------------------------------------------------------
# DESCONTO
# -----------------------------------------------------------------------------

# Pede o percentual de desconto e converte para float
# Exemplo: se digitar 15, significa 15% de desconto
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

# Calcula o valor do desconto: subtotal × percentual / 100
# Exemplo: 100 × 15 / 100 = 15 (15% de 100)
desconto = subtotal * (desconto_cupom / 100)

# -----------------------------------------------------------------------------
# TOTAL FINAL
# -----------------------------------------------------------------------------

# Total = subtotal + imposto - desconto
total = subtotal + imposto - desconto

# -----------------------------------------------------------------------------
# EXIBIÇÃO (RECIBO)
# -----------------------------------------------------------------------------

# Cria linhas decorativas para o recibo
# "=" * 31 cria uma string com 31 sinais de igual
linha = "=" * 31
separador = "-" * 31

# Imprime o cabeçalho
print(linha)
print(f" Cliente: {cliente}")  # f-string insere a variável {cliente}
print(linha)

# Imprime cada item com formatação de moeda (R$ com 2 casas decimais)
# :.2f formata para 2 casas decimais (ex: 100.00)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")

# Imprime subtotal e imposto
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Se houver desconto (percentual maior que 0), exibe o valor
# .0f formata sem casas decimais (ex: 15%)
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

# Imprime o total final com bordas
print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")  # round arredonda para 2 casas
print(linha)