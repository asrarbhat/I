import random

seed= 100
out1=0
out2=0
for j in range(50):
    for i in range(100):
        x = random.randint(1,100)
        if x<52:
            out1+=1
            out2+=seed/100
            seed+=seed/100
        else:
            out1-=1
            out2-=seed/100
            seed-=seed/100
print(out1,out2)

