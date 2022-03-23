###READ UTILIZATION OF EACH CSV FILE#####
import pandas as pd
from collections import OrderedDict
import collections
import json
from collections import defaultdict
import networkx as nx

def makelist(i): 

    df_firstn = pd.read_csv("D:/CSC 579/Project/PT (2)/pt"+str(i)+".csv")
    file = open("D:\CSC 579\Project\PT (2)\Pt_texts\ptUtility.txt", "w")
    
    file.write((df_firstn.loc[df_firstn['flow_id'] == 0].iloc[1])['optimal_mlu'])
    file.write("\n")
    
    #print((df_firstn.loc[df_firstn['flow_id'] == 0].iloc[1])['optimal_mlu'])
    
    
      
for i in range(0, 200):

    makelist(i) 