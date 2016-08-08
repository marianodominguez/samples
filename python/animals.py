
class AnimalGame:
	def __init__(self):
		animals = [ ('has spots?', 1, 2), ('is a feline?' , 3 , 4), ('is small?',5,6), 
		('leopard', None, None), ('panda', None, None), ('ant', None, None), ('elephant', None, None)]
		idx = 0 

	def play(self):
		#load_animal_data
		animal =None
		print "I'll guess your animal"
		answer = ''
		while answer!="yes" and animal != "":
			animal = self.get_animal()
			print "Is your animal a ?", animal
			answer = raw_input()
			if answer=="yes": 
				print "I knew it !"
			else:
				print "I don't know your animal."
				animal=""
				#learn_animal()

	def get_animal(self):
		while True:
			data, yes, no = animals[idx]
			if yes==None and no==None: return data
			print data
			answer = raw_input()
			if answer == "yes": 
				idx = yes
			else :
				idx = no

if __name__ == '__main__':
	play()