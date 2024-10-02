string = input("Digite a string: ")
contador = 0

for i in string:
    if (i == "a" or i == "A"):
        contador += 1

if contador != 0:
    print(f"A letra 'a' apareceu {contador} vezes.")
else:
    print(f"A letra 'a' não apareceu na string.")