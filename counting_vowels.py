"""Counting Vowels"""

my_text = input('Ingresa un texto: ')
c = 0

for char in my_text:
    if (char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U'):
        c+=1

print("Tienes ", c ,"vocales")