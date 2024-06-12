nome = input ('Digite seu nome: ')

idade = int(input('Digite a idade da aluna: '))
altura = float(input('Digite altura da aluna: '))
hobbies = input ('Digite os hobbies da aluna separada por vírgula: ')
hobbies1 = hobbies.split(',') # split torna uma lista de string, pode usar (, /)
endereco_rua = input('Digite o nome da rua da aluna: ')
endereco_numero = int(input('Digite o númeor da casa da aluna: '))
endereco_cidade = input('Digite a cidade da aluna: ')
endereco = (endereco_rua, endereco_numero, endereco_cidade) # criar uma tupla com o endereço - tupla não posso alterar 
email = input('Digite o email da aluna: ')
telefone = input('Digite o telefone da aluna: ')
contato = {'email': email, 'telefone': telefone} # cria um dicionário com o contato, quando utiliza conchete estou criando um dicionário


print('\nOlá, segue informações sobre a aluna:') # \n para pulara uma  linha 
print('Nome:' , nome)
print('Idade:' , idade)
print('Altura: ', altura)
print('Hobbies: ', hobbies1)
print('Endereço:', endereco)
print('Contato:', contato)
