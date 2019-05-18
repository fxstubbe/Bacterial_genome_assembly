def getData(path):

    with open(path,'r') as f_open: rawData = f_open.read()
    data = list(rawData.split("\n"))
    return data
    
kmer_list = getData('D:\François-Xavier\Documents\kmerlist.txt')

debruijn = {}

for i in kmer_list :
    
   debruijn[i[0:2]]= []
   debruijn[i[1:3]]= []
   
#   if len(debruijn) == 16 : break

for i in kmer_list : debruijn[i[0:2]].append(i[1:3])

print(debruijn)



#---------------Creating the graph -----------------------------

#Récupérer les clefs et les arguments du dictionnaire
cle = [i for i in debruijn.keys()]
value = [j for j in debruijn.values()]

#formatage des données
for i in range (0, len(cle)):
    val = ""
    for j in range (0, len(value[i])):
        if  j!= len(value[i])-1 :
            val += value[i][j]
            val += ","
        else : val += value[i][j]
    if i != len(cle)-1 : print(cle[i] + " -> " + val)
    else : print(cle[i] + " -> " + val)
    

        