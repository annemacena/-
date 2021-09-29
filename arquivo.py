from globais import NOME_ARQUIVO
from helper import transformar_dicionario_em_lista

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
