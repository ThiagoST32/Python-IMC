imc=22
Idade=45
MG=float(1.20*imc)+(0.23*Idade)-(10.8*1)-5.4 #Massa Gorda
print(MG)
print("Sua Massa Gorda é:" "%.2f" % MG)





if Sexo == "Feminino":
    MG=(1.20*imc)+(0.23*Idade)-(10.8*0)-5.4 #Massa Gorda Feminina
elif Sexo == "Masculino":
    MG=(1.20*imc)+(0.23*Idade)-(10.8*1)-5.4 #Massa Gorda Masculina
print("Sua Massa Gorda é:" "%.2f" % MG)