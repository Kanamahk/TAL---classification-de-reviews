#!/opt/anaconda3/bin/python3
#-*-coding:utf-8-*-

from readFileFonctions import *
from writeInFileFonctions import *
from traitements import *
from plotFunctions import *
import argparse


'''
fileName = 'alice.entier.txt'
outputFile = 'of.txt'

wordList = getTokenFromFile(fileName)



write_word_file(wordList, outputFile)
'''

   
if __name__=="__main__":

	argparser = argparse.ArgumentParser()
	argparser.add_argument('textfilefolder')
	args = argparser.parse_args()

	# file locations
	folder = args.textfilefolder
	para_file = folder+"/alice.entier.txt"
	outputFile = "of.txt"
	
	# read (and write) file with paragraphs
	paras = read_paragraph_file(para_file)

	# test segmentation
	test_segments_into_sents()

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
	#plot_occ2count(tok2count)


	# statistics
	#plot_rank2occ(tok2count)











