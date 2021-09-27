NOME_ARQUIVO = "risuto.txt"
NOME_ARQUIVO_BACKUP = "risuto_backup.txt"

#   Helpers

def transformar_string_em_lista(registro_string, caractere_separador):
    '''
    Transforma uma string em array, dado um caractere separador. 
    
    Exemplo:
        registro_string = "[drama,girls love,erotica]"
        caractere_separador = ","
        retorno = ["drama", "girls love", "erotica"]

    Parâmetros
    ----------
    registro_string : str
        String a ser transformada em array.
    caractere_separador : str
        Caractere que é usado como separador da string passada por parâmetro (registro_string).

    Retorno
    -------
    array de string

    '''
    registro_lista = []
    registro_string = registro_string[1:len(registro_string)-1] # pega a string sem os colchetes
    return registro_string.split(caractere_separador)

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

        # os itens nos índices 9 e 12 são listas (gênero e venda mensal) 
        registro_dividido[9] = transformar_string_em_lista(registro_dividido[9], ",")
        registro_dividido[12] = transformar_string_em_lista(registro_dividido[12], ",")

        cont = 0
        # venda mensal é um lista de listas
        for venda_mensal in registro_dividido[12]:
            registro_dividido[12][cont] = transformar_string_em_lista(venda_mensal, "_")
            cont += 1
        cont = 0

        dicionario[registro_dividido[0]] = registro_dividido[1:]

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
            lista_atributos[11][cont] = adicionar_colchetes_string("_".join(venda_mensal))
            cont += 1
            
        lista_atributos[11] = adicionar_colchetes_string(",".join(lista_atributos[11]))

        registro_atual += ";".join(lista_atributos)
        
        lista_registros.append(registro_atual)

    return lista_registros

def ler_arquivo():
    '''
    Lê um arquivo e retorna seus dados num array de string.

    Retorno
    -------
    lista_registros: array de string
        Cada item do lista são dados de um registro (mangá).
    '''
    arquivo = open(NOME_ARQUIVO, "r", encoding='utf-8')
    registros = arquivo.readlines()
    lista_registros = []

    for linha in registros:
        lista_registros.append(linha.strip())

    arquivo.close()
    
    return lista_registros

def atualizar_arquivo(dic):
    '''
    Escreve num arquivo dados do dicionário passado por parâmetro.

    Parâmetros
    ----------
    dic : dictionary
    '''
    arquivo = open(NOME_ARQUIVO, "w", encoding='utf-8')
    lista_registros = transformar_dicionario_em_lista(dic)
    total_registros = len(lista_registros)
    cont = 1

    for registro in lista_registros:
        arquivo.write(registro)

        if(cont < total_registros):
            arquivo.write("\n")
        
        cont += 1

    arquivo.close()

#

def atualizar_manga(lista_novos_dados, dic, id):
    '''
    Atualiza item em dicionário passado por parâmetro. Os dados atualizados do dicionário também são atualizados no arquivo.

    Parâmetros
    ----------
    lista_novos_dados: array de string
        Cada item é um atributo do registro (mangá).
    dic : dictionary
    id: str
    '''
    dic[id] = lista_novos_dados
    atualizar_arquivo(dic)

def deletar_manga(dic, id):
    '''
    Deleta item em dicionário passado por parâmetro. Os dados atualizados do dicionário também são atualizados no arquivo.

    Parâmetros
    ----------
    dic : dictionary
    id: str
    '''
    dic.pop(id)
    atualizar_arquivo(dic)

def imprimir_menu():
    pass

registros = ler_arquivo()
dic_mangas = construir_dicionario(registros)

id_teste = "TESTE3"
dados_manga_nana = dic_mangas[id_teste]
dados_manga_nana[6] = "22" # volumes (atual é 21)

atualizar_manga(dados_manga_nana, dic_mangas, id_teste)

#deletar_manga(dic_mangas, id_teste)


