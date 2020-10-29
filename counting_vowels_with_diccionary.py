"""Counting Vowels with Diccionary"""

my_text = input('Ingresa un texto: ').lower()
vowels = {
    'a': 0, 'e' : 0, 'i' : 0,
    'o' : 0, 'u' : 0,
}

for letter in my_text:
    if letter == 'a':
        vowels['a'] += 1
    elif letter == 'e':
        vowels['e'] += 1
    elif letter == 'i':
        vowels['i'] += 1
    elif letter == 'o':
        vowels['o'] += 1
    elif letter == 'u':
        vowels['u'] += 1

print(f'Tienes ', vowels['a'], '"a"')
print(f'Tienes ', vowels['e'], '"e"')
print(f'Tienes ', vowels['i'], '"i"')
print(f'Tienes ', vowels['o'], '"o"')
print(f'Tienes ', vowels['u'], '"u"')