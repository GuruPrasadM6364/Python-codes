import random as ran 
def streak(flip):
    for i in range(len(flip)-5):
        streak=flip[i:i+6]
        if all(j=='H' for j in streak) or all(j=='T' for j in streak):
            return True
    return False
streaks=0
for k in range(0,10000):
    flips=['H' if ran.randint(0,1)==0 
           else'T' for k in range(1000)]
    if streak(flips):
        streaks+=1
final=streaks/100
print("Chances of streak of 6 in a row:",final,"%")