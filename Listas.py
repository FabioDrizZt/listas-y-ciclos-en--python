paises = [
    "Argentina",
    "Uruguay",
    "Paraguay",
]
def mostrarPaises(paises):
    import os
    os.system('clear')
    print(paises)


mostrarPaises(paises)    
print(paises[0]) # Argentina
print(paises[1]) # Uruguay
print(paises[2]) # Paraguay
# print(paises[3]) fuera de rango

#Agregar un nuevo pais al final de la lista
paises.append("Bolivia")
mostrarPaises(paises)
paises.append("Chile")
mostrarPaises(paises)
#Agregar un pais en el mediode la lista
paises.insert(1, "Colombia")
mostrarPaises(paises)
# Eliminación de un elemento de la lista
paises.remove("Bolivia")
mostrarPaises(paises)
# Borrar  un ellemento inexistente arroja un error
#paises.remove("Huruguay")
mostrarPaises(paises)
# Borrar un elemento mediante el indice
paises.pop(1)
mostrarPaises(paises)
#Cantidad de elementos de la lista
print(len(paises))
# Buscar el indice de un valor
print('Paraguay se encuentra en el indice',paises.index("Paraguay"))
# Buscar un elemento inexistente arroja un error
# print('Ecuador se encuentra en el indice',paises.index("Ecuador"))
# Ordenar la lista Ascendentemente
paises.sort()
mostrarPaises(paises)
# Revertir la lista
paises.reverse()
mostrarPaises(paises)
# Encontrar el elemento mas extenso de una lista
print('Elemento mas extenso: ' , max(paises, key=len))
# Encontrar el elemento mas corto de una lista
print('Elemento mas corto: ' , min(paises, key=len))

notas = [10, 9, 8, 7, 6, 15, 4, -3, 2, 1]
print('La nota mas alta es: ', max(notas))
print('La nota mas baja es: ', min(notas))

#Ejercicio')