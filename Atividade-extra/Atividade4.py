# Atividade 4: Utilize a formatação de strings para criar uma mensagem personalizada.
# Recebendo informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

# Criando uma mensagem personalizada usando formatação de strings
mensagem = f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}. Seja bem-vindo!"

# Exibindo a mensagem personalizada
print(mensagem)