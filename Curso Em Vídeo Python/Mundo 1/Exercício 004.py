#Exercício 4

n = input('Escreva qualquer coisa e mostraremos suas classificações: ')

print("""O tipo primitivo desse valor é: {}
Contém somente letras? {}
Contém somente números? {}
Contém somente letras e números? {}
Contém somentes dígitos? {}
Está em minúsculo? {}
Está em maisúsculo? {}
Está capitalizada? {}""".format(type(n), n.isalpha(), n.isnumeric(), n.isalnum(), n.isdigit(), n.islower(), n.isupper(), n.istitle()))
