lista_compras = ["leite", "pão", "queijo", "frutas", "peixe", "carne", "arroz", "legumes", "verduras"]

opcao = 0

while opcao != 4:
    print('''           [1] Ver lista de compras 
           [2] Adicionar item à lista
           [3] Remover item da lista
           [4] Sair ''')

    opcao = int(input("Seleciona uma das opções acima. "))

    if opcao == 1:
        print("Lista de compras:", lista_compras)

    elif opcao == 2:
        item = input("Digite o item que deseja adicionar à lista: ")
        lista_compras.append(item)
        print("Item adicionado à lista.")
        print("Lista de compras:", lista_compras)

    elif opcao == 3:
        item = input("Digite o item que deseja remover da lista: ")

        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido da lista.")
        else:
            print("Item não encontrado na lista.")

        print("Lista de compras:", lista_compras)

    elif opcao == 4:
        print("Saindo do programa, obrigada por usar!")

    else:
        print("Opção inválida.")