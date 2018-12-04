import re
import os
import csv


txtFile = open("paragraph.txt","r")
paragraph= txtFile.read()
print (paragraph)
wordCount = len(re.findall(r'\w+', paragraph))
sentenceCount=len(re.findall(r'\.', paragraph))
letterCount=0
for word in paragraph:
    for letter in word:
        if len(letter)>0:
            letterCount+=1

averageLetterCount = round(letterCount/wordCount,2)
averageSentenceLength = round(wordCount/sentenceCount,2)

print("Paragraph Analysis")
print("-----------------")          
print(f"Approximate Word Count:{wordCount}")        
print(f"Approximate Sentence Count:{sentenceCount}")
print(f"Average Letter Count:{averageLetterCount}")
print(f"Average Sentence Length:{averageSentenceLength}")






