#Caso de Uso:
# Sistema de Recomendação de Conteúdo #################
# Imagine um sistema de recomendação de conteúdo para uma plataforma de streaming.
#As condicionais podem ser utilizadas para personalizar as recomendações com base nas
#preferências de idade do usuário. Por exemplo, um usuário jovem pode receber recomendações
#de filmes e séries animadas, enquanto um usuário adulto pode receber sugestões de dramas e documentários.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
idade = int(input("Digite sua idade: "))
if idade < 13:
    print("Recomendamos desenhos animados e filmes educativos.")
elif idade < 18:
    print("Recomendamos séries adolescentes e filmes de aventura")
elif idade < 60:
    print("Recomendamos dramas, documentários e thrillers.")
else:

    print("Recomendamos clássicos e filmes com temáticas históricas.")    
