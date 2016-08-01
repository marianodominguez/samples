animals = [ ('has spots?', 1 ,  2), ('is a feline?' , 3 , 4), 
	('is small?',5,6), ('leopard',,), ('panda',,), ('ant'), ('elephant')]
idx = 0 

def mainloop
	print "I'll guess your animal"
	while answer!='y' || animal != '':
		animal = get_animal()
		print "Is your animal a ", animal
		input answer
		if answer=="yes" print "I knew it !"

def get_animal
	while true:
		data, yes, no = animals[idx]
		if yes==None and no==None return data
		print data
		input answer
		if answer== 'yes' idx = yes
		if answer== 'no' idx = no

