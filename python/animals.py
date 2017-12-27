
class AnimalGame:
	animals = []
	
	def __init__(self):
		self.animals = [ ('does it have spots?', 1, 2), ('is it a feline?' , 3 , 4), ('is it small?',5,6), 
		('leopard', None, None), ('panda', None, None), ('ant', None, None), ('elephant', None, None)]
		idx = 0 

	def play(self):
		#load_animal_data
		idx=0
		animal =None
		print "I'll guess your animal"
		answer = ''
		while answer!="yes" and animal != "":
			animal,idx = self.get_animal()
			print "Is your animal a ?", animal
			answer = raw_input()
			if answer=="yes": 
				print "I knew it !"
			else:
				print "I don't know your animal."
				#animal=""
				self.learn_animal(idx)
				idx=0
				print self.animals
				print "I'll ask again "

	def get_animal(self):
		idx=0
		while True:
			data, yes, no = self.animals[idx]
			if yes==None and no==None: return data,idx
			print data
			answer = raw_input()
			if answer == "yes": 
				idx = yes
			else :
				idx = no

	def learn_animal(self,idx):
		print "I'll learn your animal"
		print "What's your animal ?"
		new_animal = raw_input()
		print "please enter a question to distinguish "
		print "between a ", self.animals[idx][0] , " and a " , new_animal
		question = raw_input()
		print "for a", new_animal , "the answer is? yes/no"
		answer=raw_input()
		self.animals.append((new_animal,None,None))
		new_idx=len(self.animals)
		yes_ans = idx
		no_ans = new_idx	
		if answer== 'yes': 
			yes_ans = new_idx
			no_ans = idx
		self.animals.append((question,yes_ans,no_ans))

if __name__ == '__main__':
	game = AnimalGame()
	game.play()
