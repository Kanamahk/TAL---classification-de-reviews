#-*-coding:utf-8-*-

import os
from parseReview import *

reviewsdirectory = "./reviews"

if __name__=="__main__":
	myReviewsFileName = os.listdir(reviewsdirectory)
	myReviews =[]
	for r in myReviewsFileName:
		myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		
	for r in myReviews:
		#printWholeReview(r)
		print("\n\ntoken analyse\n")
		print_token_analyse_review(r[5])
		print("\n\nsubsent analyse\n")
		print_subsent_analyse_review(r[5])