# import string
# import random
# from images import IMAGES
# # #for choose the random words from dectionry
# def choose_word():
# 	file=open('words.txt','r')
# 	file_data=file.read()
# 	word_list=file_data.split()
# 	secret_word=random.choice(word_list)
# 	return secret_word
# #this is for to print __ guessed word which is in secret word
# def get_guessed_word(secret_word,letter_guessed):
# 	k=0
# 	guessed_word=""
# 	for k in range(len(secret_word)):
# 		if secret_word[k] in letter_guessed:
# 			guessed_word+=secret_word[k]
# 		else:
# 			guessed_word+='_'
# 	return guessed_word

# #for hint
# def get_hint(secret_word,letter_guessed):
# 	import random
# 	letters_not_guessed=[]
# 	for i in secret_word:
# 		if i not in letter_guessed:
# 			if i not in letters_not_guessed:
# 				letters_not_guessed.append(i)
# 	return random.choice(letters_not_guessed)

# # #for printing the left letters
# def letter_left(letter_guessed):
# 	import string
# 	left_letters=string.ascii_lowercase
# 	for i in letter_guessed:
# 		left_letters=left_letters.replace(i,"")
# 	return left_letters
# def hangman(secret_word):#code for guessing the letter
# 	print('\t','\t','\t','W E L C O M E    T O   T H E   G A M E   ',IMAGES[7],'\n','\n','\t','\t','\t','\t', ' H A N G M A N !','\n','\n','\t','\t','\t','\t')
# 	letter_guessed=[]
# 	counter=7
# 	hint=3
# 	while counter>0:
# 		print('Guessed the word which is ' + str(len(secret_word)) + ' letters long::','\n')
# 		print('choose the word from:    ',letter_left(letter_guessed),'\n')
# 		print('press 1 for hint','\t'*10,'press 2 for change the word','\n'*3)
# 		guess=(input('guess the letter   ')).lower()
# 		if guess not in letter_guessed:
# 			if guess in secret_word:
# 				letter_guessed.append(guess)
# 				print('\n','good guess  ',get_guessed_word(secret_word,letter_guessed),'\n')
# 				print('you have '+str(counter)+' lives','\t','\t','\t','Hint left : ',hint,'\n')
# 			elif guess=='1':
# 				if hint>0:
# 					letter_guessed.append(get_hint(secret_word,letter_guessed))
# 					print('\t'*5,get_guessed_word(secret_word,letter_guessed))
# 					hint-=1
# 					print('\n','you have '+str(counter)+' lives','\t','\t','\t','Hint left : ',hint,'\n')
# 				else:
# 					print('\n','no hints left','\n')
# 			elif guess=='2':
# 				print('\n'*50,'\t','\t','your word is changed')
# 				break
# 			else:
# 				counter-=1
# 				print(guess,' is not belong to the word','\n')
# 				print(IMAGES[7-counter])
# 				print('\n','you have '+str(counter)+' lives','\t','\t','\t','Hint left : ',hint)
# 		else:
# 			print('\n','you enter already used  alphabet ','\n')
# 		if get_guessed_word(secret_word,letter_guessed)==secret_word:
# 			print('\t','\t','****CONGRATULATION********','\n'*50)
# 			break
# 		elif counter==0:
# 			print('NOW YOU HAVE ',counter,' LIFES','\n'*3,'\t'*9,'GAME OVER')
# 			break
	
		

# if __name__=="__main__":
# 	while 1:
# 		start=int(input('press 5 to get start'))
# 		if start==5:
# 			secret_word=choose_word()
# 			print('\n'*15,hangman(secret_word))
# 		else:
# 			print("you enter the wrong choice")






