#!/usr/bin/env python
# Requete : L occurence de chaque mot du fichier d entree 
# Module system qui vous permet de recuperer l entree std du processus 
#(liee a un tube qui recoit les lignes du fichier d entree )
import sys

# boucle qui va lire les lignes du fichier (string )
for line in sys.stdin:
    
# diviser la ligne en liste 
    words     = line.strip().split()
# Afficher sur la sortie standard le resultats    
    for word in words:
        print '%s\t%s' % (word, 1)
