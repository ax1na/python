#jade rojas
#28-4-25
#mostrar un elemento de una lista por tu posicion, manejando si la 
#posicion no existe

def mostrar_elemento():
    frutas = ["manzana", "banana", "naranja", "palta"]	
    try:
         indices = int(input("elige una posicion(0 a 3): "))
         print("fruta elegida:", frutas[indices])
    except IndexError:
        print("la posicion no existe")
    except ValueError:
        print("debes ingresar numero")