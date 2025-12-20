'''
Animal game is a recursive animal game algorithm that returns the number of times each function is called.
WIP: not working

'''

import pickle
import os.path
# Animal game
class AnimalGame:
	# List of animals
	animals = []
	# Constructor
	def __init__(self):
		# List of animals
		self.animals = [ ('does it have spots?', 1, 2), ('is it a feline?' , 3 , 4), ('is it small?',5,6), 
		('leopard', None, None), ('panda', None, None), ('ant', None, None), ('elephant', None, None)]
		# Index of the animal
		self.idx = 0 
		# Load the animal data
		self.load_animal_data()
	# Load the animal data
	def load_animal_data(self):
		if os.path.exists('animal_data.pkl'):
			with open('animal_data.pkl', 'rb') as input:
				self.animals = pickle.load(input)
		#print "data loaded", len(self.animals) 
		
	# Save the animal data
	def save_animal_data(self):
		with open('animal_data.pkl', 'wb+') as output:
			pickle.dump(self.animals, output)
		#print "data saved", len(self.animals) 

	# Play the game
	def play(self):
		# Load the animal data
		self.load_animal_data()
		# Index of the animal
		idx=0
		# Question index
		question_idx=0
		# Animal
		animal =None
		# Print the message
		print("I'll guess your animal")
		answer = ''
		# While the answer is not yes and the animal is not empty
		while answer!="yes" and animal != "":
			# Get the animal
			animal,idx,question_idx = self.get_animal()
			# Print the question
			print("Is your animal a ", animal, "?")
			answer = raw_input()
			if answer=="yes": 
				print("I knew it !")
			else:
				print("I don't know your animal.")
				#animal=""
				self.learn_animal(idx,question_idx)
				idx=0
				print(self.animals)
				self.save_animal_data()
				print("I'll ask again ")

	# Get the animal
	def get_animal(self):
		# Index of the animal
		idx=0
		# Question index
		question_idx=0
		while True:
			# Get the animal
			data, yes, no = self.animals[idx]
			# If the animal is not a question
			if yes==None and no==None: return data,idx,question_idx
			question_idx=idx
			print(data)
			answer = input()
			if answer == "yes": 
				idx = yes
			else :
				idx = no

	# Learn the animal
	def learn_animal(self,idx,question_idx):
		print("\n I'll learn your animal \n")
		print("What's your animal ?")
		new_animal = input()
		print("please enter a question to distinguish")
		print("between a", self.animals[idx][0] , "and a" , new_animal)
		question = input()
		print("for a", new_animal,"the answer is? yes/no")
		answer=input()
		# Add the animal
		self.animals.append((new_animal,None,None))
		# New index
		new_idx=len(self.animals)
		# Yes answer
		yes_ans = idx
		# No answer
		no_ans = new_idx-1
		# If the answer is yes
		if answer== 'yes': 
			yes_ans = new_idx-1
			no_ans = idx
		# Add the animal
		self.animals.append((question,yes_ans,no_ans))
		# Last question
		last_question=self.animals[question_idx]
		# Update the animal
		self.animals[question_idx]=(last_question[0],last_question[1],new_idx)

# Main
if __name__ == '__main__':
	game = AnimalGame()
	game.play()
