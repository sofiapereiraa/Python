status = 1
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print ("\n")
print ("Banco Central")
print ("----------------")
print("Bem-vindo ao simulador do Banco Central! Por favor, digite seu saldo para começarmos o programa.")
saldo = float (input ("Saldo: "))
input("Pressione Enter para continuar...")

while status:
    limpar_tela()
    print ("Banco Central")
    print ("----------------")
    print ("1- Saldo")
    print ("2- Deposito")
    print ("3- Saque")
    print ("4- Sair")
    opcao = input ("Escolha uma das opções (1-4): ")

    match opcao:
        case "1":
            limpar_tela()
            print ("=== Saldo ====")
            print (f"Seu saldo atual é de: {saldo:.2f} Reais")
            input("Pressione Enter para continuar...")
        case "2":
            print ("=== Depósito ===")
            deposito = float (input ("Digite o valor do depósito: "))
            if deposito <= 0:
             print ("Digite um valor maior que zero ! ")
             input("Pressione Enter para continuar...")
            else:
             saldo = saldo + deposito
             print (f"Seu saldo atual: {saldo:.2f}")
             input("Pressione Enter para continuar...")
        case "3":
             limpar_tela()
             print("=== Saque ===")
             saque = float(input("Digite o valor do saque: "))
             if saque <= 0:
               print("Digite um valor maior que zero!")
               input("Pressione Enter para continuar...")
             elif saque > saldo:
               print("Valor de saque inválido! Saldo insuficiente.")
               input("Pressione Enter para continuar...")
             else:
               saldo = saldo - saque
               print(f"Seu saldo atual: {saldo:.2f}")
               input("Pressione Enter para continuar...")
        case "4":
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




           
