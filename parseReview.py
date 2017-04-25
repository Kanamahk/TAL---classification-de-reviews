#-*-coding:utf-8-*-

def getReviewsFromFile(fileName): 
	file_pointer = open(fileName, "r")
	
	gameName = file_pointer.readline()
	opinion = file_pointer.readline()
	hoursPlayed = file_pointer.readline()
	writtenReviews = file_pointer.readline()
	gamesPossessed = file_pointer.readline()
	review = []
	for line in file_pointer.readlines():
		review.append(line)
	file_pointer.close()
	
	contents = gameName, opinion, hoursPlayed, writtenReviews, gamesPossessed, review
	return contents
	
	
def printReview(review):
	print("name of the game : " + review[0])
	print("opinion : " + review[1])
	print("number of hours played : " + review[2])
	print("number of written reviews : " + review[3])
	print("number of games possessed : " + review[4])
	print("review : ")
	for line in review[5]:
		print('\t'+line)