import pandas as pd
import numpy as np
from itertools import product
import re

reps = list(product(["RF_distance","MP_time","Total_time","CPU_time","CPU_usage"],["rep1","rep2","rep3"]))
params = list(product(["mpboot","lvb","tnt"],[50,200],[10000,100000],[0.1,1.0],['equal','mammal']))
columns = pd.MultiIndex.from_tuples(reps)
indexes = pd.MultiIndex.from_tuples(params)
table = pd.DataFrame(data=np.zeros((48,15)),columns=columns,index=indexes)

def filltable(software,rep):
    with open(f"experiment_{software}/{rep}/RF_{software}_{rep}.txt") as f:
        file = f.read()
        results = {
        "RF_distance":re.findall("is (\d*) over",file),
        "MP_time":re.findall("MP time: (.*)",file) ,
        "Total_time":re.findall("Total time: (.*)",file),
        "CPU_time":re.findall("CPU time: (.*)",file),
        "CPU_usage":re.findall("CPU usage: (.*)",file)}
        for col in reps:
            table.loc[(software),(col[0],rep)] = results[col[0]]
        table.to_csv("RESULTS.csv")
    
filltable("mpboot","rep1")
filltable("mpboot","rep2")
