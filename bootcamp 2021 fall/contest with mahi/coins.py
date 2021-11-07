from typing import DefaultDict
 
def coins(l1, l2, l3):
    rank = DefaultDict(int)
    if l1[1] == '<':
        rank[l1[2]]+=1
    elif l1[1] == '>':        
        rank[l1[0]]+=1
    if l2[1] == '<':        
        rank[l2[2]]+=1
    elif l2[1] == '>': 
        rank[l2[0]]+=1
    
    if l3[1] == '<': 
        rank[l3[2]]+=1
    elif l3[1] == '>': 
        rank[l3[0]]+=1
    ans=[None for _ in range(3)]
    for key,item in rank.items():
        if ans[item]:
            return "Impossible"
        ans[item]=key
    return "".join(ans)
    
    
l1 = input()
l2 = input()
l3 = input()
 
print(coins(l1, l2, l3))