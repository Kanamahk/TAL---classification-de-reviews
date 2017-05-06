#-*-coding:utf-8-*-

from treatments import *
from parseReview import *
import os
from collections import OrderedDict
from writeInFileFunctions import write_dict

reviewsdirectory = "./reviews"

def getConnotatedDictionaryFromFile():
	dictionary = {}
	with open(filename, "r") as filepointer:
		for line in filepointer.readlines():
			item = line.strip().split(" ; ")
			dictionary[item[0]] = (item[1], item[2])
	return dictionary

def WriteConnotatedDictionary(dict):
	with open("./statistics/connotatedDictionary.txt", "w+") as filepointer:
		for (wordInDict, (totalOccurence, ratio)) in dict.items():
			filepointer.write(wordInDict + " ; " + str(totalOccurence) + " ; "+str(ratio) + "\n")
	
def getConnotatedDictionary():
	if os.path.exists("/statistics/connotatedDictionary.txt"):
		return getConnotatedDictionaryFromFile()
	else:
		return createConnotatedDictionary()

def createConnotatedDictionary():
	if os.path.exists("./reviews"):
		myReviewsFileName = os.listdir(reviewsdirectory)
		myReviews = []
		for r in myReviewsFileName:
			myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		
		dictionary = {}
		
		for r in myReviews:
			paras = text_into_paragraphs(getReview(r))
			opinion = getOpinion(r)
			factor = 1 if opinion=="recommended"  else -1 if opinion == "not recommended" else 0
			
			# preprocess alice in wonderland
			preprocessed = []
			for p, para in enumerate(paras):
				preprocessed_sents = []
				sents = segment_into_sents(para)
				for sent in sents:
					sent = normalise(sent)
					sent = tokenise(sent)
					preprocessed_sents.append(sent)
					
				preprocessed.append(preprocessed_sents)
				
			tok2count = get_tok2count(preprocessed)
			
			notAWord = ["!", "\"", "'", "(", ")", ",", ".", "/", ":", ";", "?", "!", "\\"]
			
			for (word, occurence) in tok2count.items():
				notFound = True
				isNotAWord = False
				for w in notAWord:
					if word == w:
						isNotAWord = True
						
				if(not(isNotAWord)):
					for (wordInDict, (totalOccurence, ratio)) in dictionary.items():
						if word == wordInDict:
							dictionary[wordInDict] = (totalOccurence + factor*factor*occurence, ratio + factor*occurence)
							notFound = False
							break
					if notFound :
						dictionary[word] = (factor*factor*occurence, factor*occurence)
			
		dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))
		return dictionary
		
#def reviewRelevance(review):