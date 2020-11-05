"""Utopian Tree"""

my_tree = int(input('How many trees do you want to test?: \n'))

for i in range(my_tree):
	meters=1
	my_cycle = int(input('How many cycles for the tree do you want to test?: \n'))
	for j in range(my_cycle):
		if (j%2)==0:
			meters*=2
		else:
			meters+=1
	print(f'The tree height will be for {meters} meters with {my_cycle} cycles')