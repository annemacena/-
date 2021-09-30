import matplotlib.pyplot as plt
from globais import LISTA_MESES
from globais import AMARELO_N, VERDE_N, CIANO_N, VERMELHO_N, AZUL_N, RESET

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
        if(isinstance(atributos_manga[3], int)):
            atributos_manga[3] = int(atributos_manga[3])
        if(isinstance(atributos_manga[4], int)):
            atributos_manga[4] = int(atributos_manga[4])
        if(isinstance(atributos_manga[6], int)):
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
            print(f"{AMARELO_N}ID repetido, por favor insira outro ID.{RESET}")
            return True
    
    return False
# ------------------------------------ID--------------------------------------#
# pede um novo ID ao usuário para cadastro e checa o valor desse ID
def adicionar_id(dic_mangas):

    flag_id_repetido = True
    while flag_id_repetido == True:
        id = input((f"{AZUL_N}Entre com o ID único do novo mangá:{RESET} "))
        flag_id_repetido = checar_id(id, dic_mangas)
        
    return id


# ----------------------------------------------------------------------------#
# ----------------------------------STATUS------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o status recebido é válido: Completo ou Andamento ou Cancelado ou Hiato
def checar_status(status):

    if status == "COMPLETO" or status == "ANDAMENTO" or status == "CANCELADO" or status == "HIATO":
        return True

    print(f"{AMARELO_N}Status incorreto, por favor insira um status válido.{RESET}")   
    return False
# ----------------------------------STATUS------------------------------------#
# pede o status do mangá ao usuário e checa se é válido
def adicionar_status(cor):
    
    flag_status_valido = False
    while flag_status_valido == False:
        status = input((f"{cor}Entre com o status do mangá - Completo ou Andamento ou Cancelado ou Hiato - :{RESET} "))
        flag_status_valido = checar_status(status.upper())
        
    return status.capitalize()


# ----------------------------------------------------------------------------#
# -------------------------------ANO DE INICIO--------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_inicio(ano_inicio):

    if ano_inicio >= 0:
        return True
    
    print(f"{AMARELO_N}O ano do início da publicação não é válido, por favor insira um ano válido.{RESET}")   
    return False
# -------------------------------ANO DE INICIO--------------------------------#
# pede o ano que o mangá começou a ser publicado e checa se é válido
def adicionar_ano_inicio(cor):
    
    flag_ano_inicio_valido = False
    while flag_ano_inicio_valido == False:
        ano_inicio = int(input((f"{cor}Entre com o ano que o mangá começou a ser publicado:{RESET} ")))
        flag_ano_inicio_valido = checar_ano_inicio(ano_inicio)
        
    return ano_inicio


# ----------------------------------------------------------------------------#
# --------------------------------ANO DE FIM----------------------------------#
# ----------------------------------------------------------------------------#
# checa se o ano recebido é válido
def checar_ano_fim(ano_fim, ano_inicio):

    if ano_fim >= ano_inicio:
        return True
    
    print(f"{AMARELO_N}O ano de termino da publicação não pode ser menor que {ano_inicio}, por favor insira um ano válido.{RESET}")   
    return False
# --------------------------------ANO DE FIM----------------------------------#
# pede o ano que o mangá terminou de ser publicado e checa se é válido
def adicionar_ano_fim(status, ano_inicio, cor):
    
    # Se o mangá estiver em Andamento ou em Hiato,
    # ele ainda não terminou de ser publicado
    if status == "Andamento" or status == "Hiato":
        return 'None'
    
    # status == "Completo" or status == "Cancelado"
    flag_ano_fim_valido = False
    while flag_ano_fim_valido == False:
        ano_fim = int(input((f"{cor}Entre com o ano que o mangá terminou de ser publicado:{RESET} ")))
        flag_ano_fim_valido = checar_ano_fim(ano_fim, ano_inicio)
        
    return ano_fim


# ----------------------------------------------------------------------------#
# -----------------------------NUMERO DE VOLUMES------------------------------#
# ----------------------------------------------------------------------------#
# checa se o número de volumes é válido
def checar_num_volumes(num_de_volumes):

    if num_de_volumes >= 1:
        return True
    
    print(f"{AMARELO_N}O número de volumes não é válido, por favor insira um valor válido.{RESET}")   
    return False
# -----------------------------NUMERO DE VOLUMES------------------------------#
# pede o número de volumes do mangá e checa se é esse número é válido
def adicionar_num_volumes(cor):
    
    flag_num_volumes_valido = False
    while flag_num_volumes_valido == False:
        num_de_volumes = int(input((f"{cor}Entre com a quantidade de volumes que o mangá possui:{RESET} ")))
        flag_num_volumes_valido = checar_num_volumes(num_de_volumes)
        
    return num_de_volumes


# ----------------------------------------------------------------------------#
# ---------------------------------PUBLICO------------------------------------#
# ----------------------------------------------------------------------------#
# checa se o publico recebido é válido: Shojo ou Josei ou Shonen ou Seinen
def checar_publico(publico):

    if publico == "SHOJO" or publico == "JOSEI" or publico == "SHONEN" or publico == "SEINEN":
        return True
    
    print(f"{AMARELO_N}Público incorreto, por favor insira o publico correto.{RESET}")   
    return False
# ---------------------------------PUBLICO------------------------------------#
# pede o publico do mangá ao usuário e checa se é válido
def adicionar_publico(cor):
    
    flag_publico_valido = False
    while flag_publico_valido == False:
        publico = input((f"{cor}Entre com o público alvo do mangá - Shojo ou Josei ou Shonen ou Seinen - :{RESET} "))
        flag_publico_valido = checar_publico(publico.upper())
        
    return publico.capitalize()


# ----------------------------------------------------------------------------#
# ----------------------------------GENERO------------------------------------#
# ----------------------------------------------------------------------------#
# pede o genero do mangá ao usuário
def adicionar_genero(genero, cor):
    
    flag_adicionar_genero = True
    while flag_adicionar_genero == True:
        gen = input((f"{cor} Entre com 1 gênero do mangá (Ex: Ação):{RESET} "))
        gen = gen.capitalize()
        
        if gen in genero:
            print(f"{AMARELO_N}O gênero {gen} já está cadastrado!{RESET}")
        else:
            genero.append(gen)
            print(f"{VERDE_N}{gen} adicionado!{RESET}", end = '')
        
        continua = input((f"{AZUL_N} Digite 'n' caso não deseje cadastrar outro gênero:{RESET} "))
        if continua == "n":
            flag_adicionar_genero = False


# ----------------------------------------------------------------------------#
# ------------------------------VENDAS MENSAIS--------------------------------#
# ----------------------------------------------------------------------------#
# Adiciona as vendas mensais
def adicionar_vendas_mensais(venda_mensal, ano_inicio, cor):
    
    print(f"\n{VERDE_N} Início do cadastro de vendas mensais do mangá.{RESET}")

    flag_cadastrar_venda = True
    while flag_cadastrar_venda == True:
        ano_venda = int(input(f"{cor} Entre com o ano:{RESET} "))
        
        while ano_venda < ano_inicio:
            print(f"{AMARELO_N}Ano inválido! O mangá começou a ser publicado em {ano_inicio}.{RESET}")
            ano_venda = int(input(f"{cor}Entre com um ano válido:{RESET} "))
        
        print(f"\n{cor} Entre com o número do mês", end = '')
        mes_venda = int(input(f"1 - Jan, 2 - Fev, 3 - Mar, ..., 10 - Out, 11 - Nov, 12 - Dez:{RESET} "))
        
        while mes_venda < 1 or mes_venda > 12:
            print(f"{AMARELO_N}Mês inválido! 1 - Jan, 2 - Fev, 3 - Mar, 4 - Abr, 5 - Mai, 6 - Jun, 7 - Jul, 8 - Ago, 9 - Set, 10 - Out, 11 - Nov, 12 - Dec{RESET}")
            mes_venda = int(input(f"{cor}Entre com um mês válido:{RESET} "))
              
        flag_continua_cadastro = True
        for ano, mes, qtd in venda_mensal:
            if ano_venda == ano and mes_venda == mes:
                print(f"{AMARELO_N} OPA! As vendas de {LISTA_MESES[mes_venda]} de {ano_venda} já foram cadastradas!!{RESET}")
                flag_continua_cadastro = False
        
        if flag_continua_cadastro == True:
            
            quantidade = int(input(f"{cor} Entre com a quantidade de cópias vendidas em {LISTA_MESES[mes_venda]} de {ano_venda}:{RESET} "))
            
            while quantidade < 0 :
                print(f"{AMARELO_N}O número de vendas não pode ser negativo!{RESET}")
                quantidade = int(input(f"{cor}Entre com o número de vendas mensal válido:{RESET} "))

            venda_mensal.append([ano_venda, mes_venda, quantidade])
        
        continua = input((f"{cor} Digite 'n' caso não deseje cadastrar outra venda:{RESET} "))

        if continua == "n":
            flag_cadastrar_venda = False
        
    venda_mensal.sort()

def obter_atributos_manga():
    
    cor = AZUL_N
    
    nome = input((f"{cor}Entre com o nome do mangá:{RESET} "))
    autor = input((f"{cor}Entre com o nome do autor do mangá:{RESET} "))
    status = adicionar_status(cor)
    ano_inicio = adicionar_ano_inicio(cor)
    ano_fim = adicionar_ano_fim(status, int(ano_inicio), cor)
    sinopse = input((f"{cor}Entre com a sinopse do mangá:{RESET} "))
    num_de_volumes = adicionar_num_volumes(cor)
    publico = adicionar_publico(cor)
    genero = []
    adicionar_genero(genero, cor)
    impressao = input((f"{cor}Entre com a gráfica de impressão do mangá:{RESET} "))
    revista = input((f"{cor}Entre com a revista de publicação do mangá:{RESET} "))
    venda_mensal = []
    adicionar_vendas_mensais(venda_mensal, int(ano_inicio), cor)
    print("\n")

    return [nome, autor, status, ano_inicio, ano_fim, sinopse, num_de_volumes, publico, genero, impressao, revista, venda_mensal]

# ----------------------------------------------------------------------------#
# -----------------------------PRINTAR DICIONÁRIO-----------------------------#
# ----------------------------------------------------------------------------#
def exibir_ano_final(ano_final, status, cor_tit, cor_inf):
    
    if status == "Completo" or status == "Cancelado":
        print(f"{cor_tit}Ano final de publicação: {cor_inf}{ano_final}")

def exibir_vendas(venda_mensal, cor_tit, cor_inf):
    

    ano_atual = venda_mensal[0][0]
    print(f"{cor_inf}Ano: {ano_atual}")

    for ano, mes, quantidade in venda_mensal:
        if ano != ano_atual:
            ano_atual = ano
            print(f"{cor_inf}Ano: {ano_atual}")

        print(f"    {LISTA_MESES[mes]} - {quantidade} cópia", end = '')
        print(f"s vendidas" if quantidade > 1 else " vendida")  
        
        
# ----------------------------------------------------------------------------#


# ----------------------------------------------------------------------------#
# -------------------------------PLOTAR GRÁFICO-------------------------------#
# ----------------------------------------------------------------------------#
def plotar_grafico_venda_anual(lista_venda, ano_venda, nome):
    
    #lista_venda.sort()
    
    x = []
    y = []
    for ano, mes, qtd in lista_venda:
        if ano == ano_venda:
            x.append(mes)
            y.append(qtd)
    
    if not x == []:
        plt.bar(x, y, width = 0.5, color = '#f59d45')
        plt.title(f"Venda de {ano_venda} do mangá {nome}")
        plt.ylabel(f"Quantidade de volumes vendidos")
        plt.xlabel(f"Mês")
        plt.xticks([tam + 1.0 for tam in range(12)], ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], rotation=90)
        plt.show()
    else:
        print(f"\n{AMARELO_N}Não existe nenhum registro de venda nesse ano.{RESET}")
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
def plotar_grafico_venda_total(lista_venda, nome):
    
    #lista_venda.sort()
    
    ano_atual = lista_venda[0][0]
    qtd_anual = 0
    
    x = []
    y = []
    flag_adc = True
    for ano, mes, qtd in lista_venda:
        if ano_atual == ano:
            qtd_anual += qtd
            flag_adc = True
        else:
            x.append(str(ano_atual))
            y.append(qtd_anual)
            ano_atual = ano
            qtd_anual = qtd
            flag_adc = False
    
    if flag_adc == True:
        x.append(str(ano_atual))
        y.append(qtd_anual)
    
    if len(x) == 1:
        print(f"{AMARELO_N}Apenas um ano foi cadastrado. Aconselho plotar o gráfico de venda anual da opção 6.{RESET}")
    elif not x == []:
        '''x.append(str(ano_atual))
        y.append(qtd_anual)'''
    
        plt.plot(x, y, color = '#a80be0')
        plt.title(f"Venda ao longo do tempo do mangá {nome}")
        plt.ylabel("Quantidade de volumes vendidos")
        plt.xlabel("Ano")
        plt.show()
    else:
        print(f"\n{AMARELO_N}Não existe nenhum registro de venda para esse mangá.{RESET}")
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
def plot_grafico_genero(dic_mangas):
    
    lista_generos = [dic_mangas[chave][8] for chave in dic_mangas]
    
    generos = []
    for linha in lista_generos:
        for valor in linha:
            generos.append(valor)
   
    dic_generos = {i:generos.count(i) for i in generos}
    
    x = []
    y = []
    for chave in dic_generos:
        y.append(chave)
        x.append(dic_generos[chave])
    
    fig, ax1 = plt.subplots()
    ax1.barh(y, x, color = '#c42929')
    ax1.set_title("Gênero x Quantidade")
    ax1.set_ylabel("Gêneros")
    ax1.set_xlabel("Quantidade")
    ax1.set_xticks(x)
    plt.show()
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
def plot_grafico_publico(dic_mangas):
    
    lista_publico = [dic_mangas[chave][7] for chave in dic_mangas]
    
    qtd_shojo = lista_publico.count('Shojo')
    qtd_josei = lista_publico.count('Josei')
    qtd_shonen = lista_publico.count('Shonen')
    qtd_seinen = lista_publico.count('Seinen')
    
    opcoes = ('Shojo', 'Josei', 'Shonen', 'Seinen')
    qtd = (qtd_shojo, qtd_josei, qtd_shonen, qtd_seinen)
    cores = ('hotpink', '#ffcc99', '#66b3ff', '#99ff99')
    
    fig1, ax1 = plt.subplots()
    #explsion
    explode = (0.05,0.05,0.05,0.05)
    ax1.pie(qtd, colors = cores, labels = opcoes, autopct = '% 1.1f %%', startangle = 45,pctdistance=0.85, explode = explode)

    circulo_do_meio = plt.Circle((0,0), 0.70, fc = 'white') 
    fig = plt.gcf() 
    fig.gca().add_artist(circulo_do_meio)
    
    ax1.axis('equal')  
    plt.tight_layout()
    plt.legend(title = "Público")
    plt.show()
    
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#


def imprimir_bem_vindo():
    print(f"\n      ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷")
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
    print(f"\n      Seja bem-vinde ao MangaList!\n")

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
    print(f"      ⡀ 6.  Gráfico de venda        ⠁")
    print(f"      ⡄     anual de um mangá       ⠁")
    print(f"      ⡄ 7.  Gráfico de vendas de um ⠼")
    print(f"      ⡀     mangá ao longo dos anos ⠁")
    print(f"      ⢄ 8.  Gráfico de proporção    ⣈")
    print(f"      ⡀     dos gêneros cadastrados ⠁")
    print(f"      ⢱ 9.  Gráfico de proporção    ⣈")
    print(f"      ⡀     do público alvo         ⠁")
    print(f"      ⣌ 10. Sair                    ⣌")
    print(f"      ⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈⢐⢕⢐⢕⢕⠈")

def imprimir_busca_manga():
    print(f"\n")
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
    
def imprimir_msg_nao_encontrado(id):
        print(f"\n\n" )
        print(f"    ,.  ,.                       {VERMELHO}(｡╯︵╰｡){RESET}" )
        print(f"    ||  ||           {VERMELHO}-----------------------------------{RESET}" )
        print(f"   ,''--''.        {VERMELHO}/                                    |{RESET}" )
        print(f"  : (.)(.) :      {VERMELHO}/  O mangá com o ID:                  |{RESET}" )
        print(f" ,'   ︵   `.   {VERMELHO}<    {NEGRITO}{id}{RESET}" )
        print(f" :          :     {VERMELHO}\  NÃO foi encontrado.                |{RESET}" )
        print(f" :          :      {VERMELHO}\                                    |{RESET}" )
        print(f" `._m____m_,'        {VERMELHO}-----------------------------------{RESET}" )
        print(f"\n\n{RESET}" )

# ----------------------------------------------------------------------------#