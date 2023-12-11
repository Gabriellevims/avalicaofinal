print("O seu novo salário")
# entrada do dado
salarioatual= float(input("Digite seu salário atual:"))
# verificação dos salários e reajuste dos salários 
if salarioatual > 0 and salarioatual<=400:
    x1= salarioatual*0.15
    print(f"novo salário:{x1+salarioatual}\nReajuste ganho:{x1}\nEm porcentual:15%")
elif salarioatual >= 400.01 and salarioatual<=800.00:
    x2= salarioatual*0.12
    print(f"novo salário:{x2+salarioatual}\nReajuste ganho:{x2}\nEm porcentual:12%")
elif salarioatual >= 800.01 and salarioatual<=1200.00:
    x3= salarioatual*0.10
    print(f"novo salário:{x3+salarioatual}\nReajuste ganho:{x3}\nEm porcentual:10%")
elif salarioatual >= 1200.01 and salarioatual<=2000.00:
    x4= salarioatual*0.07
    print(f"novo salário:{x4+salarioatual}\nReajuste ganho:{x4}\nEm porcentual:7%")
else:
    x5=salarioatual*0.04
    print(f"novo salário:{x5+salarioatual}\nReajuste ganho:{x5}\nEm porcentual:5%")

