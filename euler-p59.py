# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 14:57:47 2025

@author: phoeb
"""

######### 暴力解
########## https://walkerdoescode.home.blog/2019/10/18/project-euler-problem-59/

import time
 
f = open("D:/Downloads/0059_cipher.txt", "r")
 
if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(x.split(","))
else:
    raise ValueError("Cannot read from file")
 
finalContents = []
for x in realContents[0]:
    finalContents.append(int(x))

def isAcceptable(myChar):
    return 'a'<=myChar<='z' or 'A'<=myChar<='Z' or myChar == ' ' or myChar == '\'' or myChar == ',' or myChar == '"' or myChar == '[' or myChar == ']' or myChar == ':' or '0'<=myChar<='9' or myChar == '/' or myChar == '.' or myChar == '(' or myChar == ')' or myChar == ';' or myChar=='+'
    
def projectEulerProblemFiftyNine(cipherText):
    tl = len(cipherText)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    possible = []
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                myGuess = a+b+c
                asciiIndices = [ord(a),ord(b),ord(c)]
                s = ""
                bad = False
                for x in range(tl):
                    myChar = chr(cipherText[x] ^ asciiIndices[x%3])
                    if not isAcceptable(myChar):
                        bad = True
                        break
                    s+=myChar
                if not bad:
                    possible.append(s)
    total = -1
    for x in possible:
        subTotal = 0
        for y in x:
            subTotal+=ord(y)
        if(total==-1):
            total = subTotal
    return total

start = time.time()
print (projectEulerProblemFiftyNine(finalContents))
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

129448
--- 0.169327974319 seconds ---

for input of given cipher text.
''' 