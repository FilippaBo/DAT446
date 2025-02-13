#import wordfreq


def tokenize(lines):
    
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            if line[start].isspace():
                start = start+1
                

            elif line[start].isalpha():
                    end = start
                    
                    while end < len(line) and line[end].isalpha(): 
                        
                        end = end+1

                    words.append(line[start:end].lower())
                    start = end


            elif line[start].isdigit():
                    end = start
                    
                    while end < len(line) and line[end].isdigit(): 
                        
                        end = end+1
                    words.append(line[start:end])
                    start = end
            else:
                    words.append(line[start])
                    start = start+1

            
    return words



def countWords(words, stopWords):
    frequencies = {}
    
    for word in words: 
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
        count=count+1 