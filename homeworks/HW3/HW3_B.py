# CSCI 1133, Lab Section 007, HW 3, Problem B REDO
# Namita Nair, nair0025

def play_game(p1list, p2list):
    if p1list == 'R':
        if p2list == 'SC':
            return 1
        if p2list == 'L':
            return 1
        if p2list == 'P':
            return 2
        if p2list == 'SP':
            return 2
        if p2list == 'R':
            return 'T'
    if p1list == 'SC':
        if p2list == 'SC':
            return 'T'
        if p2list == 'L':
            return 1
        if p2list == 'P':
            return 1
        if p2list == 'SP':
            return 2
        if p2list == 'R':
            return 2
    if p1list == 'P':
        if p2list == 'SC':
            return 2
        if p2list == 'L':
            return 2
        if p2list == 'P':
            return 'T'
        if p2list == 'SP':
            return 1
        if p2list == 'R':
            return 1
    if p1list == 'SP':
        if p2list == 'SC':
            return 1
        if p2list == 'L':
            return 2
        if p2list == 'P':
            return 2
        if p2list == 'SP':
            return 'T'
        if p2list == 'R':
            return 1
    if p1list == 'L':
        if p2list == 'SC':
            return 2
        if p2list == 'L':
            return 'T'
        if p2list == 'P':
            return 1
        if p2list == 'SP':
            return 1
        if p2list == 'R':
            return 2
        
def play_round(p1list, p2list):
    newlist = []
    newlist.append(play_game(p1list[1], p2list[1]))
    newlist.append(play_game(p1list[2], p2list[2]))
    if newlist[0] != newlist[1]:
        newlist.append(play_game(p1list[3], p2list[3]))
    if newlist.count(1) >= 2:
        return 1
    if newlist.count(2) >= 2:
        return 2
    else:
        return 'T'
        
    
def main():
    p1list = []
    p2list = []
    print("3 rounds: select R for rock, P for paper, SC for scissors, SP for spock, or L for lizard")
    p1list.append(int(input("Enter player #: ")))
    p1list.append(str(input("Game #1 choice: ")))
    p1list.append(str(input("Game #2 choice: ")))
    p1list.append(str(input("Game #3 choice: ")))
    p2list.append(int(input("Enter player #: ")))
    p2list.append(str(input("Game #1 choice: ")))
    p2list.append(str(input("Game #2 choice: ")))
    p2list.append(str(input("Game #3 choice: ")))
    print(play_round(p1list,p2list))

                            
if __name__ == "__main__":
    main()                
                
                