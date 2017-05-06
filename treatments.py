#-*-coding:utf-8-*-

import re 
import collections

def text_into_paragraphs(text):
	paragraphs = []
	for line in text:
		if line.strip()=="": continue # ignore blank paragraphs
		paragraphs.append(line.strip()) # remove whitespace with strip()
	
	return paragraphs

def segment_into_sents(paragraph):

	cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
	regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
	
	if "\n" in paragraph: exit("Error in paragraph: paragraph contains \n.")	   
	newline_separated = re.sub(regex_cannot_precede+"([\.\!\?]+([\'\â€™\"\)]*( |$)| [\'\â€™\"\) ]*))", r"\1\n", paragraph)
	sents = newline_separated.strip().split("\n")
	for s, sent in enumerate(sents):
		sents[s] = sent.strip()
	return sents


def normalise(sent):
	sent = re.sub("\'\'", '"', sent) # two single quotes = double quotes
	sent = re.sub("[`â€˜â€™]+", r"'", sent) # normalise apostrophes/single quotes
	sent = re.sub("[â‰ªâ‰«â€œâ€]", '"', sent) # normalise double quotes

	sent = re.sub("([a-z]{3,})or", r"\1our", sent) # replace ..or words with ..our words (American versus British)
	sent = re.sub("([a-z]{2,})iz([eai])", r"\1is\2", sent) # replace ize with ise (..ise, ...isation, ..ising)
	
	sent = re.sub(r"(?P<beginning>(^| |\n))+(?P<cap>[A-Z])(?P<end>[^A-Z])",  lambda m: m.group('beginning')+m.group('cap').lower()+m.group('end'), sent)
	
	
	sent = re.sub(r"(?P<beginning>(^| |\n))+(?P<cap>i)(?P<end>[^a-zA-Z])",  lambda m: m.group('beginning')+m.group('cap').upper()+m.group('end'), sent)
	
	replacements = [("it's", "it is"), ("she’s", "she is"), ("he’s", "he is"), ("someone’s", "someone is"), ("something’s", "something is"), ("there’s", "there is"),("that’s", "that is"), ("what’s", "what is"), ("who’s", "who is"), ("where’s", "where is"), ("why’s", "why is"), ("when’s", "when is"), ("y'all", "you all"), ("ain't", "are not"), ("can't", "cannot"), ("gonna", "going to"), ("gotta", "got to"), ("shan’t", "shall not"), ("won't", "will not"), ("youre", "you are")] # etc.
	
	for (original, replacement) in replacements:
		sent = re.sub("(^| )"+original+"( |$)", r"\1"+replacement+r"\2", sent)
	return sent
	
	sent = re.sub("([a-z]n't)", r"\1 not", sent)
	sent = re.sub("([a-z]'ve)", r"\1 have", sent)
	sent = re.sub("([a-z]'ll)", r"\1 will", sent)
	sent = re.sub("([a-z]'d)", r"\1 would", sent)
	sent = re.sub("([a-z]'re)", r"\1 are", sent)
	sent = re.sub("([a-z]'m)", r"\1 am", sent)


	
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

def tokenise(sent):
	return tokenise_en(sent)


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

	
