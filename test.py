import math

concetracao_proton = 0.01 #mol/L 

pH = -1*math.log(concetracao_proton, 10)
pH = round(pH,2)

print(pH)

