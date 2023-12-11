print("Quanto de imposto você tem que pegar?")
# entrada de dado
salario= float(input("Digite seu salário atual:"))
# verificação do imposto de acordo com o salário da pessoa
if salario > 0 and salario<=2000.00:
    print(f"Inseto de impoto")
elif salario>= 2000.01 and salario<=3000.00:
    x1= salario*0.08
    print(f"Você deve pagar:{x1:.2f}")
elif salario>=3000.01 and salario<=4500.00:
    x2=salario*0.18
    print(f"Você deve pagar:{x2:.2f}")
else:
    x3= salario*0.28
    print(f"Você deve pagar:{x3:.2f}")

    

