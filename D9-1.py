from collections import deque, defaultdict

def playgame(players, turns):
    scores = {}
    for k in range(players):
        scores[k] = 0
    stack = deque([0])
    
    for marble in range(1, turns + 1):
        if marble % 23 == 0:
            stack.rotate(7)
            scores[marble % players] += marble
            scores[marble % players] += stack.pop()
            stack.rotate(-1)
        else:
            stack.rotate(-1)
            stack.append(marble)
    return scores



print (max(i for i in playgame(464,70918).values()))
