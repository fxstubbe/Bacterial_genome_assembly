import random
def getData(path):
    with open(path,'r') as f_open:
        rawData = f_open.read()
    data = []
    
    # On parcourt chaque ligne de notre rawData (car on a fait un split sur le "enter")
    # Edge va enregistrer les paires séparées de chaque ligne en splitant le ->
    # Par chaque 2ème élément de cette paire (=endNode) on va spliter la virgule (qu'il y en ait une ou non).
    # Par chaque "endNode", on ajoute une ligne à data en remplissant comme startNode node 1er élément de edge
    for i in range(len(rawData.split("\n"))) :
        edge = rawData.split("\n")[i].split(" -> ")
        for i in range(len(edge[1].split(","))) :
            data.append([edge[0],edge[1].split(",")[i]])
    return data

# On parcourt data pour trouver une edge commençant par le startNode fournit
def getNodeStartedBy(startNode):
    for i in range(len(data)):
        if data[i][0] == startNode:
            return data[i]
    return 0

#On crée un cycle à partir d'un point de départ. Toutes les arrêtes visitées sont supprimées de data. 
#On insert le SubCycle dans cycle (ainsi, on crée 2 listes simultanément)    

def generateSubCycleFrom(startingEdge,insertIndex):
    eulerianSubCycle = []
    eulerianSubCycle.append(startingEdge)
    eulerianCycle.insert(insertIndex,startingEdge)
    data.remove(startingEdge)
    
    i=1
    while (getNodeStartedBy(eulerianSubCycle[-1][1])!=0):
        newEdge = getNodeStartedBy(eulerianSubCycle[-1][1])
        eulerianSubCycle.append(newEdge)
        eulerianCycle.insert(insertIndex+i,newEdge)
        data.remove(newEdge)
        i+=1
#On choisit un nouveau point de départ, dans le cycle Eulérien, encore disponible pour générer un Subcycle        
def getNewStartingNode():
    for i in range(len(eulerianCycle)):
        if getNodeStartedBy(eulerianCycle[i][0])!=0:
            return getNodeStartedBy(eulerianCycle[i][0]),i
    return 0

eulerianCycle = []
data = getData('D:\François-Xavier\Documents\datakmer.txt')

edge = random.choice(data)
index = 0

#On crée le cycle
while len(data)>0:
    generateSubCycleFrom(edge,index)
    if getNewStartingNode()!=0:
        edge,index = getNewStartingNode()
    else: break

#Formattage des données
formattedEulerianCycle = eulerianCycle[0][0]+" -> "+eulerianCycle[0][1]
for i in range(len(eulerianCycle)-1): formattedEulerianCycle += " -> "+eulerianCycle[i+1][1]

#print(data)
print("Eulerian cycle : ",eulerianCycle)
print("Formated Eulerian cycle : " , formattedEulerianCycle)
