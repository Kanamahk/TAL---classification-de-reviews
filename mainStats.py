#-*-coding:utf-8-*-

import os
from collections import OrderedDict
from parseReview import *
from treatments import *
from writeInFileFunctions import *
from connotatedDictionary import *

reviewsdirectory = "./reviews"
outputFile = "of.txt"

if __name__=="__main__":
	myReviewsFileName = os.listdir(reviewsdirectory)
	
	'''
	myReviews=[]
	
	for r in myReviewsFileName:
		myReviews.append(getWholeReviewFromFile(reviewsdirectory + '/' + r))
		
	for r in myReviews:
		#printWholeReview(r)
		
		paras = text_into_paragraphs(getReview(r))

		# preprocess alice in wonderland
		preprocessed = []
		for p, para in enumerate(paras):
			preprocessed_sents = []
			sents = segment_into_sents(para)
			
			for sent in sents:
				sent = normalise(sent)
				print(sent)
				sent = tokenise(sent)

				preprocessed_sents.append(sent)
				
			preprocessed.append(preprocessed_sents)
			
		tok2count = get_tok2count(preprocessed)

		#tok2count = sort_dict_by_value(tok2count)
		tok2count = OrderedDict(sorted(tok2count.items(), key=lambda t: t[0]))
		
		write_dict(tok2count, outputFile)


		occ2count = get_occ2count(tok2count)
	'''
	
	dict = getConnotatedDictionary()
	WriteConnotatedDictionary(dict)