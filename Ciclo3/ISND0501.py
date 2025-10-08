nombre = "Alvin"
palabra = "reconocer" #palindrome (girafarig))
otra_palabra = "palabra"

print(len(nombre)) #prints length starting from 0

print(nombre[2]) #nombre is an array, looking for the 3rd letter of the thingy

print(nombre[2:5]) #print letter 3 to 6

print(len(palabra))
print(palabra[0::2]) #inicio:fin:salto ~ comienza r:*sin fin*:salta 2(inclusivo) ; con esto se salta todas las vocales
print(palabra[1::2]) #salta todas las consonantes
print(palabra[::-1]) #imprime al reves
print(otra_palabra[::-1])

if (palabra == palabra[::-1]):print("true") #FORMAT FOR IF-ELSE ON PYTHON RAHHH
else: print("false")

mi_palabra = "jocote"
print(mi_palabra)
mi_palabra_mayuscula = mi_palabra.upper() #hijos
mi_palabra_cap = mi_palabra.capitalize()

print(mi_palabra_mayuscula) #hace todo mayusula
print(mi_palabra_cap) #pone 1ra palabra con mayuscula

tupla1 = (1,12,255,1289,60000) 
lista1 = [1,12,255,1289,60000] #if () tupla ; if [] lista
print(len(tupla1)) #cada elemento cuenta como un caracter