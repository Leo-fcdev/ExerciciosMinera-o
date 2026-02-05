"""
Uma loja de tintas deseja informar para os clientes o
melhor custo-benefício na compra de suas tintas.
Você foi contratado para desenvolver um programa que
deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00. Informe
ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício
de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.
"""
import array as arr
import math

capacidade =[18.0, 3.6]
preco = [80.0, 25.0]

area = float(input("Qual é a area em metros² que será pintada?"))
litrosNecessarios = area / 6

qtdLatas = math.ceil(litrosNecessarios / capacidade[0])
custoLata = qtdLatas * preco[0]

qtdGaloes = math.ceil(litrosNecessarios / capacidade[1])
custoGaloes = qtdGaloes * preco[1]

litrosFolga = litrosNecessarios * 1.1
mistaLata = int(litrosFolga // capacidade[0])

resto = litrosFolga % capacidade[0]

galoesMisto = math.ceil(resto / capacidade[1])

custoMistura = (mistaLata * preco[0]) + (galoesMisto * preco[1])

print(f"Opção 1 (Apenas Latas) custa R$ {custoLata:.2f}")
print(f"Opção 2 (Apenas Galões) custa R$ {custoGaloes:.2f}")
print(f"Opção 3 (Latas e Galões) custa R$ {custoMistura:.2f}")