import random
from collections import namedtuple

print("=" * 60)
print("\nBem vindo(a) à Farm Valley!\n")
print("=" * 60)

#estruturas de dados (namedtuples) — reúnem o que antes estava espalhado em variáveis soltas

Classe = namedtuple('Classe', ['numero', 'nome', 'energia_max', 'habilidade_plantio', 'habilidade_pecuaria', 'sorte'])

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
META_GALINHAS = 30        #mais fácil, junta rápido
META_VACAS = 60           #mais difícil, junta devagar

CLASSES = (
    Classe(1, "Agricultor", 100, 15, 6, 5),
    Classe(2, "Pecuarista", 120, 8, 18, 8),
    Classe(3, "Herborista", 80, 20, 8, 10),
    Classe(4, "Pescador", 90, 6, 5, 15),
)
CLASSE_PAMONHA = Classe(0, "Fazendeiro Pamonha", 70, 6, 8, 8)


Cultivo = namedtuple('Cultivo', ['nome', 'artigo', 'pronome', 'possessivo', 'chance_dobro', 'preco_semente', 'meta', 'preco_venda'])
CULTIVOS = (
    Cultivo("Cenoura", "uma", "dela", "Sua", 0, PRECO_SEMENTE_CENOURA, META_CENOURA, PRECO_VENDA_CENOURA),
    Cultivo("Milho", "um", "dele", "Seu", 0, PRECO_SEMENTE_MILHO, META_MILHO, PRECO_VENDA_MILHO),
    Cultivo("Morango", "um", "dele", "Seu", CHANCE_MORANGO_DOBRO, PRECO_SEMENTE_MORANGO, META_MORANGO, PRECO_VENDA_MORANGO),
)

Peixe = namedtuple('Peixe', ['nome', 'preco_venda'])
PEIXES = (
    Peixe("N1", PRECO_VENDA_PEIXE1),
    Peixe("N2", PRECO_VENDA_PEIXE2),
    Peixe("N3", PRECO_VENDA_PEIXE3),
)

#Animal: nome | nome_plural | preco de compra | energia por cuidado | meta de progresso
#divisor_habilidade (quanto maior, mais devagar cresce o progresso) | rotulo do produto ("ovo(s)")
#rotulo total ("ovos") | verbo da coleta ("coletou"/"tirou") | preço de venda do produto
Animal = namedtuple('Animal', ['nome', 'nome_plural', 'preco', 'energia_cuidado', 'meta',
                                 'divisor_habilidade', 'produto_rotulo', 'produto_total_label',
                                 'verbo_coleta', 'preco_venda_produto'])
ANIMAIS = (
    Animal("galinha", "galinhas", PRECO_GALINHA, ENERGIA_CUIDAR_GALINHA, META_GALINHAS, 1,
           "ovo(s)", "ovos", "coletou", PRECO_VENDA_OVO),
    Animal("vaca", "vacas", PRECO_VACA, ENERGIA_CUIDAR_VACA, META_VACAS, 2,
           "leite(s)", "leite", "tirou", PRECO_VENDA_LEITE),
)


#funções reutilizáveis

def comprar(moedas, preco):
    """Tenta comprar algo. Retorna uma tupla (sucesso, novo_saldo_de_moedas)."""
    if moedas >= preco:
        return True, moedas - preco
    return False, moedas


def vender(quantidades, precos):
    """Calcula a venda de um conjunto de itens. Retorna (total_de_itens, ganho_em_moedas)."""
    total = sum(quantidades)
    ganho = sum(quantidade * preco for quantidade, preco in zip(quantidades, precos))
    return total, ganho


def formatar_itens_vendidos(rotulos, quantidades):
    """Monta o texto 'X item1, Y item2 e Z item3' a partir de listas paralelas."""
    partes = [f"{quantidade} {rotulo}" for rotulo, quantidade in zip(rotulos, quantidades)]
    if len(partes) == 1:
        return partes[0]
    return ", ".join(partes[:-1]) + " e " + partes[-1]


def zerar(lista):
    """Zera todos os valores de uma lista (usada para zerar estoques após a venda)."""
    for i in range(len(lista)):
        lista[i] = 0


#criação do personagem

jogador = input("Digite o seu nome fazendeiro(a): ")
print(f"\nOlá {jogador}! Qual o seu tipo de fazendeiro(a)?\n")
print(" | ".join(f"{classe.numero} - {classe.nome}" for classe in CLASSES))
tipo_jogador = input("Escolha: ")

try:
    tipo_jogador = int(tipo_jogador)
    classe_escolhida = None
    for classe in CLASSES:
        if classe.numero == tipo_jogador:
            classe_escolhida = classe
            break
    if classe_escolhida is None:
        print(f"Parabéns {jogador}! Não escolheu corretamente e virou um Fazendeiro Pamonha!")
        classe_escolhida = CLASSE_PAMONHA
except:
    print("Valor indevido! Encerrando o jogo.")
    exit()

nome_tipo, energia_max, habilidade_plantio, habilidade_pecuaria, sorte = (
    classe_escolhida.nome,
    classe_escolhida.energia_max,
    classe_escolhida.habilidade_plantio,
    classe_escolhida.habilidade_pecuaria,
    classe_escolhida.sorte,
)

print(f"\nFicha criada para: {jogador}")
print(f"Tipo: {nome_tipo}")
print(f"Energia Máxima: {energia_max}")
print(f"Habilidade de Plantio: {habilidade_plantio}")
print(f"Habilidade de Pecuária: {habilidade_pecuaria}")
print(f"Sorte: {sorte}")

energia_atual = energia_max

#recursos do jogador
moedas = 30
sementes = [1, 0, 0]          #índice 0 = Cenoura, 1 = Milho, 2 = Morango (igual a CULTIVOS)
adubo = 0
estoque_cultivo = [0, 0, 0]    #mesma ordem de CULTIVOS
vara_pesca = 0                 #precisa comprar na loja antes de pescar
estoque_peixe = [0, 0, 0]      #mesma ordem de PEIXES (N1, N2, N3)

#upgrades e investimentos
ferramenta_melhorada = 0   #0 = não comprou | 1 = comprou (upgrade único)
rede_reforcada = 0         #0 = não comprou | 1 = comprou (upgrade único)
ajudante = 0                #0 = não contratou | 1 = contratou (upgrade único)
quantidade_animal = [0, 0]   #mesma ordem de ANIMAIS (galinha, vaca)
progresso_animal = [0, 0]
estoque_animal = [0, 0]       #ovos, leite

#estado da plantação
plantado = 0
plantado_tipo = 0      #0 = nada | 1 = cenoura | 2 = milho | 3 = morango (índice em CULTIVOS + 1)
saude_plantacao = 0

print(f"\n{jogador}, bem-vindo(a) à sua fazenda! Cuide da terra, compre na loja, pesque peixes, venda suas colheitas e peixes")

#loop principal
while energia_atual > 0:
    print("=" * 50)
    print(f"   FARM VALLEY — {jogador} ({nome_tipo})")
    print("=" * 50)

    if plantado_tipo > 0:
        meta_atual = CULTIVOS[plantado_tipo - 1].meta
        nome_cultivo = CULTIVOS[plantado_tipo - 1].nome
    else:
        meta_atual = 0
        nome_cultivo = "Nenhuma"

    print("\n--- STATUS ---")
    print(f"Energia: {energia_atual}/{energia_max}")
    if plantado == 1:
        print(f"Plantação ({nome_cultivo}): {saude_plantacao}/{meta_atual}")
    else:
        print("Plantação: nenhuma planta ativa")

    print("\n--- RECURSOS ---")
    print(f"Moedas: {moedas} | Adubo: {adubo}")
    print("Sementes -> " + " | ".join(f"{CULTIVOS[i].nome}: {sementes[i]}" for i in range(len(CULTIVOS))))
    print("Colheitas -> " + " | ".join(f"{CULTIVOS[i].nome}: {estoque_cultivo[i]}" for i in range(len(CULTIVOS))))
    print(f"Vara de pesca: {vara_pesca}")
    print("Peixes -> " + " | ".join(f"{PEIXES[i].nome}: {estoque_peixe[i]}" for i in range(len(PEIXES))))
    print(" | ".join(f"{ANIMAIS[i].nome_plural.capitalize()}: {quantidade_animal[i]}" for i in range(len(ANIMAIS)))
          + f" | Ajudante: {'Sim' if ajudante == 1 else 'Não'}")
    print(" | ".join(f"{ANIMAIS[i].produto_total_label.capitalize()}: {estoque_animal[i]}" for i in range(len(ANIMAIS))))
    for i, animal in enumerate(ANIMAIS):
        if quantidade_animal[i] > 0:
            print(f"Progresso {animal.nome_plural}: {progresso_animal[i]}/{animal.meta}")

    print("\n--- AÇÕES ---")
    print("1-Loja | 2-Plantar | 3-Regar | 4-Adubar | 5-Pescar | 6-Cuidar animais | 7-Descansar | 8-Sair")
    print("-" * 50)

    try:
        acao = int(input("Escolha uma ação: "))
    except:
        print("Entrada inválida! Tente novamente.")
        continue

    #loja
    if acao == 1:
        while True:
            print(f"\n FARM VALLEY LOJA (Moedas: {moedas})")
            print("1 -   Comprar semente (" + " | ".join(f"{c.nome}: {c.preco_semente}" for c in CULTIVOS) + " moedas)")
            print(f"2 -  Comprar adubo ({PRECO_ADUBO} moedas)")
            print(f"3 -  Comprar vara de pesca ({PRECO_VARA_PESCA} moedas)")
            print("4 -   Vender colheitas (" + " | ".join(f"{c.nome}: {c.preco_venda}" for c in CULTIVOS) + " moedas)")
            print("5 -   Vender peixes (" + " | ".join(f"{p.nome}: {p.preco_venda}" for p in PEIXES) + " moedas)")
            print(f"6 -  Ferramenta melhorada ({PRECO_FERRAMENTA} moedas, upgrade único, +5 habilidade de plantio)")
            print(f"7 -  Rede reforçada ({PRECO_REDE} moedas, upgrade único, reduz risco de perder a vara)")
            print(f"8 -  Comprar galinha ({ANIMAIS[0].preco} moedas, precisa cuidar para gerar ovos)")
            print(f"9 -  Comprar vaca ({ANIMAIS[1].preco} moedas, precisa cuidar para gerar leite)")
            print(f"10 - Contratar ajudante ({PRECO_AJUDANTE} moedas, upgrade único, rega a plantação sozinho)")
            print(f"11 - Vender ovos e leite (Ovo: {ANIMAIS[0].preco_venda_produto} | Leite: {ANIMAIS[1].preco_venda_produto} moedas)")
            print("12 -  Voltar para a fazenda")

            try:
                escolha_loja = int(input("O que deseja fazer? "))
            except:
                print("Entrada inválida!")
                continue

            if escolha_loja == 1:
                print(" | ".join(f"{i + 1} - {c.nome}" for i, c in enumerate(CULTIVOS)))
                try:
                    escolha_semente = int(input("Qual semente comprar? "))
                except:
                    print("Entrada inválida!")
                    escolha_semente = 0

                indice_semente = escolha_semente - 1
                if 0 <= indice_semente < len(CULTIVOS):
                    cultivo = CULTIVOS[indice_semente]
                    sucesso, moedas = comprar(moedas, cultivo.preco_semente)
                    if sucesso:
                        sementes[indice_semente] = sementes[indice_semente] + 1
                        print(f"Você comprou 1 semente de {cultivo.nome.lower()}! Total: {sementes[indice_semente]} | Moedas: {moedas}")
                    else:
                        print(f"Moedas insuficientes para comprar semente de {cultivo.nome.lower()}!")
                else:
                    print("Opção de semente inválida!")

            elif escolha_loja == 2:
                sucesso, moedas = comprar(moedas, PRECO_ADUBO)
                if sucesso:
                    adubo = adubo + 1
                    print("Você comprou 1 adubo!")
                    print(f"Adubo: {adubo} | Moedas: {moedas}")
                else:
                    print("Moedas insuficientes para comprar adubo!")

            elif escolha_loja == 3:
                sucesso, moedas = comprar(moedas, PRECO_VARA_PESCA)
                if sucesso:
                    vara_pesca = vara_pesca + 1
                    print("Você comprou 1 vara de pesca!")
                    print(f"Varas: {vara_pesca} | Moedas: {moedas}")
                else:
                    print("Moedas insuficientes para comprar vara de pesca!")

            elif escolha_loja == 4:
                total_colheitas, ganho_colheita = vender(estoque_cultivo, [c.preco_venda for c in CULTIVOS])
                if total_colheitas > 0:
                    rotulos_colheita = [f"{c.nome.lower()}(s)" for c in CULTIVOS]
                    print(f"Você vendeu {formatar_itens_vendidos(rotulos_colheita, estoque_cultivo)} por {ganho_colheita} moedas!")
                    moedas = moedas + ganho_colheita
                    zerar(estoque_cultivo)
                else:
                    print("Você não tem colheitas para vender!")

            elif escolha_loja == 5:
                total_peixes, ganho_peixe = vender(estoque_peixe, [p.preco_venda for p in PEIXES])
                if total_peixes > 0:
                    print(f"Você vendeu {total_peixes} peixe(s) por {ganho_peixe} moedas!")
                    zerar(estoque_peixe)
                else:
                    print(" Você não tem peixes para vender!")

            elif escolha_loja == 6:
                if ferramenta_melhorada == 1:
                    print("Você já tem a ferramenta melhorada!")
                else:
                    sucesso, moedas = comprar(moedas, PRECO_FERRAMENTA)
                    if sucesso:
                        ferramenta_melhorada = 1
                        habilidade_plantio = habilidade_plantio + 5
                        print(f"Ferramenta melhorada comprada! Habilidade de plantio agora é {habilidade_plantio}!")
                    else:
                        print("Moedas insuficientes para comprar a ferramenta melhorada!")

            elif escolha_loja == 7:
                if rede_reforcada == 1:
                    print("Você já tem a rede reforçada!")
                else:
                    sucesso, moedas = comprar(moedas, PRECO_REDE)
                    if sucesso:
                        rede_reforcada = 1
                        print("Rede reforçada comprada! Agora você perde a vara com menos frequência.")
                    else:
                        print("Moedas insuficientes para comprar a rede reforçada!")

            elif escolha_loja == 8:
                sucesso, moedas = comprar(moedas, ANIMAIS[0].preco)
                if sucesso:
                    quantidade_animal[0] = quantidade_animal[0] + 1
                    print(f"Você comprou 1 galinha! Total de galinhas: {quantidade_animal[0]}")
                else:
                    print("Moedas insuficientes para comprar a galinha!")

            elif escolha_loja == 9:
                sucesso, moedas = comprar(moedas, ANIMAIS[1].preco)
                if sucesso:
                    quantidade_animal[1] = quantidade_animal[1] + 1
                    print(f"Você comprou 1 vaca! Total de vacas: {quantidade_animal[1]}")
                else:
                    print("Moedas insuficientes para comprar a vaca!")

            elif escolha_loja == 10:
                if ajudante == 1:
                    print("Você já tem um ajudante contratado!")
                else:
                    sucesso, moedas = comprar(moedas, PRECO_AJUDANTE)
                    if sucesso:
                        ajudante = 1
                        print("Ajudante contratado! Ele vai cuidar da plantação automaticamente a cada rodada.")
                    else:
                        print("Moedas insuficientes para contratar o ajudante!")

            elif escolha_loja == 11:
                total_produtos, ganho_produtos = vender(estoque_animal, [a.preco_venda_produto for a in ANIMAIS])
                if total_produtos > 0:
                    rotulos_produtos = [a.produto_rotulo for a in ANIMAIS]
                    print(f"Você vendeu {formatar_itens_vendidos(rotulos_produtos, estoque_animal)} por {ganho_produtos} moedas!")
                    moedas = moedas + ganho_produtos
                    zerar(estoque_animal)
                else:
                    print("Você não tem ovos ou leite para vender!")

            elif escolha_loja == 12:
                print("Voltando para a fazenda...")
                break
            else:
                print("Opção inválida")

    #plantar
    elif acao == 2:
        if plantado == 1:
            print("Você já tem uma planta crescendo! Cuide dela antes de plantar outra.")
        else:
            print(" | ".join(f"{i + 1} - {c.nome}" for i, c in enumerate(CULTIVOS)))
            try:
                escolha_plantio = int(input("O que deseja plantar? "))
            except:
                print("Entrada inválida!")
                escolha_plantio = 0

            indice_plantio = escolha_plantio - 1
            if 0 <= indice_plantio < len(CULTIVOS):
                cultivo = CULTIVOS[indice_plantio]
                if sementes[indice_plantio] <= 0:
                    print(f"Você não tem sementes de {cultivo.nome.lower()}! Vá até a loja para comprar.")
                else:
                    sementes[indice_plantio] = sementes[indice_plantio] - 1
                    plantado = 1
                    plantado_tipo = indice_plantio + 1
                    saude_plantacao = 0
                    print(f"Você plantou {cultivo.artigo} {cultivo.nome.lower()}, agora cuide {cultivo.pronome}!")
            else:
                print("Opção de plantio inválida!")

    #regar
    elif acao == 3:
        if plantado == 0:
            print("Não há nada plantado para regar!")
        elif energia_atual < 10:
            print("Energia insuficiente para regar!")
        else:
            saude_plantacao = saude_plantacao + habilidade_plantio
            energia_atual = energia_atual - 10

            evento = random.randint(1, 10)
            if evento <= 3:
                print("Choveu! A plantação cresceu um pouco mais!")
                saude_plantacao += 5
            elif evento >= 9:
                print("Oh não, uma praga apareceu e atrapalhou o crescimento!")
                saude_plantacao -= 8

            if saude_plantacao < 0:
                saude_plantacao = 0

            print(f"Energia atual: {energia_atual} | Saúde da plantação: {saude_plantacao}/{meta_atual}")

    #adubar
    elif acao == 4:
        if plantado == 0:
            print("Não há nada plantado para adubar!")
        elif adubo <= 0:
            print("Você não tem adubo! Vá até a loja para comprar.")
        elif energia_atual < 15:
            print("Energia insuficiente para adubar! Descanse!")
        else:
            adubo = adubo - 1
            saude_plantacao = saude_plantacao + (habilidade_plantio // 2) + sorte
            energia_atual = energia_atual - 15
            print(f"Você adubou a terra! Adubo restante: {adubo} | Saúde da plantação: {saude_plantacao}/{meta_atual}")

    #pescar
    elif acao == 5:
        if vara_pesca <= 0:
            print("Você não tem vara de pesca! Vá até a loja para comprar.")
        elif energia_atual < 12:
            print("Energia insuficiente para pescar! Descanse!")
        else:
            energia_atual = energia_atual - 12
            resultado = random.randint(1, 20) + sorte

            if resultado >= 25:
                estoque_peixe[2] = estoque_peixe[2] + 1
                print(f"Uau!! Você fisgou um peixe raro (nível 3)! Total N3: {estoque_peixe[2]}")
            elif resultado >= 15:
                estoque_peixe[1] = estoque_peixe[1] + 1
                print(f"Você pescou um peixe bom (nível 2)! Total N2: {estoque_peixe[1]}")
            elif resultado >= 8:
                estoque_peixe[0] = estoque_peixe[0] + 1
                print(f"Você pescou um peixe comum (nível 1)! Total N1: {estoque_peixe[0]}")
            else:
                print("Nada mordeu o anzol dessa vez...")

            risco_perder = 20 - sorte
            if rede_reforcada == 1:
                risco_perder = risco_perder - 8
            if risco_perder < 0:
                risco_perder = 0
            chance_perder = random.randint(1, 100)
            if chance_perder <= risco_perder:
                vara_pesca = vara_pesca - 1
                print(f"Opss! Sua linha arrebentou e você perdeu a vara de pesca! Varas restante: {vara_pesca}")

            print(f"Energia atual: {energia_atual}")

    #cuidar dos animais
    elif acao == 6:
        if quantidade_animal[0] == 0 and quantidade_animal[1] == 0:
            print("Você não tem nenhum animal! Vá até a loja para comprar galinhas ou vacas.")
        else:
            custo_energia = 0
            for i, animal in enumerate(ANIMAIS):
                if quantidade_animal[i] > 0:
                    custo_energia = custo_energia + animal.energia_cuidado

            if energia_atual < custo_energia:
                print("Energia insuficiente para cuidar dos animais! Descanse!")
            else:
                energia_atual = energia_atual - custo_energia

                for i, animal in enumerate(ANIMAIS):
                    if quantidade_animal[i] > 0:
                        progresso_animal[i] = progresso_animal[i] + (habilidade_pecuaria // animal.divisor_habilidade)
                        print(f"Você cuidou das {animal.nome_plural}! Progresso: {progresso_animal[i]}/{animal.meta}")

                print(f"Energia atual: {energia_atual}")

                for i, animal in enumerate(ANIMAIS):
                    if progresso_animal[i] >= animal.meta:
                        estoque_animal[i] = estoque_animal[i] + quantidade_animal[i]
                        progresso_animal[i] = 0
                        print(f"As {animal.nome_plural} estão prontas! Você {animal.verbo_coleta} {quantidade_animal[i]} {animal.produto_rotulo}. Total de {animal.produto_total_label}: {estoque_animal[i]}")

    #descansar
    elif acao == 7:
        chance = random.randint(1, 10)
        if chance > 3:
            energia_atual = energia_atual + 20
            if energia_atual > energia_max:
                energia_atual = energia_max
            print(f"Você descansou bem! Energia atual: {energia_atual}")
        else:
            print("Você tentou descansar, mas um barulho estranho te tirou o sono!")

    #sair
    elif acao == 8:
        print(f"\nAté a próxima colheita, {jogador}! Moedas finais: {moedas}")
        exit()
    else:
        print("Ação inválida! Você hesitou e perdeu um pouco de energia.")
        energia_atual -= 5

    #ajudante rega a plantação automaticamente
    if ajudante == 1 and plantado == 1:
        saude_plantacao = saude_plantacao + 4
        print("Seu ajudante regou a plantação enquanto você trabalhava!")

    #recalcular a meta com base no cultivo atual (pode ter mudado nesta rodada)
    if plantado_tipo > 0:
        meta_atual = CULTIVOS[plantado_tipo - 1].meta
    else:
        meta_atual = 0

    #verificar plantação
    if plantado == 1 and saude_plantacao >= meta_atual:
        indice_colhido = plantado_tipo - 1
        cultivo_colhido = CULTIVOS[indice_colhido]

        if cultivo_colhido.chance_dobro > 0 and random.randint(1, 100) <= cultivo_colhido.chance_dobro:
            estoque_cultivo[indice_colhido] = estoque_cultivo[indice_colhido] + 2
            print(f"\n Sorte grande! {cultivo_colhido.possessivo} {cultivo_colhido.nome.lower()} rendeu o DOBRO da colheita! Total de {cultivo_colhido.nome.lower()}s: {estoque_cultivo[indice_colhido]}")
        else:
            estoque_cultivo[indice_colhido] = estoque_cultivo[indice_colhido] + 1
            print(f"\n{cultivo_colhido.possessivo} {cultivo_colhido.nome.lower()} cresceu por completo! Total de {cultivo_colhido.nome.lower()}s: {estoque_cultivo[indice_colhido]}")

        plantado = 0
        plantado_tipo = 0
        saude_plantacao = 0

    if energia_atual <= 0:
        print(f"\n{jogador}, você ficou sem energia e não conseguiu continuar cuidando da fazenda... Fim de jogo.")
        resumo_colheitas = " | ".join(f"{CULTIVOS[i].nome}s: {estoque_cultivo[i]}" for i in range(len(CULTIVOS)))
        print(f"Moedas finais: {moedas} | {resumo_colheitas}")
        exit()

    print()