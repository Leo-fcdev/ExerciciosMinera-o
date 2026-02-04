"""
A sua professora de Física passou uma questão
sobre velocidade média. Ela explicou que a velocidade
média de um corpo, por exemplo, um carro, é calculada
dividindo a distância percorrido (em metros) pela
quantidade de tempo (em segundos).
Desse modo, a velocidade = distancia / tempo.
Você que não é besta foi logo fazendo um programa
que calculasse a velocidade média, apenas lendo a
distância percorrida e o tempo gastado para percorrê-lo.
"""

distancia = float(input("Qual a distancia percorrida (em metros)? "))
tempo = float(input("Qual o tempo foi gasto pra percorrer essa distancia (em segundos)?"))
veloMedia = distancia / tempo

print(f"A velocidade media é de {veloMedia} m/s")