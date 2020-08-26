#Lab 09, section 007
#Namita Nair, nair0025

#Warm-up 1
def makeDictionary(names, scores):
    scoreDict = {}
    for i in range(len(names)):
        scoreDict[names[i]] = scores[i]
    return scoreDict
    
scoreDict = makeDictionary(['joe', 'tom', 'barb', 'sue','sally'], [11, 22, 14, 17, 10])
#Warm-up 2
print(scoreDict['barb'])
#Warm-up 3
scoreDict['john']=18
print(scoreDict)
#Warm-up 4
newlist = []
for key in scoreDict:
    newlist.append(scoreDict[key])
newlist.sort()
print(newlist)
#Warm-up 5
sum1 = sum(newlist)
ave = sum1 / len(newlist)
print(ave)
#Warm-up 6
del(scoreDict['tom'])
print(scoreDict)
#Warm-up 7
scoreDict['sally']=15
print(scoreDict)
#Warm-up 8
def getScore(name, dictionary):
    if name in dictionary:
        print(dictionary[name])
        return dictionary[name]
    else:
        print("Name not found")
        return -1
    
#Stretch

def morseCode(string):
    string = string.upper()
    morseDictionary = {' ': '/','A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---','K': '-.-','L': '.-..', 'M': '--','N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...','T': '-', 'U': '..-','V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    morsestr = ''
    for i in string:
        morsestr += morseDictionary[i]
    return morsestr

print(morseCode('Hello how are you'))

#Workout