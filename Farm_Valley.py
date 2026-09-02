import random

mensagens_colheita = [
    "Que colheita linda!",
    "Uau, cresceu rápido!",
    "Mais uma pra sua coleção!",
    "A terra te agradece!",
    "Colheita no capricho!"
]

print("=" * 60)
print("\nBem vindo(a) à Farm Valley!\n")
print("=" * 60)

#criação do personagem
jogador = input("Digite o seu nome fazendeiro(a): ")
print(f"\nOlá {jogador}! Qual o seu tipo de fazendeiro(a)?\n")
print("1 - Agricultor | 2 - Pecuarista | 3 - Herborista | 4 - Pescador")
tipo_jogador = input("Escolha: ")

try:
    tipo_jogador = int(tipo_jogador)
    if tipo_jogador == 1:
        nome_tipo = "Agricultor"
        energia_max = 100
        habilidade_plantio = 15
        habilidade_pecuaria = 6
        sorte = 5
    elif tipo_jogador == 2:
        nome_tipo = "Pecuarista"
        energia_max = 120
        habilidade_plantio = 8
        habilidade_pecuaria = 18
        sorte = 8
    elif tipo_jogador == 3:
        nome_tipo = "Herborista"
        energia_max = 80
        habilidade_plantio = 20
        habilidade_pecuaria = 8
        sorte = 10
    elif tipo_jogador == 4:
        nome_tipo = "Pescador"
        energia_max = 90
        habilidade_plantio = 6
        habilidade_pecuaria = 7
        sorte = 15
    else:
        print(f"Parabéns {jogador}! Não escolheu corretamente e virou um Fazendeiro Pamonha!")
        nome_tipo = "Fazendeiro Pamonha"
        energia_max = 70 
        habilidade_plantio = 6
        habilidade_pecuaria = 8
        sorte = 8
except: 
    print("Valor indevido! Encerrando o jogo.")
    exit()

print(f"\nFicha criada para: {jogador}")
print(f"Tipo: {nome_tipo}")
print(f"Energia Máxima: {energia_max}")
print(f"Habilidade de Plantio: {habilidade_plantio}")
print(f"Habilidade de Pecuária: {habilidade_pecuaria}") 
print(f"Sorte: {sorte}")

energia_atual = energia_max

#recursos do jogador
moedas = 30
sementes_cenoura = 1    #começa com 1 semente de cenoura de graça
sementes_milho = 0
sementes_morango = 0
adubo = 0
estoque_cenoura = 0
estoque_milho = 0
estoque_morango = 0
vara_pesca = 0         #precisa comprar na loja antes de pescar
peixe_nivel1 = 0
peixe_nivel2 = 0
peixe_nivel3 = 0

#upgrades e investimentos
ferramenta_melhorada = 0   #0 = não comprou | 1 = comprou (upgrade único)
rede_reforcada = 0         #0 = não comprou | 1 = comprou (upgrade único)
ajudante = 0              #0 = não contratou | 1 = contratou (upgrade único)
galinhas = 0
vacas = 0
ovos = 0
leite = 0
progresso_galinhas = 0
progresso_vacas = 0

#estado da plantação | preços
plantado = 0
plantado_tipo = 0      #0 = nada | 1 = cenoura | 2 = milho | 3 = morango
saude_plantacao = 0

PRECO_SEMENTE_CENOURA = 3
PRECO_SEMENTE_MILHO = 15
PRECO_SEMENTE_MORANGO = 8
PRECO_VENDA_CENOURA = 7
PRECO_VENDA_MILHO = 30
PRECO_VENDA_MORANGO = 14
META_CENOURA = 20       #barata e rápida
META_MILHO = 90          #cara e lenta, mas rende muito
META_MORANGO = 45        #meio-termo, com chance de colheita dupla
CHANCE_MORANGO_DOBRO = 25   #de 100, chance de render 2 ao colher
PRECO_ADUBO = 8
PRECO_VARA_PESCA = 25
PRECO_VENDA_PEIXE1 = 5
PRECO_VENDA_PEIXE2 = 8
PRECO_VENDA_PEIXE3 = 12
PRECO_FERRAMENTA = 60
PRECO_REDE = 50
PRECO_GALINHA = 35
PRECO_VACA = 150
PRECO_AJUDANTE = 200
PRECO_VENDA_OVO = 4
PRECO_VENDA_LEITE = 9
ENERGIA_CUIDAR_GALINHA = 5
ENERGIA_CUIDAR_VACA = 12
META_GALINHAS = 30
META_VACAS = 60

print(f"\n{jogador}, bem-vindo(a) à sua fazenda! Cuide da terra, compre na loja, pesque peixes, venda suas colheitas e peixes")

#loop principal
while energia_atual > 0:
    print("=" * 50)
    print(f"   FARM VALLEY — {jogador} ({nome_tipo})")
    print("=" * 50)

    if plantado_tipo == 1:
        meta_atual = META_CENOURA
        nome_cultivo = "Cenoura"
    elif plantado_tipo == 2:
        meta_atual = META_MILHO
        nome_cultivo = "Milho"
    elif plantado_tipo == 3:
        meta_atual = META_MORANGO
        nome_cultivo = "Morango"
    else:
        meta_atual = 0
        nome_cultivo = "Nenhuma"

    print("\n--- STATUS ---")
    print(f"Energia: {energia_atual}/{energia_max}")
    if plantado == 1:
        print(f"Plantação: ({nome_cultivo}): {saude_plantacao}/{meta_atual}")
    else:
        print("Plantação: nenhuma planta ativa")

    print("\n--- RECURSOS ---")
    print(f"Moedas: {moedas} | Adubo: {adubo}")
    print(f"Sementes -> Cenoura: {sementes_cenoura} | Milho: {sementes_milho} | Morango: {sementes_morango}")
    print(f"Colheitas -> Cenoura: {estoque_cenoura} | Milho: {estoque_milho}  | Morango: {estoque_morango}")
    print(f"Vara de pesca: {vara_pesca}")
    print(f"Peixes -> N1: {peixe_nivel1} | N2: {peixe_nivel2} | N3: {peixe_nivel3}")
    print(f"Galinhas: {galinhas} | Vacas: {vacas} | Ajudante: {'Sim' if ajudante == 1 else 'Não'}")
    print(f"Ovos: {ovos} | Leite: {leite}")
    if galinhas > 0:
        print(f"Progresso galinhas: {progresso_galinhas}/{META_GALINHAS}")
    if vacas > 0:
        print(f"Progresso vacas: {progresso_vacas}/{META_VACAS}")

    print("\n--- AÇÕES ---")
    print("1-Loja | 2-Plantar | 3-Regar | 4-Adubar | 5-Pescar | 6-Cuidar dos animais | 7-Descansar | 8-Sair")
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
            print(f"1 - Comprar semente (Cenoura: {PRECO_SEMENTE_CENOURA} | Milho: {PRECO_SEMENTE_MILHO} | Morango: {PRECO_SEMENTE_MORANGO} moedas)")
            print(f"2 - Comprar adubo ({PRECO_ADUBO} moedas)")
            print(f"3 - Comprar vara de pesca ({PRECO_VARA_PESCA} moedas)")
            print(f"4 - Vender colheitas (Cenoura: {PRECO_VENDA_CENOURA} | Milho: {PRECO_VENDA_MILHO} | Morango: {PRECO_VENDA_MORANGO} moedas)")
            print(f"5 - Vender peixes (N1: {PRECO_VENDA_PEIXE1} | N2: {PRECO_VENDA_PEIXE2} | N3: {PRECO_VENDA_PEIXE3} moedas)")
            print(f"6 - Ferramenta melhorada ({PRECO_FERRAMENTA} moedas, upgrade único, +5 habilida de plantio)")
            print(f"7 - Rede reforçada ({PRECO_REDE} moedas, upgrade único, reduz risco de perder a vara)")
            print(f"8 - Comprar galinha ({PRECO_GALINHA} moedas, precisa cuidar para gerar ovos)")
            print(f"9 - Comprar vaca ({PRECO_VACA} moedas, precisa cuidar para gerar leite)")
            print(f"10 - Contratar ajudante ({PRECO_AJUDANTE} moedas, upgrade único, rega a plantação sozinho)")
            print(f"11 - Vender ovos e leite (Ovo: {PRECO_VENDA_OVO} | Leite: {PRECO_VENDA_LEITE} moedas)")
            print("12 - Voltar para a fazenda")

            try:
                escolha_loja = int(input("O que deseja fazer? "))
            except:
                print("Entrada inválida!")
                continue

            if escolha_loja == 1:
                print("1 - Cenoura | 2 - Milho | 3 - Morango")
                try:
                    escolha_semente = int(input("Qual semente comprar? "))
                except:
                    print("Entrada inválida!")
                    escolha_semente = 0

                if escolha_semente == 1:
                    if moedas >= PRECO_SEMENTE_CENOURA:
                        moedas = moedas - PRECO_SEMENTE_CENOURA
                        sementes_cenoura = sementes_cenoura + 1
                        print(f"Você comprou 1 semente de cenoura! Total: {sementes_cenoura} | Moedas: {moedas}")
                    else:
                        print("Moedas insuficientes para comprar semente de cenoura!")
                elif escolha_semente == 2:
                    if moedas >= PRECO_SEMENTE_MILHO:
                        moedas = moedas - PRECO_SEMENTE_MILHO
                        sementes_milho = sementes_milho + 1
                        print(f"Você comprou 1 semente de milho! Total: {sementes_milho} | Moedas: {moedas}")
                    else:
                        print("Moedas insuficientes para comprar semente de milho!")
                elif escolha_semente == 3:
                    if moedas >= PRECO_SEMENTE_MORANGO:
                        moedas = moedas - PRECO_SEMENTE_MORANGO
                        sementes_morango = sementes_morango + 1
                        print(f"Você comprou 1 semente de morango! Total: {sementes_morango} | Moedas: {moedas}")
                    else:
                        print("Moedas insuficientes para comprar semente de morango!")
                else:
                    print("Opção de semente inválida!")

            elif escolha_loja == 2:
                if moedas >= PRECO_ADUBO:
                    moedas =  moedas - PRECO_ADUBO
                    adubo = adubo + 1
                    print("Você comprou 1 adubo!")
                    print(f"Adubo: {adubo} | Moedas: {moedas}")
                else:
                    print("Moedas insuficientes para comprar adubo!")

            elif escolha_loja == 3:
                if moedas >= PRECO_VARA_PESCA:
                    moedas =  moedas - PRECO_VARA_PESCA
                    vara_pesca = vara_pesca + 1
                    print("Você comprou 1 vara de pesca!")
                    print(f"Varas: {vara_pesca} | Moedas: {moedas}")
                else:
                    print("Moedas insuficientes para comprar vara de pesca!")

            elif escolha_loja == 4:
                total_colheitas = estoque_cenoura + estoque_milho + estoque_morango
                if total_colheitas > 0:
                    ganho_colheita = (estoque_cenoura * PRECO_VENDA_CENOURA) + (estoque_milho * PRECO_VENDA_MILHO) + (estoque_morango * PRECO_VENDA_MORANGO)
                    print(f"Você vendeu {estoque_cenoura} cenoura(s), {estoque_milho} milho(s) e {estoque_morango} morango(s) por {ganho_colheita} moedas!")
                    moedas = moedas + ganho_colheita
                    estoque_cenoura = 0
                    estoque_milho = 0
                    estoque_morango = 0
                    ganho_colheita = 0
                else:
                    print("Você não tem colheitas para vender!")

            elif escolha_loja == 5:
                total_peixes = peixe_nivel1 + peixe_nivel2 + peixe_nivel3
                if total_peixes > 0:
                    ganho_peixe = (peixe_nivel1 * PRECO_VENDA_PEIXE1) + (peixe_nivel2 * PRECO_VENDA_PEIXE2) + (peixe_nivel3 * PRECO_VENDA_PEIXE3)
                    moedas = moedas + ganho_peixe
                    print(f"Você vendeu {total_peixes} peixe(s) por {ganho_peixe} moedas!")
                    ganho_peixe = 0
                    peixe_nivel1 = 0
                    peixe_nivel2 = 0
                    peixe_nivel3 = 0
                else:
                    print(" Você não tem peixes para vender!")

            elif escolha_loja == 6:
                if ferramenta_melhorada == 1:
                    print("Você já tem a ferramenta melhorada!")
                elif moedas >= PRECO_FERRAMENTA:
                    moedas = moedas - PRECO_FERRAMENTA
                    ferramenta_melhorada = 1
                    habilidade_plantio = habilidade_plantio + 5
                    print(f"Ferramenta melhorada comprada! Habilidade de plantio agora é {habilidade_plantio}!")
                else:
                    print("Moedas insuficientes para comprar a ferramenta melhorada!")

            elif escolha_loja == 7:
                if rede_reforcada == 1:
                    print("Você já tem a rede reforçada!")
                elif moedas >= PRECO_REDE:
                    moedas = moedas - PRECO_REDE
                    rede_reforcada = 1
                    sorte = sorte + 5
                    print(f"Rede reforçada comprada! Agora você perde a vara com menos frequência. Sua sorte agora é {sorte}!")
                else:
                    print("Moedas insuficientes para comprar a rede reforçada!")

            elif escolha_loja == 8:
                if moedas >= PRECO_GALINHA:
                    moedas = moedas - PRECO_GALINHA
                    galinhas = galinhas + 1
                    print(f"Você comprou 1 galinha! Total de galinhas: {galinhas}")
                else:
                    print("Moedas insuficientes para comprar a galinha!")

            elif escolha_loja == 9:
                if moedas >= PRECO_VACA:
                    moedas = moedas - PRECO_VACA
                    vacas = vacas + 1
                    print(f"Você comprou 1 vaca! Total de vacas: {vacas}")
                else:
                    print("Moedas insuficientes para comprar a vaca!")

            elif escolha_loja == 10:
                if ajudante == 1:
                    print("Você já tem um ajudante contratado!")
                elif moedas >= PRECO_AJUDANTE:
                    moedas = moedas - PRECO_AJUDANTE
                    ajudante = 1
                    print("Ajudante contratado! Ele vai cuidar da plantação automaticamente a cada rodada.")
                else:
                    print("Moedas insuficientes para contratar o ajudante!")

            elif escolha_loja == 11:
                total_produtos = ovos + leite
                if total_produtos > 0:
                    ganho_produtos = (ovos * PRECO_VENDA_OVO) + (leite * PRECO_VENDA_LEITE)
                    print(f"Você vendeu {ovos} ovo(s) e {leite} leite(s) por {ganho_produtos} moedas!")
                    moedas = moedas + ganho_produtos
                    ovos = 0
                    leite = 0
                    ganho_produtos = 0
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
            print("1 - Cenoura | 2 - Milho | 3 - Morango")
            try:
                escolha_plantio = int(input("O que deseja plantar? "))
            except:
                print("Entrada inválida!")
                escolha_plantio = 0

            if escolha_plantio == 1:
                if sementes_cenoura <= 0:
                    print("Você não tem sementes de cenoura! Vá até a loja para comprar.")
                else:
                    sementes_cenoura = sementes_cenoura - 1
                    plantado = 1
                    plantado_tipo = 1
                    saude_plantacao = 0
                    print("Você plantou uma cenoura, agora cuide dela!")
            elif escolha_plantio == 2:
                if sementes_milho <= 0:
                    print("Você não tem sementes de milho! Vá até a loja para comprar.")
                else:
                    sementes_milho = sementes_milho - 1
                    plantado = 1
                    plantado_tipo = 2
                    saude_plantacao = 0
                    print("Você plantou um milho, agora cuide dele!")
            elif escolha_plantio == 3:
                if sementes_morango <= 0:
                    print("Você não tem sementes de morango! Vá até a loja para comprar.")
                else:
                    sementes_morango = sementes_morango - 1
                    plantado = 1
                    plantado_tipo = 3
                    saude_plantacao = 0
                    print("Você plantou um morango, agora cuide dele!")
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
                peixe_nivel3 = peixe_nivel3 + 1
                print(f"Uau!! Você fisgou um peixe raro (nível 3)! Total N3: {peixe_nivel3}")
            elif resultado >= 18:
                peixe_nivel2 = peixe_nivel2 + 1
                print(f"Você pescou um peixe bom (nível 2)! Total N2: {peixe_nivel2}")
            elif resultado >= 10:
                peixe_nivel1 = peixe_nivel1 + 1
                print(f"Você pescou um peixe comum (nível 1)! Total N1: {peixe_nivel1}")
            else:
                print("Nada mordeu o anzol dessa vez...")

            risco_perder = 20 - sorte
            if risco_perder < 0:
                risco_perder = 0
            chance_perder = random.randint(1, 100)
            if chance_perder <= risco_perder:
                vara_pesca = vara_pesca - 1
                print(f"Opss! Sua linha arrebentou e você perdeu a vara de pesca! Varas restante: {vara_pesca}")

            print(f"Energia atual: {energia_atual}")

    #cuidar dos animais
    elif acao == 6:
        if galinhas == 0 and vacas == 0:
            print("Você não tem nenhum animal! Vá até a loja para comprar galinhas ou vacas.")
        else:
            custo_energia = 0
            if galinhas > 0:
                custo_energia = custo_energia + ENERGIA_CUIDAR_GALINHA  
            if vacas > 0:
                custo_energia = custo_energia + ENERGIA_CUIDAR_VACA          

            if energia_atual < custo_energia:
                print("Energia insuficiente para cuidar dos animais! Descanse!")
            else:
                energia_atual = energia_atual - custo_energia

                if galinhas > 0:
                    progresso_galinhas = progresso_galinhas + habilidade_pecuaria
                    print(f"Você cuidou das galinhas! Progresso: {progresso_galinhas}/{META_GALINHAS}")
                if vacas > 0:
                    progresso_vacas = progresso_vacas + (habilidade_pecuaria // 2)
                    print(f"Você cuidou das vacas! Progresso: {progresso_vacas}/{META_VACAS}")

                print(f"Energia atual: {energia_atual}")

                if progresso_galinhas >= META_GALINHAS:
                    ovos = ovos + galinhas
                    progresso_galinhas = 0 
                    print(f"As galinhas estão prontas! Você coletou {galinhas} ovo(s). Total de ovos: {ovos}")
                if progresso_vacas >= META_VACAS:
                    leite = leite + vacas
                    progresso_vacas = 0
                    print(f"As vacas estão prontas! Você tirou {vacas} leite(s). Total de leite: {leite}")

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
    if plantado_tipo == 1:
        meta_atual = META_CENOURA
    elif plantado_tipo == 2:
        meta_atual = META_MILHO
    elif plantado_tipo == 3:
        meta_atual = META_MORANGO
    else:
        meta_atual = 0

    #verificar plantação
    if plantado == 1 and saude_plantacao >= meta_atual:
        print(random.choice(mensagens_colheita))
        if plantado_tipo == 1:
            estoque_cenoura = estoque_cenoura + 1
            print(f"\nSua cenoura cresceu por completo! Total de cenouras: {estoque_cenoura}")
        elif plantado_tipo == 2:
            estoque_milho = estoque_milho + 1
            print(f"\nSeu milho cresceu por completo! Total de milhos: {estoque_milho}")
        elif plantado_tipo == 3:
            sorteio_morango = random.randint(1, 100)
            if sorteio_morango <= CHANCE_MORANGO_DOBRO:
                estoque_morango = estoque_morango + 2
                print(f"\nSorte grande! Seu morango rendeu o DOBRO da colheita! Total de morangos: {estoque_morango}")
            else:
                estoque_morango = estoque_morango + 1
                print(f"\nSeu morango cresceu por completo! Total de morangos: {estoque_morango}")
        plantado = 0
        plantado_tipo = 0
        saude_plantacao = 0

    if energia_atual <= 0:
        print(f"\n{jogador}, você ficou sem energia e não conseguiu continuar cuidando da fazenda... Fim de jogo.")
        print(f"Moedas finais: {moedas} | Cenouras: {estoque_cenoura} | Milhos: {estoque_milho} | Morangos: {estoque_morango}")
        exit()

    print()