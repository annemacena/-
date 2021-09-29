from main import transformar_string_em_lista
from main import construir_dicionario
from main import adicionar_colchetes_string
from main import transformar_dicionario_em_lista
from main import ler_arquivo
from main import atualizar_arquivo
import os
#from termcolor import colored
"""
id: string
nome: string
autor: string
status: string (Opções: Completo, Andamento, Cancelado e Hiato)
ano_inicio: int
ano_fim: int
sinopse: string
num_de_volumes: int
publico: string (Opções: Shojo, Josei, Shonen e Seinen)
genero: lista de string
impressao: string
revista: string
venda_mensal: [ [ano, mes, quantidade], [ano, mes, quantidade], ..., [ano, mes, quantidade] lista de lista de int
"""

PRETO = '\u001b[30m'
VERMELHO = '\u001b[31m'
VERDE = '\u001b[32m'
AMARELO = '\u001b[33m'
AZUL = '\u001b[34m'
MAGENTA = '\u001b[35m'
CIANO = '\u001b[36m'
BRANCO = '\u001b[37m'
CORR = '\u001b[40m'
RESET = '\u001b[0m'
NEGRITO = '\u001b[1m'
SUBLINHADO = '\u001b[4m'
REVERSO = '\u001b[7m'
BG_PRETO = '\u001b[43m'
LISTA_MESES = ('','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')


# ----------------------------------------------------------------------------#
# -------------------------------------ID-------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ID recebido já foi utilizado
def checar_id(id, dic_mangas):
    
    for chaves_manga in dic_mangas.keys():
        if id == chaves_manga:
            print(f"ID repetido, por favor insira outro ID.")
            return True
    
    return False
# ------------------------------------ID--------------------------------------#
# pede um novo ID ao usuário para cadastro e checa o valor desse ID
def adicionar_id(dic_mangas):
    
    flag_id_repetido = True
    while flag_id_repetido == True:
        id = input(("Entre com o ID único do novo mangá que você deseja cadastrar: "))
        flag_id_repetido = checar_id(id, dic_mangas)
        
    return id


# ----------------------------------------------------------------------------#
# ----------------------------------STATUS------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o status recebido é válido: Completo ou Andamento ou Cancelado ou Hiato
def checar_status(status):

    if status == "Completo" or status == "Andamento" or status == "Cancelado" or status == "Hiato":
        return True
    
    print(f"Status incorreto, por favor insira um status válido.")   
    return False
# ----------------------------------STATUS------------------------------------#
# pede o status do mangá ao usuário e checa se é válido
def adicionar_status():
    
    flag_status_valido = False
    while flag_status_valido == False:
        status = input(("Entre com o status do mangá que você deseja cadastrar - Completo ou Andamento ou Cancelado ou Hiato - : "))
        flag_status_valido = checar_status(status)
        
    return status


# ----------------------------------------------------------------------------#
# -------------------------------ANO DE INICIO--------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_inicio(ano_inicio):

    if ano_inicio >= 0:
        return True
    
    print(f"O ano do início da publicação não é válido, por favor insira um ano válido.")   
    return False
# -------------------------------ANO DE INICIO--------------------------------#
# pede o ano que o mangá começou a ser publicado e checa se é válido
def adicionar_ano_inicio():
    
    flag_ano_inicio_valido = False
    while flag_ano_inicio_valido == False:
        ano_inicio = int(input(("Entre com o ano que o mangá começou a ser publicado: ")))
        flag_ano_inicio_valido = checar_ano_inicio(ano_inicio)
        
    return str(ano_inicio)


# ----------------------------------------------------------------------------#
# --------------------------------ANO DE FIM----------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_fim(ano_fim, ano_inicio):

    if ano_fim >= ano_inicio:
        return True
    
    print(f"O ano do termino da publicação não é válido, por favor insira um ano válido.")   
    return False
# --------------------------------ANO DE FIM----------------------------------#
# pede o ano que o mangá terminou de ser publicado e checa se é válido
def adicionar_ano_fim(status, ano_inicio):
    
    # Se o mangá estiver em Andamento ou em Hiato,
    # ele ainda não terminou de ser publicado
    if status == "Andamento" or status == "Hiato":
        return 'None'
    
    # status == "Completo" or status == "Cancelado"
    flag_ano_fim_valido = False
    while flag_ano_fim_valido == False:
        ano_fim = int(input(("Entre com o ano que o mangá terminou de ser publicado: ")))
        flag_ano_fim_valido = checar_ano_fim(ano_fim, ano_inicio)
        
    return str(ano_fim)


# ----------------------------------------------------------------------------#
# -----------------------------NUMERO DE VOLUMES------------------------------#
# ----------------------------------------------------------------------------#
# checa se o número de volumes é válido
def checar_num_volumes(num_de_volumes):

    if num_de_volumes >= 1:
        return True
    
    print(f"O número de volumes não é válido, por favor insira um valor válido.")   
    return False
# -----------------------------NUMERO DE VOLUMES------------------------------#
# pede o número de volumes do mangá e checa se é esse número é válido
def adicionar_num_volumes():
    
    flag_num_volumes_valido = False
    while flag_num_volumes_valido == False:
        num_de_volumes = int(input(("Entre com a quantidade de volumes que o mangá possui: ")))
        flag_num_volumes_valido = checar_num_volumes(num_de_volumes)
        
    return str(num_de_volumes)


# ----------------------------------------------------------------------------#
# ---------------------------------PUBLICO------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o publico recebido é válido: Shojo ou Josei ou Shonen ou Seinen
def checar_publico(publico):

    if publico == "Shojo" or publico == "Josei" or publico == "Shonen" or publico == "Seinen":
        return True
    
    print(f"Publico incorreto, por favor insira o publico correto.")   
    return False
# ---------------------------------PUBLICO------------------------------------#
# pede o publico do mangá ao usuário e checa se é válido
def adicionar_publico():
    
    flag_publico_valido = False
    while flag_publico_valido == False:
        publico = input(("Entre com o público alvo do mangá que você deseja cadastrar - Shojo ou Josei ou Shonen ou Seinen - : "))
        flag_publico_valido = checar_publico(publico)
        
    return publico


# ----------------------------------------------------------------------------#
# ----------------------------------GENERO------------------------------------#
# ----------------------------------------------------------------------------#
# pede o genero do mangá ao usuário
def adicionar_genero(genero):
    
    flag_adicionar_genero = True
    while flag_adicionar_genero == True:
        gen = input(("Entre com o genero do mangá que você deseja cadastrar: "))
        genero.append(gen)
        
        continua = input(("Você deseja cadastrar um novo genero? s/n: "))
        if continua == "n":
            flag_adicionar_genero = False


# ----------------------------------------------------------------------------#
# ------------------------------VENDAS MENSAIS--------------------------------#
# ----------------------------------------------------------------------------#
# Adiciona as vendas mensais
def adicionar_vendas_mensais(venda_mensal, ano_inicio):
    
    print(f"\nInício do cadastro de vendas mensais do mangá.")

    flag_cadastrar_venda = True
    while flag_cadastrar_venda == True:
        ano_venda = int(input("Entre com o ano: "))
        
        while ano_venda < ano_inicio:
            ano_venda = int(input("Ano inválido. Entre com um ano válido: "))
        
        mes_venda = int(input("Entre com o mês: "))
        
        while mes_venda < 1 or mes_venda > 12:
            mes_venda = int(input("Mês inválido. Entre com um mês válido: "))
        
        quantidade = int(input("Entre com a quantidade de vendas: "))

        while quantidade < 0 :
            quantidade = int(input("Número de vendas mensal inválido. Entre com um valor válido: "))
        
        continua = input(("Você deseja cadastrar outra venda? s/n: "))
        if continua == "n":
            flag_cadastrar_venda = False
            
        venda_mensal.append([str(ano_venda), str(mes_venda), str(quantidade)])
        
    venda_mensal.sort()


# ----------------------------------------------------------------------------#
# ------------------------------ADICIONAR MANGÁ-------------------------------#
# ----------------------------------------------------------------------------#
def adicionar_manga(dic_mangas):

    id = adicionar_id(dic_mangas)
    nome = input(("Entre com o nome do novo mangá que você deseja cadastrar: "))
    autor = input(("Entre com o nome do autor do mangá que você deseja cadastrar: "))
    status = adicionar_status()
    ano_inicio = adicionar_ano_inicio()
    ano_fim = adicionar_ano_fim(status, int(ano_inicio))
    sinopse = input(("Entre com a sinopse do mangá que você deseja cadastrar: "))
    num_de_volumes = adicionar_num_volumes()
    publico = adicionar_publico()
    genero = []
    adicionar_genero(genero)
    impressao = input(("Entre com a gráfica de impressão do mangá: "))
    revista = input(("Entre com a revista de publicação do mangá: "))
    venda_mensal = []
    adicionar_vendas_mensais(venda_mensal, int(ano_inicio))

    dic_mangas[id] = [nome, autor, status, ano_inicio, ano_fim, sinopse, num_de_volumes, publico, genero, impressao, revista, venda_mensal]
    #print(dic_mangas)
    
    '''id = 'MNG_OP'
    dic_mangas[id] = ['Op', 'Oda', 'Andamento', '2016', 'None', 'Pirata', '110', 'Shonen', ['Ação'], 'Jump', 'Comics', [['2020', '2', '10']]]
    print(dic_mangas)'''
    
    atualizar_arquivo(dic_mangas)
    print(f"Cadastro efetuado com sucesso.")


# ----------------------------------------------------------------------------#
# -----------------------------PRINTAR DICIONÁRIO-----------------------------#
# ----------------------------------------------------------------------------#
def exibir_ano_final(ano_final, status, cor_tit, cor_inf):
    
    if status == "Completo" or status == "Cancelado":
        print(f"{cor_tit}Ano final de publicação: {cor_inf}{ano_final}")
    
def transformar_string_em_int(lista_string):
    
    lista_int = []
    for string in lista_string:
         lista_int.append([int(i) for i in string])
    
    lista_int.sort()
    return lista_int

def exibir_vendas(venda_mensal, cor_tit, cor_inf):

    venda_mensal_int = transformar_string_em_int(venda_mensal)
    
    ano_atual = venda_mensal_int[0][0]
    string1 = f"{cor_inf}Ano: {ano_atual}"

    print(f"{string1}")

    for ano, mes, quantidade in venda_mensal_int:
        if ano != ano_atual:
            ano_atual = ano
            print(f"{string1}")

        print(f"    {LISTA_MESES[mes]} - {quantidade} cópia", end = '')
        print("s vendidas" if quantidade > 1 else " vendida")


def exibir_valores_dicionário(id, nome, autor, status, ano_inicio, ano_fim,
                                sinopse, num_de_volumes, publico, genero,
                                impressao, revista, venda_mensal,
                                cor_sep, cor_tit, cor_inf):
    
    print(f"\n{cor_sep}(¸.•´ (¸.•´ .•´ ¸.•´ .•´ ¸¸.•¨¯`•.•´¯¨•.¸¸ `•. `•.¸ `•. `•.¸) `•.¸)\n")
    print(f"{cor_tit}\tInformação sobre o mangá {cor_inf}{id}\n")
    print(f"{cor_tit}Nome: {cor_inf}{nome}")
    print(f"{cor_tit}Autor(a): {cor_inf}{autor}")
    print(f"{cor_tit}Status: {cor_inf}{status}")
    print(f"{cor_tit}Ano inicial de publicação: {cor_inf}{ano_inicio}")
    exibir_ano_final(ano_fim, status, cor_tit, cor_inf)
    print(f"{cor_tit}Sinopse: {cor_inf}{sinopse}")
    print(f"{cor_tit}Número de volumes: {cor_inf}{num_de_volumes}")
    print(f"{cor_tit}Público: {cor_inf}{publico}")        
    print(f"{cor_tit}Gênero(s): {cor_inf}{', '.join(genero)}")        
    print(f"{cor_tit}Impressão do Tankobon: {cor_inf}{impressao}")
    print(f"{cor_tit}Revista de publicação dos capítulos: {cor_inf}{revista}")
    print(f"{cor_tit}Vendas mensais:")
    exibir_vendas(venda_mensal, cor_tit, cor_inf)
    print(f"\n{cor_sep}(¸.•´ (¸.•´ .•´ ¸.•´ .•´ ¸¸.•¨¯`•.•´¯¨•.¸¸ `•. `•.¸ `•. `•.¸) `•.¸)")
    

def exibir_dicionário_completo(dic_mangas):
    
    os.system(f"cls")
    
    cor_sep = AMARELO
    cor_tit = AMARELO
    cor_inf = RESET
    cor_neko = CIANO
    cor_txt = CIANO
    #texto = colored('Hello and Welcome to FINXTER!', attrs=['bold'])  # bold-text
    #print(texto)
    

    print(f"\n\n\n{cor_neko}")
    print(f"\u001b[36m⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}")
    print(f"\u001b[36m⡫             ⡫{RESET}")
    print(f"\u001b[36m⡫  O⠀ acervo  ⡫{RESET}⠀⠀        ⣰⣷⣦")
    print(f"\u001b[36m⡫             ⡫{RESET}        ⣀⣶⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⣀⡀⠀⢀⣴⣇")
    print(f"\u001b[36m⡫ está abaixo ⡫{RESET}     ⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"\u001b[36m⡫             ⡫{RESET}    ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"\u001b[36m⡫    \   /    ⡫{RESET}  ⠀⠀⣴⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣄")
    print(f"\u001b[36m⡫     \ /     ⡫{RESET}  ⠀⣾⣿⣿⣿⣿⣿⣶⣿⣯⣭⣬⣉⣽⣿⣿⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀")
    print(f"\u001b[36m⡫      Y      ⡫{RESET}⠀ ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄")
    print(f"\u001b[36m⡫             ⡫{RESET} ⢸⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠁")
    print(f"\u001b[36m⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⡫{RESET}   ⠘⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠃{RESET}\n\n")

    for chave in dic_mangas.keys():

        exibir_valores_dicionário(chave,
                                  dic_mangas[chave][0], dic_mangas[chave][1],
                                  dic_mangas[chave][2], dic_mangas[chave][3],
                                  dic_mangas[chave][4], dic_mangas[chave][5],
                                  dic_mangas[chave][6], dic_mangas[chave][7],
                                  dic_mangas[chave][8], dic_mangas[chave][9],
                                  dic_mangas[chave][10], dic_mangas[chave][11],
                                  cor_sep, cor_tit, cor_inf)
        
    print(f"\n\n")
    print(f"\u001b[36m⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}")
    print(f"\u001b[36m⡫             ⡫{RESET}")
    print(f"\u001b[36m⡫  O⠀ acervo  ⡫{RESET}⠀⠀       ⠀ ⠀⢠⣿⣶⣄⣀⡀")
    print(f"\u001b[36m⡫             ⡫{RESET}          ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇")
    print(f"\u001b[36m⡫ está  acima ⡫{RESET}     ⠀ ⠀ ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print(f"\u001b[36m⡫             ⡫{RESET}       ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇")
    print(f"\u001b[36m⡫      ^      ⡫{RESET}   ⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄")
    print(f"\u001b[36m⡫     / \     ⡫{RESET}   ⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧")
    print(f"\u001b[36m⡫    /   \    ⡫{RESET}⠀  ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷")
    print(f"\u001b[36m⡫             ⡫{RESET}")
    print(f"\u001b[36m⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⢕{RESET}\n\n\n")

# ----------------------------------------------------------------------------#
# --------------------------------BUSCAR MANGÁ--------------------------------#
# ----------------------------------------------------------------------------#
def buscar_manga(dic_mangas):
    
    cor_txt = CIANO

    print(f"\n\n\n")
    print("⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⠛⠉⣉⣀⣀⣈⠉⠻⠿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿")
    print("⣿⠛⠁⣠⣤⣤⣤⣄⠈⠋⠁⠠⣾⡿⠛⠛⣿⣿⡄⠄⠄⠄⠠⣴⣶⣦⣤⡀⠙⢿")
    print("⠃⢰⣿⠿⠛⠛⢿⣿⡇⠄⠄⠄⠄⠄⠄⢀⣾⡿⠁⠄⠂⠂⠄⠘⠉⠙⠻⣿⣦⠈")
    print("⣦⣤⣀⣀⠈⢠⣿⡿⠁⠄⠄⠄⠄⠄⢸⣿⡏⠄⠄⠄⠄⠄⠄⠁⣠⣴⣾⣿⠏⢠")
    print("⣿⣿⣿⣿⠄⠿⠟⠄⠄⠄⠄⠄⠄⠄⣠⣤⡄⠄⠄⠄⠄⠄⢀⣈⠛⠋⠉⠄⢠⣾")
    print("⣿⣿⣿⡏⠄⢰⣿⣶⠄⠄⠄⠄⠄⠄⠙⠿⠃⠄⠄⠄⠄⠄⠿⣿⡇⠄⠄⠄⠄⣿")
    print("⣿⣿⣿⠄⠄⡈⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿")
    print(f"⣿⣿⣷⠄⠄⢉⠄⠄⠄⠄⠄⠐⠦⡘⠿⠿⣿⡿⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿     \u001b[36m-----------{RESET}" )
    print(f"⣿⣿⡟⠈⠄⠄⠄⠄⢰⣄⠄⠠⠄⠄⠄⢀⡌⠁⠄⠄⠄⣹⠟⡁⠄⠄⠄⠄⣸⣿   \u001b[36m/  Digite    |{RESET}" )
    print(f"⣿⣿⠇⠄⠄⠄⠄⠄⢸⣿⣿⣷⣦⡤⣾⣿⣷⢄⣀⣀⣠⣶⣿⠁⠄⠄⠄⢠⣿⣿  \u001b[36m/ abaixo o ID |{RESET}" ) 
    print(f"⣿⣿⣤⣶⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⠻⢿⠿⢻⣿⣿⣿⣿⡍⠄⠄⠄⣴⣿⣿⣿ \u001b[36m<   do mangá   |{RESET}" )
    print(f"⣿⣿⣿⣿⠄⠄⠄⠄⠘⣿⣿⡟⠄⠄⠄⠄⠄⠉⠛⠻⣿⣿⠁⠄⠄⢸⣿⣿⣿⣿  \u001b[36m\ que deseja  |{RESET}" )
    print(f"⣿⣿⣯⣉⣀⠄⠄⠄⠄⢿⣿⣆⣼⣿⠲⠲⠶⢦⣄⡀⠻⡏⠄⠄⠰⣼⣿⣿⣿⣿   \u001b[36m\   buscar   |{RESET}" )
    print(f"⣿⣿⣿⣿⣿⡄⠠⠄⠄⠄⠻⢝⠿⣿⣿⣿⣷⣶⠟⢃⡄⠁⠄⠄⠸⣾⡿⣿⣿⣿     \u001b[36m-----------{RESET}" )
    print(f"⡿⠟⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠁⠚⠋⠁⠄⠄⠄⠄⠒⠿⣿⣿⣿\n")
    
    chave = input(f"\u001b[36m{NEGRITO}--------> ID:{RESET} ")
    print("\n")

    if chave in dic_mangas.keys():

        cor_sep = AMARELO
        cor_tit = AMARELO
        cor_inf = RESET
        exibir_valores_dicionário(chave,
                                  dic_mangas[chave][0], dic_mangas[chave][1],
                                  dic_mangas[chave][2], dic_mangas[chave][3],
                                  dic_mangas[chave][4], dic_mangas[chave][5],
                                  dic_mangas[chave][6], dic_mangas[chave][7],
                                  dic_mangas[chave][8], dic_mangas[chave][9],
                                  dic_mangas[chave][10], dic_mangas[chave][11],
                                  cor_sep, cor_tit, cor_inf)
        print("\n\n\n")
        
    else:
        cor_txt = VERMELHO
        print(f"\n\n" )
        print(f"    ,.  ,.                       \u001b[36m(｡╯︵╰｡){RESET}" )
        print(f"    ||  ||           \u001b[36m-----------------------------------{RESET}" )
        print(f"   ,''--''.        \u001b[36m/                                    |{RESET}" )
        print(f"  : (.)(.) :      \u001b[36m/  O mangá com o ID:                  |{RESET}" )
        print(f" ,'   ︵   `.   \u001b[36m<    {chave}{RESET}" )
        print(f" :          :     \u001b[36m\  NÃO foi encontrado.                |{RESET}" )
        print(f" :          :      \u001b[36m\                                    |{RESET}" )
        print(f" `._m____m_,'        \u001b[36m-----------------------------------{RESET}" )
        print(f"\n\n{RESET}" )

n = 1
lista_mangas = ler_arquivo()
dic_mangas = construir_dicionario(lista_mangas)
'''print(construir_dicionario)
for i in range(n):
    adicionar_manga(dic_mangas)
print(dic_mangas)'''

buscar_manga(dic_mangas)
exibir_dicionário_completo(dic_mangas)

