from RCV import RCV
from plurality import plurality
from Borda import Borda
from Data import num_voters, num_alts, data
import numpy as np

alt_winner = RCV(num_alts, data)

count = np.zeros(10)

for p in range(1, 11):
    for k in range(3):
        s = np.random.choice(int(num_voters), size=int((num_voters/10)*p), replace=False)
        sdata = data.iloc[s]
        s_winner = None
        
        s_winner = Borda(num_alts, sdata)

        if (s_winner == alt_winner):
            count[p - 1] += 1

for i in range(1, 11):
    print("%d0 percent sample: %.2f" %(i, count[i - 1]/100))

#use 21 profiles

with open('pluralities.txt', 'a') as f:
    for c in count:
        f.write(str(c) + ", ")
    f.write("\n")