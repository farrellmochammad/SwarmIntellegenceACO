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
         
def findmin(distancematrix,townvisited):
    Min = 1000
    index = -1
    for i in range(0,len(distancematrix)) :   
        if (i<min and i not in townvisited):
            Min = distancematrix[i]
            index = i
    return Min,index

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


tabulist = []
for i in range(0,x):
    distancematrix[i][i] = 100

town = random.randint(0,15)
tabulist.append(town)
firsttown = town
townvisited = []
townvisited.append(town)
print(town)
print(distancematrix[town])
for i in range(0,x-1):
    minusvalue,idx = findmin(distancematrix[town],townvisited)
    townvisited.append(distancematrix[town].index(minusvalue))
    tabulist.append(distancematrix[town].index(minusvalue))
    town = distancematrix[town].index(minusvalue)
tabulist[len(tabulist)-1] = firsttown

sum = 0
for i in range(0,x-1):
    sum += distancematrix[i][i+1]

print(tabulist,sum)

