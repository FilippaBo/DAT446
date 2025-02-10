#import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
        #print(line)
        while start < len(line):
            if line[start].isspace():
                start = start+1
                

            elif line[start].isalpha():
                    end = start
                    
                    while end < len(line) and line[end].isalpha(): 
                        
                        end = end+1

                    words.append(line[start:end].lower())
                        #print(f"{line[start]} is a letter")
                    start = end


            elif line[start].isdigit():
                    end = start
                    
                    while end < len(line) and line[end].isdigit(): 
                        
                        end = end+1
                    words.append(line[start:end])
                        #print(f"{line[start]} is a digit")
                    start = end
            else:
                    #print(f"{line[start]} is a symbol")
                    words.append(line[start])
                    start = start+1

            
    return words

#print(tokenize(['Apple','p1e!']))
#tokenize(['apple','p1e!'])
#wordfreq.tokenize(['apple','p1e!'])



"""
Initialize a variable with an empty dictionary.
Start a loop that goes through all words in the list. If the current word appears in the list stopWords then ignore it.
The first time when you encounter a new word, add it with count 1 to the dictionary. The next time just increment the count with one.
return the dictionary from the function after you have counted all words.
Note that you can find whether you have already seen the word by using the operator in in Python. If the variable frequencies refers to the dictionary, then the expression word not in frequencies will evaluate to True only if this is the first time when you have encountered the word.

When you are done, run the test program, to make sure that everything works well.
"""

def countWords(words, stopWords):
    frequencies = {}
    
    for word in words: #tar bort stopwords
        if not word in stopWords:
             
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    
    return frequencies


def printTopMost(frequencies,n): 
     x=sorted(frequencies.items(), key=lambda x: -x[1])
     count=0
     for word,freq in x:
        if n==count:
             break
        print(word.ljust(20) + str(freq).rjust(5))
        count=count+1 #skriver bara ut n antal ord