lista = [8.17, 90, 1, 5, 44, 1.32]

lista.sort(reverse=True) #ancedente, lo que esta adentro del parentesis es para desendente
mayor = lista[0] #tambien se puede con mayor=max(lista) en caso de poner menor es min
print(lista)

logitud = len(lista)
print(logitud) #mostrara la cantidad de elem que tiene

resultado = 8.17 in lista
print(resultado) #dara true

indice = lista.index(8.17)
print(indice) #diraa que posc esta

contador = lista.count(5) #para ver cuantos hay
print(contador)