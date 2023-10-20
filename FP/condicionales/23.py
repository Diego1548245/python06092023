import os
os.system("cls")

notamate = int(input("Notas en Matemáticas: "))
notafisica = int(input("Notas en Física: "))

if notamate > 17 : propina1 = 3 * notamate
else : propina1 = 1 * notamate

if notafisica > 15 : propina2 = 2 * notafisica
else : propina2 = 0.5 * notafisica

if (notafisica + notamate)/2 > 16 : obsequio = "Reloj"
else : obsequio = "Nada"

print(f"Propina:    s/{propina1+propina2:.2f}")
print(f"Obsequio:   {obsequio}")
Fal