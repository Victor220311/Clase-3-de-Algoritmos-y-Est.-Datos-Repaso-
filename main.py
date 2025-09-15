#Repaso python
#numeros = [1,2,3,4,5,6,7,8,9,10]
#for a in numeros:
    #print(a) Recorre elementos de una lista

# [1,2,3] lista
# (1,2,3) tupla (inmutable)
# {1,2,3} diccionario 

#PILAS: coleccion de elementos que permiten solo dos acciones: Añadir/sacar elementos
#Ultimo elemento en salir es el primero en entrar (LIFO)

#COLAS: coleccion de elementos que permiten solo dos acciones: Añadir/sacar elementos
#Primer elemento dentro es el primero fuera (FIFO)

#Para guardar elementos por script se con la ruta "cd" y se coloca script
#Todo esto usando la libreris "sys"

#En la funcion se utiliza el (*args,**kwargs)
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)