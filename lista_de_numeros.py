def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média dos números na lista é:", media)
