#jade rojas
#28-4-25
#repetir hasta que lo hagan bien
#podemos usar bucle junto con try

def pedir_repetido():
    while True: 
        try:
            numero = int(input("escribre un numero enttero: "))
            print("¡Gracias tu numero es:",numero)
        except ValueError:
           print("ese numero no es valido")
pedir_repetido()