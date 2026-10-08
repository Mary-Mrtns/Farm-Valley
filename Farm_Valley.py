import random
from collections import namedtuple

print("=" * 60)
print("\nBem vindo(a) à Farm Valley!\n")
print("=" * 60)

#estruturas de dados (namedtuples) — reúnem o que antes estava espalhado em variáveis soltas
Classe = namedtuple('Classe', ['numero', 'nome', 'energia_max', 'habiliade_plantio', 'habilidade_pecuaria', 'sorte'])

PRECO_SEMENTE_CENOURA = 3
PRECO_SEMENTE_MILHO = 15
PRECO_SEMENTE_MORANGO = 8
PRECO_VENDA_CENOURA = 7
PRECO_VENDA_MILHO = 30
PRECO_VENDA_MORANGO = 14
META_CENOURA = 20           #barata e rápida
META_MILHO = 90             #cara e lenta, mas rende muito
META_MORANGO = 45           #meio-termo, com chance de colheita dupla
CHANCE_MORANGO_DOBRO = 25   #de 100, chance de render 2 ao colher
PRECO_ADUBO = 8
PRECO_VARA_PESCA = 25
PRECO_VENDA_PEIXE1 = 8
PRECO_VENDA_PEIXE2 = 18
PRECO_VENDA_PEIXE3 = 30
PRECO_FERRAMENTA = 60
PRECO_REDE = 50
PRECO_GALINHA = 35
PRECO_VACA = 80
PRECO_AJUDANTE = 100
PRECO_VENDA_OVO = 4
PRECO_VENDA_LEITE = 9
ENERGIA_CUIDAR_GALINHA = 5
ENERGIA_CUIDAR_VACA = 12
META_GALINHAS = 30          #mais fácil, junta rápido
META_VACAS = 60             #mais difícil, junta devagar

CLASSES = (
    Classe(1, "Agricultor", 100, 15, 6, 5),
    Classe(2, "Pecuarista", 120, 8, 18, 8),
    Classe(3, "Herborista", 80, 20, 8, 10),
    Classe(4, "Pescador", 90, 6, 5, 15),
)
CLASSE_PAMONHA = Classe(0, "Fazendeiro Pamonha", 70, 6, 8, 8)

