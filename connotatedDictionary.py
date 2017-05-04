#-*-coding:utf-8-*-

from treatments import *
import os

reviewsdirectory

def getConnotatedDictionaryFromFile():		

def writeConnotatedDictionary():
	with open("./statistics/connotatedDictionary.txt", "w") as filepointer:
		filepointer.write("test")
	
def getConnotatedDictionary():
	if os.exist("./statistics/connotatedDictionary.txt"):
		return getConnotatedDictionaryFromFile()
	else:
		return createConnotatedDictionary()

def createConnotatedDictionary(reviewsdirectory):
	if os.exist("./reviews"):
		myReviewsFileName = os.listdir("./reviews")
		for r in myReviewsFileName:
			myReviews.add(getReviewsFromFile("./reviews" + '/' + r))
			
		for r in myReviews:
		
		
def reviewRelevance(review):