def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade, distancia, litros_usados):
    print("Tempo gasto na viagem:", tempo, "horas")
    print("Velocidade média durante a viagem:", velocidade, "km/h")
    print("Distância percorrida na viagem:", distancia, "km")
    print("Quantidade de litros utilizada na viagem:", litros_usados, "litros")

tempo, velocidade = ler_valores()
distancia = calcular_distancia(tempo, velocidade)
litros_usados = calcular_litros(distancia)
apresentar_resultado(tempo, velocidade, distancia, litros_usados)
