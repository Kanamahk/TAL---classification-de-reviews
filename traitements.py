#-*-coding:utf-8-*-

import re 
import collections

def segment_into_sents(paragraph):

	cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
	regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
	
	if "\n" in paragraph: exit("Error in paragraph: paragraph contains \n.")	   
	newline_separated = re.sub(regex_cannot_precede+"([\.\!\?]+([\'\â€™\"\)]*( |$)| [\'\â€™\"\) ]*))", r"\1\n", paragraph)
	sents = newline_separated.strip().split("\n")
	for s, sent in enumerate(sents):
		sents[s] = sent.strip()
	return sents


def normalise(sent, lang):
	sent = re.sub("\'\'", '"', sent) # two single quotes = double quotes
	sent = re.sub("[`â€˜â€™]+", r"'", sent) # normalise apostrophes/single quotes
	sent = re.sub("[â‰ªâ‰«â€œâ€]", '"', sent) # normalise double quotes

	if lang=="en":
		sent = re.sub("([a-z]{3,})or", r"\1our", sent) # replace ..or words with ..our words (American versus British)
		sent = re.sub("([a-z]{2,})iz([eai])", r"\1is\2", sent) # replace ize with ise (..ise, ...isation, ..ising)
	if lang=="fr":
		replacements = [("keske", "qu' est -ce que"), ("estke", "est -ce que"), ("bcp", "beaucoup")] # etc.
		for (original, replacement) in replacements:
			sent = re.sub("(^| )"+original+"( |$)", r"\1"+replacement+r"\2", sent)
	return sent
	
def tokenise_en(sent):

	sent = re.sub("([^ ])\'", r"\1 '", sent) # separate apostrophe from preceding word by a space if no space to left
	sent = re.sub(" \'", r" ' ", sent) # separate apostrophe from following word if a space if left

	sent = re.sub(" \(", r" \( ", sent) # separate ( from following word if a space 
	sent = re.sub("([^ ])\) ", r" \) ", sent) # separate ) from following word if a space 

	# separate on punctuation
	cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
	regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
	sent = re.sub(regex_cannot_precede+"([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", sent)
	sent = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", sent) # then restick several fullstops ... or several ?? or !!
	sent = sent.split() # split on whitespace
	return sent

def tokenise(sent, lang):
	if lang=="en":
		return tokenise_en(sent)
	elif lang=="fr":
		return tokenise_fr(sent)
	else:
		exit("Lang: "+str(lang)+" not recognised for tokenisation.\n")


def test_segments_into_sents():
	# basic case
	assert(segment_into_sents("Time flies like an arrow. Fruit flies like a banana.") == ["Time flies like an arrow.", "Fruit flies like a banana."])
	# don't segment on all full stops
	assert(segment_into_sents("M. Dupont est venu nous voir.") == ["M. Dupont est venu nous voir."])
	assert(segment_into_sents("Aux U.S.A. il pleut.") == ["Aux U.S.A. il pleut."])


def get_tok2count(paras):
	tok2count = {}
	for para in paras:
		for sent in para:
			for tok in sent:
				if tok not in tok2count: tok2count[tok] = 0
				tok2count[tok] += 1

	return tok2count

def get_occ2count(tok2count):
	occ2count = {}
	for tok in tok2count:
		if tok2count[tok] not in occ2count: occ2count[tok2count[tok]] = 0
		occ2count[tok2count[tok]] += 1
	return occ2count

def sort_dict_by_value(dictionary):
	return collections.OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))

	
