#Exemplo Prático:
# Classificação de Usuários por Idade ################################

# Vamos aplicar o conhecimento sobre estruturas condicionais para classificar usuários por faixa etária. Este exemplo demonstra como as condicionais podem ser usadas para direcionar o fluxo de um programa.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
idade = int(input("Digite sua idade: "))

# if idade <= 2:
#     categoria = "Bebê"
# elif idade < 13:
#     categoria = "Criança"
if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade <60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Você é classificado com: {categoria}")