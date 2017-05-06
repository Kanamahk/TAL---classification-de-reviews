#-*-coding:utf-8-*-

import os
from parseReview import *
from connotatedDictionary import *

reviewsdirectory = "./reviews"


if __name__=="__main__":
	dict = getConnotatedDictionary()
	WriteConnotatedDictionary(dict)

	myReviewsFileName = os.listdir(reviewsdirectory)
	myReviews =[]
	for r in myReviewsFileName:
		myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		
	for r in myReviews:
		print("\n\nNew review : ")
		review = getReview(r)
		para =""
		for line in review:
			para += line
		print (para) 
		
		print("\n\nToken analyse using the connotated dictionary :")
		print_token_analyse_review(getReview(r))
		print("\nToken analyse :")
		print_token_analyse_review(getReview(r))
		print("\nSub sentence analyse :")
		print_subsent_analyse_review(getReview(r))
		print("\nThe review was " + ("positiv" if getOpinion(r)=="recommended"  else "negativ" if opinion == "not recommended" else "incomplete") + ".\n\n")