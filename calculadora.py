print ("Bem vindo a minha calculadora básica no python !")
print ("Regras: Utileze as operações disponíveis (+,-,/,*)")
print ("Exemplo: 1 + 2")

n1 = float (input ("Digite o primeiro número: "))
n2 = float (input ("Digite o segundo número: "))
op = input ("Escolha seu operador:")



if op == "+":
    resultado = n1 + n2

elif op == "-":
    resultado = n1 - n2

elif op == "*":
    resultado = n1 * n2

elif op == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        print("Não pode dividir por zero!")
        resultado = None

else:
    print("Digite operadores válidos")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")











