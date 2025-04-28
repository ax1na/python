#JADE ROJAS
#28-4-25
#accerder a un valos en un diccionario 
#sin que s4e rompa el programa si la clave no existe 

def buscar_cantante():
    cantante={
        "nombre":"luis Miguel",
        "pais":"puerto rico",
    }
    try: 
        clave =  input("que quieres saber? (nombre o pais): ")
        print("el resultado", cantante[clave])
    except KeyError:
        print("la clave no existe")
         
buscar_cantante()