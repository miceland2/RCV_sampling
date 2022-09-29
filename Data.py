import pandas as pd

df = pd.read_csv('elections/ED-00008-00000001.soi', names = [i for i in range(1, 15)])
num_alts = df.iloc[0].iloc[0]
num_voters = df.iloc[num_alts + 1].iloc[0]

df = pd.read_csv('elections/ED-00008-00000001.soi', skiprows=num_alts+2, names = [i for i in range(1, 15)])

data = pd.DataFrame()

cnt = 0
for i in range(len(df)):
    for j in range(df.iloc[i, 0]):
        data = data.append(df.iloc[i, 1:])
        
data = data.iloc[:, 0: num_alts]
        

        
