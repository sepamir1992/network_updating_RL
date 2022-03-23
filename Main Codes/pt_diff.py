num_diff = []
fraction = []
size1 = []
size2 = []
  
for num in range (0, 200):
    newlist=[]
    pti = []
    ptj = []
    
    with open("pt"+str(num)+".txt", "r") as file_1:
        file_1_text = file_1.read().splitlines()
    
        with open("pt"+str(num+1)+".txt", "r") as file_2:
            file_2_text = file_2.read().splitlines()
            
        
    
        
            for i in (file_1_text):
                pti.append(i)
    
            for j in (file_2_text):
                ptj.append(j)
                
      

            
            

                    
            
            

# =============================================================================
            newlist.append([item for item in pti if item not in ptj])
            newlist.append([item for item in ptj if item not in pti])
            num_diff.append((len(newlist[0])+len(newlist[1]))/2)
            #fraction.append(num_diff[num]/max(len(pti), len(ptj)))
# =============================================================================
#             if num == 0:
#                 fraction.append(num_diff[num]/max(len(pti), len(ptj)))
#             else:
#                 fraction.append((num_diff[num]/max(len(pti), len(ptj)))+fraction[num-1])                 
# =============================================================================
# =============================================================================

C = [0 for i in range(0, 2000)]
for x in num_diff:
    for y in range(0, 2000):
        if x<=y:
            C[y] = C[y]+1

        

dP = [i/200 for i in C]
num_nodes=[i for i in range(0, 2000)]
import matplotlib.pyplot as plt
plt.plot(num_nodes, dP)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xlabel("dP (K=1)")
plt.show()

