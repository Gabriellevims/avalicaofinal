print("Quantos número pares tem?")
# criação de uma lista
quannu= []
# uso do for para estrutura de repetição e verificação dos númeoros
for i in range(5):
    num= int(input(f"Digite um número:"))
    if num %2 == 0:
        # Adicionar os números pares na lista
        quannu.append(num)
# conta a quantidade de intens na lista
par=len(quannu)
print(par)