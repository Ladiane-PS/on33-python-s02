# Atividade 3: Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Os números são iguais"

# Testando a função
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = maior_numero(numero1, numero2)
print(f"O maior número é: {resultado}")