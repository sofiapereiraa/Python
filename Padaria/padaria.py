paoTrigo = 1.5
paoDoce = 1.7
coxinha = 3
cafe = 4.2
suco = 4
saladaFruta = 5
cuca = 6
status = 1
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while status:
    print ("Sistema de Padaria")
    print ("\n")
    print ("1- Cardapio")
    print ("2-Comprar produto")
    print ("3- Sair")

    opcao = input ("Escolha uma das opções (1-3): ")

    match opcao:
        case "1": 
            limpar_tela ()
            print ("\n")
            print ("=== Produtos ===")
            print ("Pão de trigo: ",paoTrigo)
            print ("Pão doce: ", paoDoce)
            print ("Coxinha: ", coxinha)
            print ("Copo de café: ", cafe)
            print ("Suco de fruta: ", suco)
            print ("Salada de Fruta: ",saladaFruta)
            print ("Cuca de banana: ",cuca)
            input("Pressione Enter para continuar...")
            limpar_tela ()
            
        case "2":
             limpar_tela ()
             print ("\n")
             print ("=== Produtos ===")
             print ("Pão de trigo: ",paoTrigo)
             print ("Pão doce: ", paoDoce)
             print ("Coxinha: ", coxinha)
             print ("Copo de café: ", cafe)
             print ("Suco de fruta: ", suco)
             print ("Salada de Fruta: ",saladaFruta)
             print ("Cuca de banana: ",cuca)
             input("Pressione Enter para continuar...")
             print ("\n")
             compra = input ("Digite o produto que deseja comprar: ")
             quantidade = int (input ("Digite a quantidade: "))
             preco = 0

             if compra == "pão de trigo":
                preco = paoTrigo
             if compra == "pão doce":
                preco = paoDoce
             if compra == "coxinha":
               preco = coxinha
             if compra == "café":
              preco = cafe
             if compra == "suco de fruta":
              preco = suco
             if compra == "salada de frutas":
              preco = saladaFruta
             if compra == "cuca de banana":
               preco = cuca

             conta = preco * quantidade
             print ("Preço da compra: ", conta)
             input("Pressione Enter para continuar...")
             limpar_tela ()

        case "3":
          limpar_tela ()
          print ("Saindo do programa ! ")
          input("Pressione Enter para continuar...")
          limpar_tela ()
          break
        case _:
           limpar_tela ()
           print("Digite uma opção válida!")
           input("Pressione Enter para continuar...")
           limpar_tela ()
    
