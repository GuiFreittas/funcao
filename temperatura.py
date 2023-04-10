def ler_temperatura():
    celsius = float(input("Digite a temperatura em Celsius: "))
    return celsius

def converter_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrar_resultado(fahrenheit):
    print("A temperatura em Fahrenheit é:", fahrenheit)

temperatura_celsius = ler_temperatura()
temperatura_fahrenheit = converter_para_fahrenheit(temperatura_celsius)
mostrar_resultado(temperatura_fahrenheit)
