#-*-coding:utf-8-*-

from treatments import *
from parseReview import *
import os
from collections import OrderedDict
from writeInFileFunctions import write_dict

reviewsdirectory = "./reviews"

def getConnotatedDictionaryFromFile():
	dictionary = {}
	with open("./statistics/connotatedDictionary.txt", "r") as filepointer:
		for line in filepointer.readlines():
			item = line.strip().split(" ; ")
			dictionary[item[0]] = (item[1], item[2])
	return dictionary

def WriteConnotatedDictionary(dict):
	with open("./statistics/connotatedDictionary.txt", "w+") as filepointer:
		for (wordInDict, (totalOccurence, ratio)) in dict.items():
			filepointer.write(wordInDict + " ; " + str(totalOccurence) + " ; "+str(ratio) + "\n")
	
def getConnotatedDictionary():
	return createConnotatedDictionary()

def createConnotatedDictionary():
	if os.path.exists("./reviews"):
		myReviewsFileName = os.listdir(reviewsdirectory)
		myReviews = []
		dictionary = {}
		for r in myReviewsFileName:
			myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		for r in myReviews:
			dictionary = addReviewToDictionary(r, dictionary)
		return dictionary
		
def addReviewToDictionary(review, dictionary):
	paras = text_into_paragraphs(getReview(review))
	opinion = getOpinion(review)
	factor = 1 if opinion=="recommended"  else -1 if opinion == "not recommended" else 0
	
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
	
		
def print_token_analyse_review_with_dictionary(review, dictionary):
	paras = text_into_paragraphs(getReview(review))
	opinion = getOpinion(review)
	factor = 1 if opinion=="recommended"  else -1 if opinion == "not recommended" else 0
	
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
					reviewvalue += ratio
					notFound = False
					break

	if reviewvalue > 0: print ("This is a positive review.")
	if reviewvalue<0: print ("This is a negative review.")
	if reviewvalue == 0 : print("This is a neutral review.")