import wordfreq
import sys
import urllib.request



def main():

    inp_file = open(sys.argv[1]) # hämtar stopord från fil
    article = int(sys.argv[3]) #gör om 20 från str till int
    #inp_file = open(sys.argv[1], encoding="utf-8")   för windows
    stopwordlist=[]

    for line in inp_file:
        line=line.strip()
        stopwordlist.append(line)
    
    if sys.argv[2].startswith("https://") or sys.argv[2].startswith("http://"):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        textrows=[]
        for line in lines:
            textrows.append(line)
    else: 
        inp_file2 = open(sys.argv[2]) 
        textrows=[]
        for line in inp_file2:
            textrows.append(line)
        inp_file2.close()

    inp_file.close()


    words=wordfreq.tokenize(textrows)
    count=wordfreq.countWords(words, stopwordlist)
    wordfreq.printTopMost(count,article)
    


main()

