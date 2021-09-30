from funcionalidade import *
from helper import construir_dicionario, imprimir_bem_vindo, imprimir_menu
from arquivo import ler_arquivo
from globais import EMOJI_OPCAO, CIANO_N, AMARELO_N, RESET

if __name__ == '__main__':
    
    dic_mangas = construir_dicionario(ler_arquivo())
    
    imprimir_bem_vindo()
    
    opcao = ""
    
    cor = CIANO_N
    
    while(opcao != "10"):
        
        imprimir_menu()
        
        print(f"\n{cor}")
        print(f"  --------------------------")
        print(f"//  Digite a opção abaixo  //")
        print(f"  --------------------------{RESET}")
            
        flag_imprimir_menu = True
        opcao = input(f"{cor}{EMOJI_OPCAO}{RESET}")

        if(opcao != "10"): 

            if(opcao == "1"): # adicionar um mangá
                adicionar_manga(dic_mangas)
                dic_mangas = construir_dicionario(ler_arquivo())

            elif(opcao == "2"): # visualizar todos os mangás
                exibir_dicionário_completo(dic_mangas)

            elif(opcao == "3"): # visualizar um mangá
                buscar_manga(dic_mangas)

            elif(opcao == "4"): # editar um mangá
                atualizar_manga(dic_mangas)
                dic_mangas = construir_dicionario(ler_arquivo())

            elif(opcao == "5"): # excluir um mangá
                deletar_manga(dic_mangas)
                dic_mangas = construir_dicionario(ler_arquivo())

            elif(opcao == "6"): # visualizar gráfico de venda anual
                visualizar_grafico_vendas_anuais(dic_mangas)
                
            elif(opcao == "7"): # visualizar gráfico de vendas totais
                visualizar_grafico_vendas_totais(dic_mangas)
                
            elif(opcao == "8"): # visualizar gráfico de gênero
                visualizar_grafico_genero(dic_mangas)
                
            elif(opcao == "9"): # visualizar gráfico de público alvo
                visualizar_grafico_publico(dic_mangas)
                
            else:
                print(f"\n{AMARELO_N}  Opção inválida (╯°益°)╯彡┻━┻\n       Digite um número de 1 a 10!{RESET}\n")
                flag_imprimir_menu = True
                
            input(f"\n{AMARELO_N}Aperte Enter para continuar... {RESET}")
            print("\n\n\n")

        else:
            print("\n\n\n  。。。ミヽ(。＞-＜)ノ Saindo...")


    print("\n  byebye (｡•́︿•̀｡)")
