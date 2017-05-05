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
		printWholeReview(r)
		print_analyse_review(r[5])