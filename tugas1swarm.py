import math

#Read file
filetsp = open('Tugas 1 CSH4313 Kecerdasan Kolektif Ganjil 2018-2019.enc/Swarm016.tsp','r')

#Defining function
def euclid(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

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
matrix = [[0 for dataX in range(x)] for dataY in range(y)]

#Fill in distance matrix
for i in range(0,x):
    for j in range(0,y):
        matrix[i][j] = euclid(float(data[j][1]),float(data[i][1]),float(data[j][2]),float(data[i][2]))

for i in range(0,x):
    for j in range(0,y):
        print("Jarak ke-",i,j,":",matrix[i][j])
    print()
