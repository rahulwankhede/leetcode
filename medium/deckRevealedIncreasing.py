from collections import deque

def deckRevealedIncreasing(deck):
    mylist = deque()
    deck.sort()
    mylist.append(deck.pop()) #mylist contains one element now
    while(deck):
        mylist.appendleft(mylist.pop())
        mylist.appendleft(deck.pop())
    return mylist


"""testing"""

deck = [17,13,11,2,3,5,7]
print(deckRevealedIncreasing(deck))
