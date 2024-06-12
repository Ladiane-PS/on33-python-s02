# Solicitar ao usuário para digitar dois números e mostrar qual é o maior
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

# Operações Aritméticas

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2

# Exibir os resultados 
print('\n Resultados das operações aritmeticas:')
print('Soma: ', soma)
print('Subtracção: ', subtracao)
print('multiplicação:' , multiplicacao)
print('Divisão:', divisao)
print('Divisão Inteira:', divisao_inteira)
print('Módulo: ', modulo)
print('Potência: ', potencia)

# Comparações com operadores

print('\nResultados das operações de comparação:')
print('Igualdade:', numero1== numero2)
print('Diferência:', numero1!= numero2)
print('Maior:', numero1 > numero2)
print('Menor ou igual:', numero1>= numero2)
print('Menor:', numero1 < numero2)
print('Menor ou igual:', numero1 <= numero2)




# Operadores de atribuição
print('\n Resultado dos Operadores de atribuição:')
numero1 += 5
print('número 1 += ', numero1)
numero2 /= 2
print('número 2 /=:', numero2)

#Verificar presença na lista de elementos
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if numero1 in lista_numeros:
    print(f'O número {numero1} está na lista de números')
else:
    print(f'O número {numero1} não está na lista de números') 
    
# Compare a identidade de objetos

x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('\n Resultados das operações de identidade de objetos:')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)





      

              
              