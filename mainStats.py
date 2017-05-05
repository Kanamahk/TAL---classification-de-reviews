#-*-coding:utf-8-*-

import os
from parseReview import *
from treatments import *

reviewsdirectory = "./reviews"

if __name__=="__main__":
	myReviewsFileName = os.listdir(reviewsdirectory)
	
	myReviews=[]
	
	for r in myReviewsFileName:
		myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		
	for r in myReviews:
		#printWholeReview(r)
		
		
		paras = getReview(r)

		# preprocess alice in wonderland
		preprocessed = []
		for p, para in enumerate(paras):
			preprocessed_sents = []
			sents = segment_into_sents(para)
			
			for sent in sents:
				sent = normalise(sent, "en")
				sent = tokenise(sent, "en")

				preprocessed_sents.append(sent)
				
			preprocessed.append(preprocessed_sents)
			
		tok2count = get_tok2count(preprocessed)

		tok2count = sort_dict_by_value(tok2count)
		write_dict(tok2count, outputFile)


		occ2count = get_occ2count(tok2count)