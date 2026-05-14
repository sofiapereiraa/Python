print ("Bem vindo a lista de compras")

print ("Lista 1")
compras = ["Carne", "Frango","Arroz","Feijão","Macarrão","Ovo","Sabão em pó"]
print (compras)

print ("Lista 2")
print ("Vamos adicionar UMA fruta a lista: ")
fruta = input("Digite uma fruta: ")
compras.append(fruta)
print (compras)

print ("Lista 3")
print ("Vamos adicionar várias frutas e vegetais a lista: ")
fruta = input("Digite suas frutas (separadas por vírgula): ")
frutas = fruta.split(",")
compras.extend(frutas)
print(compras)


