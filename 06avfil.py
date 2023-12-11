# criação de uma lista e de um variavel
intero= []
soma = 0
# uso do for para estrutura de repetição
for i in range(6):
    num= float(input("digite o número:"))
    if num>0:
        # adicionar os valores na lista
        intero.append(num)
#    cálculo para a média dos números maiores do que 0.s
    soma= sum(intero)
quantidade=len(intero)
media= soma/quantidade
print(f"{quantidade} valores positivos.\n{media}")

