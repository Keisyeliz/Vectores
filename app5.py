import os 
list_animales_nombre = []
list_animales_codigo = []
item = 0
def fnt_limpiar():
    os.system
    print('Zoologico - Luis Amigó')
    print('----------------------\n\n')

def fnt_agregar(nombre):
    global item
    if nombre == '':
        input('\nDebe ingresar un nombre <ENTER>')
    else:
        list_animales_nombre.append(nombre)
        list_animales_codigo.append(item)
        item += 1
        input('\nAnimal registrado con exito <ENTER>')

def fnt_mostrar():
    fnt_limpiar()
    for i in range(len(list_animales_nombre)):
        print(list_animales_codigo[i],' - ',list_animales_nombre[i])
    input('\nRegistro finalizado <ENTER>')

sw = True
while sw == True:
    fnt_limpiar()
    opcion = input('---MENU---\n\n1. Agregar por orden(Append)\n2. Agregar por posición(Insert)\n3. Eliminar por orden(pop)\n4. Eliminar por posición(pop[pos])\n5. Mostrar\n6. Salir\n-> ')
    if opcion == '1':
        nombre = input('Nombre del animal: ')
        fnt_agregar(nombre.upper())
     elif opcion == '2':
     nombre = input('Nombre del animal: ')
     posicion = int(input('Posición: '))
     if posicion > len(list_animales_nombre):
         input('Posición no valida <ENTER>') 
     else:
         list_animales_nombre.insert(posicion,nombre.upper())
 elif opcion == '3':
     if len(list_animales_nombre) == 0:
         input('No hay animales registrados <ENTER>')
     else:
         list_animales_nombre.pop()
         list_animales_codigo.pop()
 elif opcion == '4':
     if len(list_animales_nombre) == 0:
         input('No hay animales registrados <ENTER>')
     else:
         posicion = int(input('Posición: '))
         if posicion > len(list_animales_nombre):
             input('Posición no valida <ENTER>') 
         else:
             list_animales_nombre.pop(posicion)
             list_animales_codigo.pop(posicion)
 

    elif opcion == '5':
        fnt_mostrar()

    elif opcion == '6':
        input('Fin del programa')
        sw = False
    else:
        print('Opción no valida')
