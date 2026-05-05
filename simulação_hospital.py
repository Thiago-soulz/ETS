import random
import math
import matplotlib.pyplot as plt

def X():
    if random.random() < 0.15:
        return random.randint(40,60)
    else:
        return random.randint(5,20)
    

N=10000
valores=[]

for i in range(N):
    valores.append(X())

media = sum(valores)/N
s=0
for j in valores:
    s+=((j - media)**2)
variancia = s/N
desvio = math.sqrt(variancia)

print(f"Média:{media}")
print(f"Desvio Padrão: {desvio}")

def y(n):
    soma = 0
    for i in range(n):
        soma+=X()
    return soma/n

medias = []


for i in range(N):
    medias.append(y(100))

plt.hist(medias,bins=30)

plt.show()

from scipy.stats import norm

media = 18
desvio = 4
x= 22

z = (x - media)/desvio

prob = 1 - norm.cdf(z)

print(f"A probabilidade de ser maior que 22 minutos é {round(prob*100,2)}%")