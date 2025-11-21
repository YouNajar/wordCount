#!/usr/bin/env python

from operator import itemgetter
import sys
 # Initialisation des variables de comptage d<occurence
current_word = None
current_count = 0
word = None


for line in sys.stdin:
    # Enlever les espaces
    line = line.strip()
    # Creation d une liste \ partir d un string
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    # Si le mot ne change pas incrementer l occurence
    if current_word == word:
        current_count += count
    else :
        if current_word:
            # Si le mot change donc afficher le mot precedent et son occurence
            print '%s\t%s' % (current_word, current_count)
        current_count = count # 
        current_word = word
# Affichage du dernier mot
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
