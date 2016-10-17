#!/usr/local/bin/python3
# -*-coding:Utf-8 -*


print("Bonjour ; voilà une fonction calculant des factorielles (normalement ...)")

fac    = 1
vinit  = 4  
valeur = vinit
while valeur >= 1 :
  fac = fac*valeur
  valeur = valeur-1
  print("ICI : ",fac)

print("la factorielle de {} vaut {} ".format(vinit,fac))





