import re

#Paragraph Analysis
#-----------------
#Approximate Word Count: 122
#Approximate Sentence Count: 5
#Average Letter Count: 4.6
#Average Sentence Length: 24.0

paragraph = (" A Turing machine is a device that manipulates "
            "symbols on a strip of tape according to a table "
            "of rules. Despite its simplicity, a Turing machine "
            "can be adapted to simulate the logic of any computer "
            "algorithm, and is particularly useful in explaining "
            "the functions of a CPU inside a computer. The 'Turing'"
            " machine was described by Alan Turing in 1936, who "
            "called it an""a(utomatic)-machine"". The Turing "
            "machine is not intended as a practical computing "
            "technology, but rather as a hypothetical device "
            "representing a computing machine. Turing machines "
            "help computer scientists understandthe limits of "
            "mechanical computation.")

paragraph=("Adam Wayne, the conqueror, with his face flung back" 
           "and his mane like a lion's, stood with his great sword point"
           "upwards, the red raiment of his office flapping around "
           "him like the red wings of an archangel. And the King saw,"
           "he knew not how, something new and overwhelming."
           "The great green trees and the great red robes swung "
           "together in the wind. The preposterous masquerade," 
           "born of his own mockery, towered over him and embraced"
           "the world. This was the normal, this was sanity," 
           "this was nature, and he himself, with his rationality," 
           "and his detachment and his black frock-coat, "
           "he was the exception and the accident a blot of black "
           "upon a world of crimson and gold.")


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






