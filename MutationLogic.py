import random
import math

initialPopulation0 = [12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 59, 61, 62, 64, 65, 67, 68, 69, 72, 74, 75, 76, 77, 78, 79, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 112, 113, 116, 117, 118, 119, 120, 121, 122, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139] #randomly generated by random.org. Every list can be picked up randomly. Domain is [11,148]
initialPopulation1 = [13, 14, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 36, 37, 38, 39, 40, 41, 42, 44, 46, 47, 48, 49, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 98, 99, 100, 101, 103, 105, 106, 107, 109, 110, 111, 112, 113, 118, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139]
initialPopulation2 = [12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 37, 38, 40, 42, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 114, 116, 117, 119, 120, 121, 122, 123, 124, 127, 129, 132, 135, 136, 139]
initialPopulation3 = [13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38, 41, 42, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 70, 72, 73, 74, 75, 76, 78, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 100, 101, 102, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 133, 134, 135, 136, 137, 138, 139]
initialPopulation4 = [12, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24, 26, 28, 29, 31, 32, 33, 34, 36, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 95, 98, 100, 101, 102, 104, 105, 106, 107, 108, 110, 111, 113, 114, 115, 116, 117, 119, 120, 121, 124, 125, 126, 127, 128, 129, 130, 132, 133, 134, 136, 138, 139]
initialPopulation5 = [13, 14, 15, 17, 19, 20, 21, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 48, 49, 50, 51, 53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 121, 122, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 137, 139]
initialPopulation6 = [12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 27, 28, 29, 32, 33, 34, 35, 36, 37, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 53, 55, 57, 58, 59, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 109, 110, 111, 113, 114, 115, 116, 118, 119, 120, 121, 124, 125, 126, 127, 130, 132, 133, 135, 136, 137, 138, 139]
initialPopulation7 = [12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27, 28, 29, 30, 32, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 50, 51, 53, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68, 71, 72, 73, 75, 78, 79, 81, 82, 83, 85, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139]
initialPopulation8 = [12, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 81, 85, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 115, 116, 117, 118, 120, 123, 124, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138]
initialPopulation9 = [13, 14, 16, 17, 18, 19, 20, 23, 24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 74, 76, 79, 80, 81, 83, 84, 85, 89, 90, 91, 93, 94, 95, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 119, 121, 123, 124, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139]
initialPopulation10 = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 63, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 98, 101, 102, 103, 104, 106, 107, 108, 109, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 126, 127]
initialPopulation11 = [0, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 36, 38, 40, 42, 43, 44, 47, 48, 49, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 69, 70, 71, 72, 73, 75, 76, 77, 78, 81, 82, 83, 84, 85, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 108, 109, 110, 111, 112, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]
initialPopulation12 = [0, 1, 2, 3, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 30, 32, 34, 35, 37, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 63, 64, 65, 66, 67, 69, 70, 72, 73, 75, 76, 77, 79, 81, 83, 84, 85, 86, 87, 89, 90, 91, 93, 94, 95, 96, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 127]
initialPopulation13 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 21, 22, 23, 25, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 62, 63, 64, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 100, 101, 102, 104, 106, 107, 108, 109, 110, 111, 113, 116, 118, 119, 121, 122, 124, 125, 126, 127]
initialPopulation14 = [3, 4, 5, 6, 8, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78, 81, 83, 84, 85, 86, 87, 88, 91, 92, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122, 123, 124, 125, 126]
initialPopulation15 = [0, 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 94, 95, 96, 97, 98, 99, 101, 102, 103, 106, 107, 108, 110, 111, 112, 113, 115, 118, 119, 121, 122, 123, 124, 125, 127]
initialPopulation16 = [0, 1, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36, 37, 38, 40, 42, 43, 44, 45, 46, 47, 50, 51, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 81, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 97, 98, 101, 102, 104, 105, 106, 107, 108, 110, 111, 112, 113, 115, 116, 117, 118, 120, 122, 123, 124, 125, 126]
initialPopulation17 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 27, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 81, 82, 84, 85, 86, 88, 89, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 110, 112, 113, 115, 116, 117, 120, 121, 123, 124, 125, 126, 127]
initialPopulation18 = [1, 3, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 40, 41, 42, 43, 46, 48, 49, 51, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 90, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 113, 114, 115, 117, 121, 122, 123, 124, 125, 126, 127]
initialPopulation19 = [ 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 53, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 120, 121, 123, 124, 125]
initialPopulationMock = []

listInitial=[initialPopulation0,initialPopulation1,initialPopulation2,initialPopulation3,initialPopulation4,initialPopulation5,initialPopulation6,initialPopulation7,initialPopulation8,initialPopulation9,]
separator=""
listInitial2=[initialPopulation10,initialPopulation11,initialPopulation12,initialPopulation13,initialPopulation14,initialPopulation15,initialPopulation16,initialPopulation17,initialPopulation18,initialPopulation19,]
separator=""
def functionMock(x):
    return 0

def generateBugs(initialPopulation,mode):
    pass
def f(x):
    #previous function - domain was to slight so put another function#y=-(2*x^8)/229635 + (2*x^7)/15309 + (44*x^6)/32805 - (697*x^5)/32805 - (578*x^4)/10935 + (5852*x^3)/6561 + (108712*x^2)/229635 - (213074*x)/25515 + 643621/6561
    #y=(661*x ^ 19) / 310319133696000000000000000000000 - (84191*x ^ 17) / 1067062284288000000000000000000 + (21373*x ^ 15) / 17831923200000000000000000 - (1863947*x ^ 13) / 192148070400000000000000 + (550410559*x ^ 11) / 12070840320000000000000 - (6174558259*x ^ 9) / 48283361280000000000 + (10235317597*x ^ 7) / 48037017600000000 - (24259025771*x ^ 5) / 118879488000000 + (785230009181*x ^ 3) / 7718911200000 - (4695781*x) / 230945

    return -(118831
             *x ^ 8) / 20756736000000000 + (793097
             *x ^ 7) / 230630400000000 - (1693363
             *x ^ 6) / 1976832000000 + (12571151
             *x ^ 5) / 109824000000 - (3061549
             *x ^ 4) / 345600000 + (109655527
             *x ^ 3) / 274560000 - (5191552439
             *x ^ 2) / 518918400 + (892511507
             *x) / 7207200 - 113123 / 198


def g(x):
    return 2*(x^2)+1
#print f(0b11111111)
#print 0b11111111

# select n nodes from initial population and convert them to binary list
def initializePopulation(list,n):
    listDec=[]
    #listBin=[]
    for x in range(n):
        listDec.append(random.choice(list))
        #listBin.append(bin(listDec[x]))
    #print listDec
    #print "\n"

    return listDec


def convertPopulation(list):
    listBin=[]
    for x in range(len(list)):
        listBin.append(bin(list[x])[2:].zfill(8))
    #print listBin
    return listBin

def deConvertPopulation(list):
    listDec=[]
    for x in range(len(list)):
        #print list
        listDec=int(list,2)
    return listDec
# rate elements of population - assign

def ratePopulation(listDec,listBin):
    valueDec=[]
    dictVB={}
    for x in range(len(listDec)):
         valueDec.append(int(f(listDec[x]))) #need to cast to int by force, because python automatically assigned long int here. #Here is the place to choose g(x) or f(x)
         #print listDec[x]
         #print f(listDec[x])
         dictVB[listBin[x]]=valueDec[x]
    orderedDictVB=sorted(dictVB.items(), key=lambda t: t[1]) #sorted by values
    orderedDictBV=sorted(dictVB.items(), key=lambda t: t[0])
    print "chromosomes and values: "+str(orderedDictBV) #sorted by keys
    #print valueDec
    return orderedDictVB


def countTotal(chromosomes):
    total=0
    for x in range(len(chromosomes)):
        total += chromosomes[x][1]
    #print total
    return total

def selectPopulation(chromosomes,totalValue):

    outputChromosomes=[]

    for x in range(len(chromosomes)):
        dividend = float(chromosomes[x][1])
        divisor=float(totalValue)
        value=(dividend/divisor)*100
        finalValue= (int('%0.f' % value))
        #print chromosomes[x][0]
        finalX=deConvertPopulation(chromosomes[x][0])
        for i in range(1,finalValue):
            outputChromosomes.append(finalX)
            #print outputChromosomes
        #print finalValue
        #print value
    #print "Total number of chromosomes "+str(len(outputChromosomes))

        #print outputChromosomes
    #print chromosomes
    #print chromosomes[x][1]
   #print totalValue
    return outputChromosomes

    #print chromosomes
    #print len(chromosomes)

def crossPopulation(chromosomes, mutationRate):

    outputChromosomes=[]
    chance = random.random()
    lotus = random.randint(0,6)

    if (chance<=mutationRate):
        if(len(chromosomes)%2==0):
            k=1
        else:
            k=2
        for x in range(0,len(chromosomes)-k,2):
            element1 = list(chromosomes[x])
            element2 = list(chromosomes[x + 1])
            for i in range(7, lotus, -1):
                if '0' in element1[i] and '1' in element2[i]:
                    element1[i] = '1'
                    element2[i] = '0'
                elif '1' in element1[i] and '0' in element2[i]:
                    element1[i] = '0'
                    element2[i] = '1'
                else:
                    element1[i] = element1[i]
                    element2[i] = element2[i]
            element1 = "".join(element1)
            element2 = "".join(element2)
            outputChromosomes.append(element1)
            outputChromosomes.append(element2)
        if k == 2:
            outputChromosomes.append(chromosomes[len(chromosomes)-1])

        #print list(outputChromosomes)
        return list(outputChromosomes)
    else:
        print "No crossing during this iteration!"
        #print chromosomes
        return chromosomes

def mutatePopulation(chromosomes,mutationRate):
    outputChromosomes = []
    chance = random.random()
    lotus = random.randint(0, 7)
    element=random.randint(0,len(chromosomes)-1)
    if (chance <= mutationRate):
        #print chromosomes
        chromosome=list(chromosomes[element])
        #print chromosome
        #print chromosome[lotus]
        #print chromosome
        #print chromosomes
        if '0' in chromosome[lotus]:
            chromosome[lotus] = '1'
        else:
            chromosome[lotus] = '0'

        chromosome="".join(chromosome)
        #print chromosomes
        #print chromosome
        #print chromosome[lotus]
        outputChromosomes=chromosomes
        outputChromosomes[element]=chromosome

        #print chromosomes
        return outputChromosomes



    else:
        print "No mutation during this iteration!"
        return chromosomes
n=20
population=initializePopulation(listInitial[random.randint(0,9)],n) #random initial population is picked once.
#insert randomized population with values set to 0 here
iteration = 0
stop = 'y'
while stop == 'y':
    print "selected population: " + str(sorted(population))
    populationBin = convertPopulation(population)
    populationBin = crossPopulation(populationBin,0.0)
    populationBin = mutatePopulation(populationBin,0.9)
    population=ratePopulation(population,populationBin)
    #print "values" +str
    totalValue=countTotal(population)
    population=selectPopulation(population,totalValue)
    population=initializePopulation(population,n)
    iteration+=1;
    print "Iteration:" +str(iteration)

    stop = raw_input("Continue?<y/n> ")






