from traceback import print_tb


print("Composição corporal!")
peso=float(input("Digite seu Peso:"))
altura=float(input("Digite sua altura:"))
imc=(peso/(altura**altura))
print("Seu IMC é: %.2f" % imc)
if imc <16:
    print("Magreza leve!")
elif imc <17:
    print("Magreza Moderada!")
elif imc <18.5:
    print ("Magreza Leve!")
elif imc <25:
    print("Saudavel!")
elif imc <30:
    print("Sobre peso!")
elif imc <35:
    print ("Obesidade grau I!")
elif imc <40:
    print ("Obesidade grau II!(Severa)")
elif imc <45:
    print ("Obesidade grau III!(Grave)")