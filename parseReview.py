#-*-coding:utf-8-*-
from treatments import *


def getWholeReviewFromFile(fileName): 
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

def getGameName(review):
	return review[0]
	
def getOpinion(review):
	opinion = review[1]
	if opinion[-1] == "\n":
		opinion = opinion[:-1]
	return opinion

def getHoursPlayed(review):
	return review[2]

def getWrittenReviews(review):
	return review[3]
	
def getGamesPossessed(review):
	return review[4]
	
def getReview(review):
	return review[5]
	
	
def printWholeReview(review):
	print("name of the game : " + getGameName(review))
	print("opinion : " + getOpinion(review))
	print("number of hours played : " + getHoursPlayed(review))
	print("number of written reviews : " + getWrittenReviews(review))
	print("number of games possessed : " +etGamesPossessed(review))
	print("review : ")
	for line in getReview(review):
		print('\t' + line)
	
		
def print_token_analyse_review(review):
	auxil = read_word_list_file("auxiliary_pos.txt")
	posi = read_word_list_file("Positive.txt")
	nega = read_word_list_file("Negative.txt")
	reviewvalue = 0
	for line in review:
		for sent in getSubSent((line)):
			sentvalue = 0
			tokens = tokenise_en(normalise(sent))
			for tok in tokens:
				for pos in posi:
					if tok == pos:
						sentvalue +=1
				for neg in nega:
					if tok == neg:
						sentvalue -=1
				if tok == "not" or tok == "won't":
					sentvalue *= -1
				for aux in auxil:
					if tok == (aux + "n't") or tok == (aux + " not"):
						sentvalue *=-1
			reviewvalue+=sentvalue
	if reviewvalue > 0: print ("This is a positive review.")
	if reviewvalue<0: print ("This is a negative review.")
	if reviewvalue == 0 : print("This is a neutral review.")


def print_subsent_analyse_review(review):
	auxil = read_word_list_file("auxiliary_pos.txt")
	posi = read_word_list_file("Positive.txt")
	nega = read_word_list_file("Negative.txt")
	reviewvalue = 0
	for lint in review:
		for sent in getSubSent((lint)):
			sentvalue = 0
			for pos in posi: 
				if sent.find(pos): sentvalue += sent.find(pos)
			for neg in nega:
				if sent.find(neg): sentvalue += -sent.find(neg)
			if sent.find("not") or sent.find("won't"): sentvalue *=-1
			for aux in auxil:
				if sent.find(aux+"'nt"): sentvalue *=-1
			reviewvalue+=sentvalue
	if reviewvalue > 0: print ("This is a positive review.")
	if reviewvalue<0: print ("This is a negative review.")
	if reviewvalue == 0 : print("This is a neutral review.")