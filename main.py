#!/usr/local/bin/python3
# -*-coding:Utf-8 -*

from fact import factorielle

print("Bonjour ; voilà une fonction calculant des factorielles (normalement ...)")

vinit = input("De quel valeur voulez-vous calculer la factorielle ? ")

try:
  vinit = int(vinit)
except ValueError :
  print(" -- ERREUR : Vous devez entrer un entier")   
  quit()

 


fac = factorielle(vinit)

print("la factorielle de {} vaut {} ".format(vinit,fac))







