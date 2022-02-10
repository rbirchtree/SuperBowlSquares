import random

#create a function that picks numbers 0-9 and add them
#to the list randomly, if the number isn't in the list, don't add the number

def SuperBowlNumbers():	
		superBowlLine = []
		while len(superBowlLine) < 10:
			r = random.randint(0,9)
			if r in superBowlLine:
				print("Not adding duplicates.")
			else:
				superBowlLine.append(r)			
			#if not in list append, else don't do anything
		print(superBowlLine)
		
	

SuperBowlNumbers()
#Bengals are X-axis
SuperBowlNumbers()
#Rams are Y-axis