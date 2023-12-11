print("Descubra qual é a senha")
# criação da varial já com dados
senha= 2002 
# entrada do dado
des = int(input("Digite a senha:"))
# uso do while para verifica se a senha estão iguais
while des != senha:
    print("A senha esta invalida!")
    des = int(input("Digite a senha:"))
print("Acesso Permetido!")
