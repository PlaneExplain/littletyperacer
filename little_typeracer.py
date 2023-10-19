#!/usr/bin/env python3
import random
import time
import curses

x = random.randrange(10, 20)
slowa = []

def initial(iloscSlow):
# Ta funkcja wypełni tablicę slowa[x]
# Najpiew lista jest wypełniana numerami losowymi, potem je sortujemy
# wyczytywać linijki z pliku tylko sekwencyjnie (wiec sortujac zmniejszamy czas obliczenia)

    numerySlow=random.sample(range(0, 1000), iloscSlow)
    numerySlow.sort()
    calyTekst="Treść:"
    f = open("Dictionary.txt")
    for pozycja, tekst in enumerate(f):
        if pozycja in numerySlow:
            #print(tekst)
            calyTekst=calyTekst+" "+tekst
            slowa.append(tekst.replace("\n "," "))

    # Przez sekwencyjność readline trzeba pozbyć się w nich
    print(calyTekst.replace("\n",""))

def pisanie():
# Zaczynamy od ustalenia jaki jest teraz czas, aby potem obliczyć z tego czas pisania
    start=time.time()
    i=0
    while i in range(0,x):
        prawdziwe=False
        print('Słowo: '+slowa[i])
        slowkoTemp=input("Prosze:")
        slowa[i]=slowa[i].replace("\n","")
        #print(str(int(slowa[i])-int(slowkoTemp)))
        if slowkoTemp==slowa[i]:
            prawdziwe=True
        if prawdziwe:
            i += 1
        else:
            print("Powtórz")
    print("Your time was: "+str(time.time()-start))
print("Tekst do napisania\n")
initial(x)
print('\nIlosc slów: '+str(x)+"\n")
pisanie()

