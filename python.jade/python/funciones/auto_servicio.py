#jade rojas
#21-4-25

from tkinter import Menu


def obtener_articulo(numero):
    menu ={
        1:"hamburgesa con queso",
        2: "papas fritas",
 3: "refresco",
  4: "helado",
  5:"galleta"
}
return menu.get(numero, "articulo no encontrado")

def vienvenido():
    print("Bienvenido a fastfood express")
    print("1. @ hamburguesa con queso")
    print("2. ;papas fritas")
    print("3. / refresco")
    print("4. * helado")
    print("5.  - galleta")

def main():
    vienvenido()
    numero = int(input("ingrese el numero del articulo que desea: "))
try:
    print("has pedido : ", obtener_articulo(numero))
except:
    print("entrada invalida")
