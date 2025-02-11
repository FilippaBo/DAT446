import wordfreq
import sys
import urllib.request



def main():

    inp_file = open(sys.argv[1]) # hämtar stopord från fil
    inp_file2 = open(sys.argv[2]) # hämtar textrader från artiklar
    article = int(sys.argv[3]) #gör om 20 från str till int
    #inp_file = open(sys.argv[1], encoding="utf-8")   för windows

    #response = urllib.request.urlopen(sys.argv[2])
    #lines = response.read().decode("utf8").splitlines()

    
    stopwordlist=[]
    textrows=[]

    for line in inp_file:
        line=line.strip()
        stopwordlist.append(line)

    for line in inp_file2:
        textrows.append(line)

    inp_file.close()
    inp_file2.close()


    words=wordfreq.tokenize(textrows)
    count=wordfreq.countWords(words, stopwordlist)
    wordfreq.printTopMost(count,article)
    


main()

#obs skriv python3 topmost.py eng_stopwords.txt examples/article1.txt 20 i terminalen varje gång

