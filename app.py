#Este programa classifica se o consumo de água é economico
#Autor: Luan-S-Marin

import os

os.system("cls")

#entrada de dados do gasto de água mensal

print("=== Programa para classificação de consumo de água ===")
print("Este programa ira classificar se seu consumo é economico")

imovel = input("Digite o tipo do imóvel (casa/apartamento/comercial): ")
gasto_metros3 = int(input("Digite o gasto mensal em metros cubicos: ")) #variavel de gasto por metros cubicos


#processamento e saída de dados 
#classificação do tipo de consumo

if imovel == ("comercial"):
   print("tarifa comercial aplicada - consulte o plano corporativo")
elif imovel == ("casa" or "apartamento") and gasto_metros3 < 10:
   print ("Consumo econômico - excelente controle de água!")
elif gasto_metros3 >= 10 and gasto_metros3 < 25:
   print ("Consumo moderado - dentro do padrão residencial")
elif gasto_metros3 > 25:
   print ("Consumo excessivo - adote medidas de economia e verifique vazamentos")
else:
   print ("Erro - digite o seu tipo de imóvel e tente novamente")

   

