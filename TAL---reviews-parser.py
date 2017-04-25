# -*- coding: utf-8 -*-
"""
Created on Fri Apr  25 12:09:26 2017

@author: shankar.sivagnanasundaram, bryan.vigee
"""

import os, argparse, re, sys

def read_file(filename)->list:
	list_parag = []
	with open(filename,"r") as file_pointer:
        for line in file_pointer.readlines():
            #list_parag = line
            if line.strip()=="": continue
            list_parag.append(line.strip())
    return list_parag

def read_parag(rawText)->list:
    list_parag = []
    for line in rawText:
        if line.strip()=="": continue
        list_parag.append(line.strip())
    return list_parag
	
def read_parag(list_parag:list)->list:
    list_places=[]
    placesRegex= re.compile('[A-Z].*[^\n]')
    with open(filename,"r") as fp:
        for line in fp.readlines():
            line= line.rstrip('\n')
            print(line)
            match_obj = re.match(placesRegex,line)
            mot = match_obj.string
            list_places.append(mot)
    return list_places


def parse_sentence(list_parag:list)->list:
    list_sentences =[]    
    for line in list_parag:
        line = line.strip()
        if line=="" : continue
        list_sentences.append(line.split("\t"))
    return list_sentences

def parse_token(list_segment:list):


def tokenise(sentence):
    sentence = re.sub("([^ ])\'",(r"\1"),sentence)
    sentence = re.sub("( \')",r" ' ",sentence)
    sentence = re.sub("[\"]", '"',sentence)
    sentence = re.sub("([\.)");
    sentence = sentence.split()
    return sentence
