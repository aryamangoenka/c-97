introstring=input("enter a sentence: ")
wordCount=1
characterCounter=0
for i in introstring:
    characterCounter=characterCounter+1
    if(i ==' '):
        wordCount=wordCount+1
print("number of characters in the sentence is = ")
print(characterCounter)
print("number of words in the sentence is = ")
print(wordCount)