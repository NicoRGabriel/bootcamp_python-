# Type Error

# try:
#     numero_01 = int(input("insira um número: "))
#     numero_02 = int(input("insira outro número: "))
#     resultado = numero_01 // numero_02
#     print(resultado)
# except:
#     print("integer divicion or modulo by zero")


try:
    numero = int(input("insira um numero:"))
    if isinstance(numero, int):
        print("a variavel é um inteiro")
    else:
        print("a variavel não é um inteiro")
except:
    print("invalid literal for int() with base 10")