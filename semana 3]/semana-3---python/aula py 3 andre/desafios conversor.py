
def celsius_para_fahrenheit(c):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return c * 9 / 5 + 32


temperatura = float(input("Temperatura em °C: 2 "))
print(f"Temperatura em °F: {celsius_para_fahrenheit(temperatura):.1f}")


