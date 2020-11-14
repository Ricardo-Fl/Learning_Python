"""Number Pyramids"""

def num_pyr(number):

    lista = []
    pyramids_number = number + 1

    for char in range(pyramids_number):
        string = str(char)
        value_list = string * char
        lista.append(value_list)
    inverse = lista[::-1]
    lista.extend(inverse)
    lista.pop(pyramids_number)
    lista.pop(0)
    lista.pop(-1)
    return lista

pyramids_number = int(input('Enter a number: '))
pyramids_list = num_pyr(pyramids_number)
for number in range(len(pyramids_list)):
    print(pyramids_list[number])