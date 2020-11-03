"""Counting Bob"""

def couting_bobs(text):
    """Function couting Bobs"""

    text = text.lower()
    bobs_number = 0
    for letter in range(len(text)):
        if text[letter: letter+3] == 'bob':
            bobs_number += 1
    return bobs_number

my_text = input('Introduce un texto: ')
bobs_number = couting_bobs(my_text)
print(f'Tienes {bobs_number} bobs')