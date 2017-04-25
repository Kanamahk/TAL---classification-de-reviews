#-*-coding:utf-8-*-

import os
from parseReview import *

reviewsdirectory = "./reviews"

if __name__=="__main__":
	myReviews = os.listdir(reviewsdirectory)
	for r in myReviews:
		printReview(getReviewsFromFile(reviewsdirectory + '/' + r))
	