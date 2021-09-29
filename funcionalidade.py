from globais import EMOJI_OPCAO
from arquivo import atualizar_arquivo
from helper import adicionar_id, obter_atributos_manga, exibir_valores_dicionario
from helper import imprimir_busca_manga, imprimir_msg_nao_encontrado
from helper import plotar_grafico_venda_anual, plotar_grafico_venda_total, plot_grafico_genero, plot_grafico_publico


AMARELO = '\u001b[33m'
CIANO = '\u001b[36m'
RESET = '\u001b[0m'
NEGRITO = '\u001b[1m'

def adicionar_manga(dic_mangas):

    id = adicionar_id(dic_mangas)
    dic_mangas[id] = obter_atributos_manga()

    atualizar_arquivo(dic_mangas)
    print(f"Cadastro efetuado com sucesso.")


def exibir_dicionário_completo(dic_mangas):
    
    cor_sep = AMARELO
    cor_tit = AMARELO
    cor_inf = RESET
    cor_neko = CIANO

    print(f"\n\n\n{cor_neko}")
    print(f"{cor_neko}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}")
    print(f"{cor_neko}⡫             ⡫{RESET}")
    print(f"{cor_neko}⡫  O⠀ acervo  ⡫{RESET}⠀⠀        ⣰⣷⣦")
    print(f"{cor_neko}⡫             ⡫{RESET}        ⣀⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⡀⠀⢀⣴⣇")
    print(f"{cor_neko}⡫ está abaixo ⡫{RESET}     ⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"{cor_neko}⡫             ⡫{RESET}    ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"{cor_neko}⡫    \   /    ⡫{RESET}  ⠀⠀⣴⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣄")
    print(f"{cor_neko}⡫     \ /     ⡫{RESET}  ⠀⣾⣿⣿⣿⣿⣿⣶⣿⣯⣭⣬⣉⣽⣿⣿⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀")
    print(f"{cor_neko}⡫      Y      ⡫{RESET}⠀ ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄")
    print(f"{cor_neko}⡫             ⡫{RESET} ⢸⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠁")
    print(f"{cor_neko}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}   ⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠃{RESET}\n\n")

    for id in dic_mangas.keys():

        exibir_valores_dicionario(id,
                                  dic_mangas[id][0], dic_mangas[id][1],
                                  dic_mangas[id][2], dic_mangas[id][3],
                                  dic_mangas[id][4], dic_mangas[id][5],
                                  dic_mangas[id][6], dic_mangas[id][7],
                                  dic_mangas[id][8], dic_mangas[id][9],
                                  dic_mangas[id][10], dic_mangas[id][11],
                                  cor_sep, cor_tit, cor_inf)
        
    print(f"\n\n")
    print(f"{cor_neko}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}")
    print(f"{cor_neko}⡫             ⡫{RESET}")
    print(f"{cor_neko}⡫  O⠀ acervo  ⡫{RESET}⠀⠀       ⠀ ⠀⢠⣿⣶⣄⣀⡀")
    print(f"{cor_neko}⡫             ⡫{RESET}          ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇")
    print(f"{cor_neko}⡫ está  acima ⡫{RESET}     ⠀ ⠀ ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print(f"{cor_neko}⡫             ⡫{RESET}       ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇")
    print(f"{cor_neko}⡫      ^      ⡫{RESET}   ⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄")
    print(f"{cor_neko}⡫     / \     ⡫{RESET}   ⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧")
    print(f"{cor_neko}⡫    /   \    ⡫{RESET}⠀  ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷")
    print(f"{cor_neko}⡫             ⡫{RESET}")
    print(f"{cor_neko}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}\n\n\n")

def buscar_manga(dic_mangas):
    
    imprimir_busca_manga()
    
    id = input(f"{CIANO}{NEGRITO}--------> ID:{RESET} ")
    print("\n")

    if id in dic_mangas.keys():

        exibir_valores_dicionario(id,
                                  dic_mangas[id][0], dic_mangas[id][1],
                                  dic_mangas[id][2], dic_mangas[id][3],
                                  dic_mangas[id][4], dic_mangas[id][5],
                                  dic_mangas[id][6], dic_mangas[id][7],
                                  dic_mangas[id][8], dic_mangas[id][9],
                                  dic_mangas[id][10], dic_mangas[id][11],
                                  AMARELO, AMARELO, RESET)
        print("\n\n\n")
        
    else:
        imprimir_msg_nao_encontrado(id)

def atualizar_manga(dic_mangas):
    '''
    Atualiza item em dicionário passado por parâmetro. Os dados atualizados do dicionário também são atualizados no arquivo.

    Parâmetros
    ----------
    dic_mangas : dictionary
    '''

    imprimir_busca_manga()
    id = input(EMOJI_OPCAO)

    dic_mangas[id] = obter_atributos_manga()
    atualizar_arquivo(dic_mangas)

def deletar_manga(dic_mangas):
    '''
    Deleta item em dicionário passado por parâmetro. Os dados atualizados do dicionário também são atualizados no arquivo.

    Parâmetros
    ----------
    dic_mangas : dictionary
    '''
    
    imprimir_busca_manga()
    id = input(EMOJI_OPCAO)

    dic_mangas.pop(id)
    atualizar_arquivo(dic_mangas)

def visualizar_grafico_vendas_anuais(dic_mangas):
    
    id = input("Digite o ID do mangá que deseja ver a venda anual: ")
    
    if id in dic_mangas.keys():
        ano_venda = int(input("Digite o ano que você deseja ver a venda: "))
        
        nome = dic_mangas[id][0]
        lista_venda = dic_mangas[id][11]        

        plotar_grafico_venda_anual(lista_venda, ano_venda, nome)
    else:
        print("Infelizmente, o ID que você inseriu não está cadastrado.")
    

def visualizar_grafico_vendas_totais(dic_mangas):
    
    id = input("Digite o ID do mangá que deseja ver a venda ao longo dos anos: ")
    print("\n\n")
    
    if id in dic_mangas.keys():
        
        nome = dic_mangas[id][0]
        lista_venda = dic_mangas[id][11]
        
        plotar_grafico_venda_total(lista_venda, nome)

    else:
        print("Infelizmente, o ID que você inseriu não está cadastrado.\n\n\n")    
    

def visualizar_grafico_genero(dic_mangas):
    

    if len(dic_mangas.keys()) > 0:
        
        plot_grafico_genero(dic_mangas)

    else:
        
        print("Infelizmente, não existe nennhum mangá cadastrado.\n\n\n")  


def visualizar_grafico_publico(dic_mangas):

    if len(dic_mangas.keys()) > 0:
        
        plot_grafico_publico(dic_mangas)

    else:
        
        print("Infelizmente, não existe nennhum mangá cadastrado.\n\n\n")  
    
    
    