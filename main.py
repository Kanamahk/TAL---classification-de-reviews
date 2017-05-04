#-*-coding:utf-8-*-

import os
from parseReview import *

reviewsdirectory = "./reviews"

if __name__=="__main__":
	myReviewsFileName = os.listdir(reviewsdirectory)
	for r in myReviewsFileName:
		myReviews.add(getReviewsFromFile(reviewsdirectory + '/' + r))
		
	for r in myReviews:
		printWholeReview(r)