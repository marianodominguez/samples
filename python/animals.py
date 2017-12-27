import pickle

class AnimalGame:
	animals = []
	
	def __init__(self):
		self.animals = [ ('does it have spots?', 1, 2), ('is it a feline?' , 3 , 4), ('is it small?',5,6), 
		('leopard', None, None), ('panda', None, None), ('ant', None, None), ('elephant', None, None)]
		idx = 0 

	def load_animal_data(self):
		with open('animal_data.pkl', 'rb') as input:
			self.animals = pickle.load(input)
		
	def save_animal_data(self):
		with open('animal_data.pkl', 'wb') as output:
			pickle.dump(self.animals, output, pickle.HIGHEST_PROTOCOL)

	def play(self):
		self.load_animal_data
		idx=0
		question_idx=0
		animal =None
		print "I'll guess your animal"
		answer = ''
		while answer!="yes" and animal != "":
			animal,idx,question_idx = self.get_animal()
			print "Is your animal a ", animal, "?"
			answer = raw_input()
			if answer=="yes": 
				print "I knew it !"
			else:
				print "I don't know your animal."
				#animal=""
				self.learn_animal(idx,question_idx)
				idx=0
				print self.animals
				self.save_animal_data
				print "I'll ask again "

	def get_animal(self):
		idx=0
		question_idx=0
		while True:
			data, yes, no = self.animals[idx]
			if yes==None and no==None: return data,idx,question_idx
			question_idx=idx
			print data
			answer = raw_input()
			if answer == "yes": 
				idx = yes
			else :
				idx = no

	def learn_animal(self,idx,question_idx):
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
		no_ans = new_idx-1
		if answer== 'yes': 
			yes_ans = new_idx-1
			no_ans = idx
		self.animals.append((question,yes_ans,no_ans))
		last_question=self.animals[question_idx]
		self.animals[question_idx]=(last_question[0],last_question[1],new_idx)

if __name__ == '__main__':
	game = AnimalGame()
	game.play()
