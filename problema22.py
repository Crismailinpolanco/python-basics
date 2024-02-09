def decimal_a_binario(decimal):
    if decimal < 0:
        return "No se admiten números negativos en binario."
    elif decimal == 0:
        return "0b0"
    else:
        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal //= 2
        return "0b" + binario
def binario_a_decimal(binario):
    if not binario.startswith("0b"):
        return "Formato binario incorrecto. Debe comenzar con '0b'."
    else:
        binario = binario[2:]
        decimal = 0
        exp = len(binario) - 1

        for bit in binario:
            if bit == '1':
                decimal += 2 ** exp
            exp -= 1

        return decimal
# Convertir decimal a binario
numero_decimal = 25
binario_resultante = decimal_a_binario(numero_decimal)
print(f"{numero_decimal} en binario: {binario_resultante}")

# Convertir binario a decimal
numero_binario = "0b11001"
decimal_resultante = binario_a_decimal(numero_binario)
print(f"{numero_binario} en decimal: {decimal_resultante}")
