import os
os.system("cls")

matematicas = int(input("Notas en Matemáticas: "))
fisica = int(input("Notas en Física: "))

#if matematicas > 17 : propina = 3 * matematicas
#else : propina = matematicas
#
#if fisica > 15 : propina = 2 * fisica
#else : propina = 0.5 * fisica

#forma corta:
propina = matematicas + fisica/2
if propina > 17 : propina += 2 * matematicas
if fisica > 15 : propina += fisica * 1.5

#if (fisica + matematicas)/2 > 16 : obsequio = "Reloj"
#else : obsequio = "Nada"

#print(f"Propina:    s/{propina:.2f}")
#print(f"Obsequio:   {obsequio}")

#forma corta:
promedio = (matematicas + fisica)/2
print(f"Promedio:   {promedio}")
print(f"Propina :   {propina}")
print(f"Obsequio:   {'Si' if promedio > 16 else 'No'}")