#jade rojas
#28-4-25


#divison segura 
#objetivo entre 2 numeros y evitar o alertar 
#asi el usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input("ingresa numero: "))
        num2 = int(input("ingresa numero: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("el resultado de la divison  es:", resultado)
    except ValueError:
        print("Error. solo debes ingresar numeros ")
        
division_segura()
    
    