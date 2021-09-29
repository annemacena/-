from globais import EMOJI_OPCAO
from helper import adicionar_id, obter_atributos_manga, imprimir_busca_manga, imprimir_msg_nao_encontrado, exibir_valores_dicionario
from arquivo import atualizar_arquivo

AMARELO = '\u001b[33m'
CIANO = '\u001b[36m'
RESET = '\u001b[0m'
NEGRITO = '\u001b[1m'

def adicionar_manga(dic_mangas):

    id = adicionar_id(dic_mangas)
    dic_mangas[id] = obter_atributos_manga()
    #print(dic_mangas)
    
    '''id = 'MNG_OP'
    dic_mangas[id] = ['Op', 'Oda', 'Andamento', '2016', 'None', 'Pirata', '110', 'Shonen', ['Ação'], 'Jump', 'Comics', [['2020', '2', '10']]]
    print(dic_mangas)'''
    
    atualizar_arquivo(dic_mangas)
    print(f"Cadastro efetuado com sucesso.")


def exibir_dicionário_completo(dic_mangas):
    
    cor_sep = AMARELO
    cor_tit = AMARELO
    cor_inf = RESET
    cor_neko = CIANO
    cor_txt = CIANO

    print(f"\n\n\n{cor_neko}")
    print(f"{CIANO}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}")
    print(f"{CIANO}⡫             ⡫{RESET}")
    print(f"{CIANO}⡫  O⠀ acervo  ⡫{RESET}⠀⠀        ⣰⣷⣦")
    print(f"{CIANO}⡫             ⡫{RESET}        ⣀⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⡀⠀⢀⣴⣇")
    print(f"{CIANO}⡫ está abaixo ⡫{RESET}     ⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"{CIANO}⡫             ⡫{RESET}    ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"{CIANO}⡫    \   /    ⡫{RESET}  ⠀⠀⣴⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣄")
    print(f"{CIANO}⡫     \ /     ⡫{RESET}  ⠀⣾⣿⣿⣿⣿⣿⣶⣿⣯⣭⣬⣉⣽⣿⣿⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀")
    print(f"{CIANO}⡫      Y      ⡫{RESET}⠀ ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄")
    print(f"{CIANO}⡫             ⡫{RESET} ⢸⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠁")
    print(f"{CIANO}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}   ⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠃{RESET}\n\n")

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
    print(f"{CIANO}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}")
    print(f"{CIANO}⡫             ⡫{RESET}")
    print(f"{CIANO}⡫  O⠀ acervo  ⡫{RESET}⠀⠀       ⠀ ⠀⢠⣿⣶⣄⣀⡀")
    print(f"{CIANO}⡫             ⡫{RESET}          ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇")
    print(f"{CIANO}⡫ está  acima ⡫{RESET}     ⠀ ⠀ ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print(f"{CIANO}⡫             ⡫{RESET}       ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇")
    print(f"{CIANO}⡫      ^      ⡫{RESET}   ⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄")
    print(f"{CIANO}⡫     / \     ⡫{RESET}   ⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧")
    print(f"{CIANO}⡫    /   \    ⡫{RESET}⠀  ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷")
    print(f"{CIANO}⡫             ⡫{RESET}")
    print(f"{CIANO}⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}\n\n\n")

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
