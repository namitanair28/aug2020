# Lab 06, Problem 1
# nair0025, Namita Nair, lab section 007

def cntWordOccur(sentences, word):
    list1 = sentences.split()
    count = 0
    for i in list1:
        if i == word:
            count += 1
    return count

def main():
    sentences = "I like to eat lots ad lots of ice cream"
    word = 'lots'
    print(cntWordOccur(sentences, word))
main()
