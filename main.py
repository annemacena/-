from globais import EMOJI_OPCAO
from helper import construir_dicionario, imprimir_bem_vindo, imprimir_menu
from funcionalidade import adicionar_manga, exibir_dicionário_completo, buscar_manga, atualizar_manga, deletar_manga
from arquivo import ler_arquivo

dic_mangas = construir_dicionario(ler_arquivo())

def main():
    imprimir_bem_vindo()

    opcao = ""

    while(opcao != "10"):
        imprimir_menu()   
        opcao = input(EMOJI_OPCAO)

        if(opcao != "10"): 

            if(opcao == "1"): # adicionar um mangá
                adicionar_manga(dic_mangas)

            elif(opcao == "2"): # visualizar todos os mangás
                exibir_dicionário_completo(dic_mangas)

            elif(opcao == "3"): # visualizar um mangá
                buscar_manga(dic_mangas)

            elif(opcao == "4"): # editar um mangá
                atualizar_manga(dic_mangas)

            elif(opcao == "5"): # excluir um mangá
                deletar_manga(dic_mangas)

            elif(opcao == "6"): # visualizar gráfico 1
                print("\n-\n")
            elif(opcao == "7"): # visualizar gráfico 1
                print("\n-\n")
            elif(opcao == "8"): # visualizar gráfico 1
                print("\n-\n")
            elif(opcao == "9"): # visualizar gráfico 1
                print("\n-\n")
            else:
                print("\n  Opção inválida (╯°益°)╯彡┻━┻\n")

        else:
            print("\n  。。。ミヽ(。＞＜)ノ Saindo...")


    print("\n  byebye (｡•́︿•̀｡)")


main()

