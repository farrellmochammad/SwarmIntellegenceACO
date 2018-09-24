import math
import random

#Read file
filetsp = open('Tugas 1 CSH4313 Kecerdasan Kolektif Ganjil 2018-2019.enc/Swarm016.tsp','r')

#Defining function
def euclid(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def probability(antposition,alpha,beta,matrixTij,distancematrix,townvisited):
    findmax = []
    
    #calculate sum
    sumelement = []
    sum = 0
    for i in range (0,len(matrixTij)) : sumelement.append(i)
    for i in range (0,len(matrixTij)) : 
        if (i not in townvisited) and (i!=antposition): sum += (matrixTij[antposition][i]**alpha)*(1/distancematrix[antposition][i]**beta) 
            #print((matrixTij[antposition][i]**alpha),distancematrix[antposition][i],antposition,i)
    for i in range(0,len(matrixTij)):
        if (i in townvisited ):
            findmax.append(0)
        elif (i==antposition):
            findmax.append(0)
        else :
            findmax.append((matrixTij[antposition][i]**alpha)*(1/distancematrix[antposition][i])**beta/sum)
    return(findmax.index(max(findmax)))
        
def countLk(tabulist,distancematrix):
    Lkmatrix = []
    for i in range(0,len(tabulist)):
        sum = 0
        for j in range(0,len(tabulist[0])-1):
            sum += distancematrix[tabulist[i][j]][tabulist[i][j+1]]
        Lkmatrix.append(sum)
    return Lkmatrix   
        
        
    
        
#Append data file to data
data = []
idx = 0
countdata = filetsp.readline().strip()
while (countdata!='EOF'):
    countdata = filetsp.readline().strip().split(' ')
    data.append(countdata)
    idx += 1
    countdata = countdata[0]
idx -= 1

#Initialization dynamic index
x,y = idx,idx
distancematrix = [[0 for dataX in range(x)] for dataY in range(y)]

#Fill in distance matrix
for i in range(0,x):
    for j in range(0,y):
        distancematrix[i][j] = euclid(float(data[j][1]),float(data[i][1]),float(data[j][2]),float(data[i][2]))



#part 1 : Initialization variable
t = 0
NC = 0
Minvalue = 1000
c = 0.5
Q = 1
alpha = 15
beta = 20
NCmax = 100
matrixdeltaTij =  [[0 for dataX in range(x)] for dataY in range(y)]
matrixTij = [[c for dataX in range(x)] for dataY in range(y)]
ant = 16
prevmatrix = []

while (NC<=NCmax) :
    #part 2 : Initialization ant to tabu list
    s = 0
    tabulist = [[0 for dataX in range(x+1)] for dataY in range(ant)]
    for k in range(0,x):
        tabulist[k][0] = k
    for k in range(x,ant):
        tabulist[k][0] = random.randint(0,x-1)
    

    #part 3 : Append route to each tabulist
    l = 0
    while(l<ant):
        townvisited = []
        townvisited.append(tabulist[l][0])
        for m in range(0,y-1):
            j = probability(tabulist[l][m],alpha,beta,matrixTij,distancematrix,townvisited)
            tabulist[l][m+1] = j
            townvisited.append(j)
        l += 1

    #part 4 : Update Pheromone
    for n in range(0,ant):
        tabulist[n][x]=tabulist[n][0]
        towntravelmatrix = countLk(tabulist,distancematrix)
        if prevmatrix!=[]:
            if towntravelmatrix[n]>prevmatrix[n]:
                towntravelmatrix[n] = prevmatrix[n]
        else :
            prevmatirx = towntravelmatrix
    for n in range(0,len(tabulist)):
        for o in range(0,len(tabulist[0])-1):
            deltaij = Q/towntravelmatrix[n]
            matrixdeltaTij[tabulist[n][o]][tabulist[n][o+1]] += deltaij

    #part 5 :
    for o in range(0,len(tabulist[0])-1):
        matrixTij[tabulist[n][o]][tabulist[n][o+1]] = 0.357 * matrixTij[tabulist[n][o]][tabulist[n][o+1]] + matrixdeltaTij[tabulist[n][o]][tabulist[n][o+1]]
    t += 1
    matrixdeltaTij =  [[0 for dataX in range(x)] for dataY in range(y)]
    
    if (Minvalue>min(towntravelmatrix)):
        Minvalue = min(towntravelmatrix)
    print ("Solusi jarak terbaik ke ",NC,  " : ",Minvalue)
    print ("Solusi rute terbaik : ",tabulist[towntravelmatrix.index(min(towntravelmatrix))])

    #part 6 :
    if (NC<NCmax) :
        tabulist = [[0 for dataX in range(x+1)] for dataY in range(y)]
    elif(NC==NCmax-1) :
        print towntravelmatrix
    NC += 1

