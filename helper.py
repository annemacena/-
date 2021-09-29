from globais import LISTA_MESES

AMARELO = '\u001b[33m'
CIANO = '\u001b[36m'
RESET = '\u001b[0m'
NEGRITO = '\u001b[1m'
VERMELHO = '\u001b[31m'

def transformar_string_em_lista(registro_string, caractere_separador, tipo_itens_array = None):
    '''
    Transforma uma string em array, dado um caractere separador. 
    
    Exemplo:
        registro_string = "[drama,girls love,romance]"
        caractere_separador = ","
        retorno = ["drama", "girls love", "romance"]

    Parâmetros
    ----------
    registro_string : str
        String a ser transformada em array.
    caractere_separador : str
        Caractere que é usado como separador da string passada por parâmetro (registro_string).
    tipo_itens_array: palavra reservada (int, float)
        Palavra reservada especifica qual tipo os itens do array deve ter convertido (exemplo: int, float, etc). 

    Retorno
    -------
    array de string, int ou float

    '''
    registro_lista = []
    registro_string = registro_string[1:len(registro_string)-1] # pega a string sem os colchetes

    lista_final = registro_string.split(caractere_separador)

    if(tipo_itens_array != None):
        lista_final = list(map(tipo_itens_array, lista_final))
        
    return lista_final

def construir_dicionario(lista_registros):
    '''
    Constrói um dicionário a partir de um array de string. Cada value do dicionário é um array gerado de cada item de "lista_registros"
    separadas por ponto e vírgula (;).

    Exemplo: 
        lista_registros = ["id;atributo1;atributo2", "id2;atributo1;atributo2"]
        dic = {'id': ['atributo1', 'atributo2'], 'id2': ['atributo1', 'atributo2']}

    Parâmetros
    ----------
    lista_registros : array de string

    Retorno
    -------
    dictionary
    '''
    dicionario = {}
    for registro in lista_registros:
        registro_dividido = registro.split(";")

        id_manga = registro_dividido[0]
        atributos_manga = registro_dividido[1:]

        # os itens nos índices 8 e 11 são listas (gênero e venda mensal) 
        atributos_manga[8] = transformar_string_em_lista(atributos_manga[8], ",")
        atributos_manga[11] = transformar_string_em_lista(atributos_manga[11], ",")

        cont = 0
        # venda mensal é um lista de listas
        for venda_mensal in atributos_manga[11]:
            atributos_manga[11][cont] = transformar_string_em_lista(venda_mensal, "_", int)
            cont += 1
        cont = 0

        # convertendo valores do tipo inteiro (ver https://github.com/annemacena/mangarisuto#rela%C3%A7%C3%A3o-atributo-x-%C3%ADndice) 
        atributos_manga[3] = int(atributos_manga[3])
        atributos_manga[4] = int(atributos_manga[4])
        atributos_manga[6] = int(atributos_manga[6])

        dicionario[id_manga] = atributos_manga

    return dicionario

def adicionar_colchetes_string(string):
    '''
    Encalpsula a string passada por parâmetro em colchetes.

    Parâmetros
    ----------
    str

    Retorno
    -------
    str
    '''
    return "[" + string + "]"

def transformar_dicionario_em_lista(dic):
    '''
    Transforma um dicionário em um array de strings separadas por ponto e vírgula (;).

    Exemplo:
        dic = {'id': ['atributo1', 'atributo2'], 'id2': ['atributo1', 'atributo2']}
        lista_registros = ["id;atributo1;atributo2", "id2;atributo1;atributo2"]

    Parâmetros
    ----------
    dic : dictionary

    Retorno
    -------
    lista_registros: array de string
        Cada item do array são dados de um registro (mangá).
    '''
    lista_registros = []
    total_registros = len(dic.keys())

    for id in dic.keys():
        registro_atual = ""
        registro_atual += id + ";"

        lista_atributos = dic[id]
        
        # os itens nos índices 8 e 11 são listas (gênero e venda mensal) 
        lista_atributos[8] = adicionar_colchetes_string(",".join(lista_atributos[8]))

        cont = 0
        for venda_mensal in lista_atributos[11]:
            lista_atributos[11][cont] = adicionar_colchetes_string("_".join(map(str, venda_mensal)))
            cont += 1
            
        lista_atributos[11] = adicionar_colchetes_string(",".join(map(str, lista_atributos[11])))

        registro_atual += ";".join(map(str, lista_atributos))
        
        lista_registros.append(registro_atual)

    return lista_registros

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
        id = input(("Entre com o ID único do novo mangá: "))
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
        status = input(("Entre com o status do mangá - Completo ou Andamento ou Cancelado ou Hiato - : "))
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
        publico = input(("Entre com o público alvo do mangá - Shojo ou Josei ou Shonen ou Seinen - : "))
        flag_publico_valido = checar_publico(publico)
        
    return publico


# ----------------------------------------------------------------------------#
# ----------------------------------GENERO------------------------------------#
# ----------------------------------------------------------------------------#
# pede o genero do mangá ao usuário
def adicionar_genero(genero):
    
    flag_adicionar_genero = True
    while flag_adicionar_genero == True:
        gen = input(("Entre com o genero do mangá: "))
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

def obter_atributos_manga():
    
    nome = input(("Entre com o nome do mangá: "))
    autor = input(("Entre com o nome do autor do mangá: "))
    status = adicionar_status()
    ano_inicio = adicionar_ano_inicio()
    ano_fim = adicionar_ano_fim(status, int(ano_inicio))
    sinopse = input(("Entre com a sinopse do mangá: "))
    num_de_volumes = adicionar_num_volumes()
    publico = adicionar_publico()
    genero = []
    adicionar_genero(genero)
    impressao = input(("Entre com a gráfica de impressão do mangá: "))
    revista = input(("Entre com a revista de publicação do mangá: "))
    venda_mensal = []
    adicionar_vendas_mensais(venda_mensal, int(ano_inicio))

    return [nome, autor, status, ano_inicio, ano_fim, sinopse, num_de_volumes, publico, genero, impressao, revista, venda_mensal]

# ----------------------------------------------------------------------------#
# -----------------------------PRINTAR DICIONÁRIO-----------------------------#
# ----------------------------------------------------------------------------#
def exibir_ano_final(ano_final, status, cor_tit, cor_inf):
    
    if status == "Completo" or status == "Cancelado":
        print(f"{cor_tit}Ano final de publicação: {cor_inf}{ano_final}")

def exibir_vendas(venda_mensal, cor_tit, cor_inf):

    ano_atual = venda_mensal[0][0]
    string1 = f"{cor_inf}Ano: {ano_atual}"

    print(f"{string1}")

    for ano, mes, quantidade in venda_mensal:
        if ano != ano_atual:
            ano_atual = ano
            print(f"{string1}")

        print(f"    {LISTA_MESES[mes]} - {quantidade} cópia", end = '')
        print("s vendidas" if quantidade > 1 else " vendida")

# ----------------------------------------------------------------------------#

def imprimir_bem_vindo():
    print(f"      ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷")
    print(f"      ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇")
    print(f"      ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽")
    print(f"      ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕")
    print(f"      ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕")
    print(f"      ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕")
    print(f"      ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄")
    print(f"      ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕")
    print(f"      ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿")
    print(f"      ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print(f"      ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟")
    print(f"      ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠")
    print(f"      ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙")
    print(f"      ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣")
    print(f"      ⡆⠉⠉⠉⠉⠉⠉ マンガリスト。⠉⠉⠉⠉⠉⠉⠉⠙")
    print(f"      ⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈")
    print(f"      \n Seja bem-vinde ao MangaList!\n")

def imprimir_menu():
    print(f"      ⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈")
    print(f"      ⡫                             ⡣")
    print(f"      ⡫   O que você deseja fazer?  ⡣")
    print(f"      ⡫   Escolha uma opção:        ⡣")
    print(f"      ⡫                             ⡣")
    print(f"      ⢱ 1.  Adicionar um mangá      ⢗")
    print(f"      ⢄ 2.  Visualizar todos mangás ⣈")
    print(f"      ⡀ 3.  Visualizar um mangá     ⠁")
    print(f"      ⡄ 4.  Editar um mangá         ⠼")
    print(f"      ⢱ 5.  Excluir um mangá        ⢗")
    print(f"      ⡀ 6.  Visualizar gráfico 1    ⠁")
    print(f"      ⡄ 7.  Visualizar gráfico 2    ⠼")
    print(f"      ⢄ 8.  Visualizar gráfico 3    ⣈")
    print(f"      ⡄ 9.  Visualizar gráfico 4    ⠼")
    print(f"      ⡆ 10. Sair                    ⣌")
    print(f"      ⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈")

def imprimir_busca_manga():
    print(f"\n\n\n")
    print("⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⠛⠉⣉⣀⣀⣈⠉⠻⠿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿")
    print("⣿⠛⠁⣠⣤⣤⣤⣄⠈⠋⠁⠠⣾⡿⠛⠛⣿⣿⡄⠄⠄⠄⠠⣴⣶⣦⣤⡀⠙⢿")
    print("⠃⢰⣿⠿⠛⠛⢿⣿⡇⠄⠄⠄⠄⠄⠄⢀⣾⡿⠁⠄⠂⠂⠄⠘⠉⠙⠻⣿⣦⠈")
    print("⣦⣤⣀⣀⠈⢠⣿⡿⠁⠄⠄⠄⠄⠄⢸⣿⡏⠄⠄⠄⠄⠄⠄⠁⣠⣴⣾⣿⠏⢠")
    print("⣿⣿⣿⣿⠄⠿⠟⠄⠄⠄⠄⠄⠄⠄⣠⣤⡄⠄⠄⠄⠄⠄⢀⣈⠛⠋⠉⠄⢠⣾")
    print("⣿⣿⣿⡏⠄⢰⣿⣶⠄⠄⠄⠄⠄⠄⠙⠿⠃⠄⠄⠄⠄⠄⠿⣿⡇⠄⠄⠄⠄⣿")
    print("⣿⣿⣿⠄⠄⡈⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿")
    print(f"⣿⣿⣷⠄⠄⢉⠄⠄⠄⠄⠄⠐⠦⡘⠿⠿⣿⡿⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿     {CIANO}-----------{RESET}" )
    print(f"⣿⣿⡟⠈⠄⠄⠄⠄⢰⣄⠄⠠⠄⠄⠄⢀⡌⠁⠄⠄⠄⣹⠟⡁⠄⠄⠄⠄⣸⣿   {CIANO}/             |{RESET}" )
    print(f"⣿⣿⠇⠄⠄⠄⠄⠄⢸⣿⣿⣷⣦⡤⣾⣿⣷⢄⣀⣀⣠⣶⣿⠁⠄⠄⠄⢠⣿⣿  {CIANO}/     Digite   |{RESET}" ) 
    print(f"⣿⣿⣤⣶⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⠻⢿⠿⢻⣿⣿⣿⣿⡍⠄⠄⠄⣴⣿⣿⣿ {CIANO}<   abaixo o ID |{RESET}" )
    print(f"⣿⣿⣿⣿⠄⠄⠄⠄⠘⣿⣿⡟⠄⠄⠄⠄⠄⠉⠛⠻⣿⣿⠁⠄⠄⢸⣿⣿⣿⣿  {CIANO}\   do mangá   |{RESET}" )
    print(f"⣿⣿⣯⣉⣀⠄⠄⠄⠄⢿⣿⣆⣼⣿⠲⠲⠶⢦⣄⡀⠻⡏⠄⠄⠰⣼⣿⣿⣿⣿   {CIANO}\             |{RESET}" )
    print(f"⣿⣿⣿⣿⣿⡄⠠⠄⠄⠄⠻⢝⠿⣿⣿⣿⣷⣶⠟⢃⡄⠁⠄⠄⠸⣾⡿⣿⣿⣿     {CIANO}-----------{RESET}" )
    print(f"⡿⠟⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠁⠚⠋⠁⠄⠄⠄⠄⠒⠿⣿⣿⣿\n")

def exibir_valores_dicionario(id, nome, autor, status, ano_inicio, ano_fim,
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
    print(f"\n{cor_sep}(¸.•´ (¸.•´ .•´ ¸.•´ .•´ ¸¸.•¨¯`•.•´¯¨•.¸¸ `•. `•.¸ `•. `•.¸) `•.¸){cor_inf}")
    
def imprimir_msg_nao_encontrado(ID):
        print(f"\n\n" )
        print(f"    ,.  ,.                       {VERMELHO}(｡╯︵╰｡){RESET}" )
        print(f"    ||  ||           {VERMELHO}-----------------------------------{RESET}" )
        print(f"   ,''--''.        {VERMELHO}/                                    |{RESET}" )
        print(f"  : (.)(.) :      {VERMELHO}/  O mangá com o ID:                  |{RESET}" )
        print(f" ,'   ︵   `.   {VERMELHO}<    {NEGRITO}{ID}{RESET}" )
        print(f" :          :     {VERMELHO}\  NÃO foi encontrado.                |{RESET}" )
        print(f" :          :      {VERMELHO}\                                    |{RESET}" )
        print(f" `._m____m_,'        {VERMELHO}-----------------------------------{RESET}" )
        print(f"\n\n{RESET}" )

# ----------------------------------------------------------------------------#