# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
#Ejercicio 7.10

#Modificá el código anterior para ponerles nombres a los ejes ("tiempo" y distancia al origen") y al gráfico.
#Graficá 12 trayectorias en la misma figura, con diferentes colores.
#Usá la estructura de subplots sugerida en el Ejercicio 7.9 para graficar tres pubplots en una figura:
#Arriba, grande, 12 trayectorias aleatorias como en el inciso anterior
#Abajo a la izquierda la trayectoria que más se aleja del origen.
#Abajo a la derecha la trayectoria que menos se aleja del origen.
#Ojo, cuando decimos la que más o menos se aleja, nos referimos a en algún momento, no necesariamente a la que termina más cerca o más lejos.
#%%

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import random, pylab
 

#%%
def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()
#%%
N = 100000
trayectorias = 12
distancias_maximas = []
walks = []

fig = plt.figure() #dpi=100
plt.subplot(2, 1, 1)

for _ in range(trayectorias):
    walk = randomwalk(N)
    distancias_maximas.append(max(abs(walk)))
    walks.append(walk)
    
    plt.plot(walk,'-',linewidth=0.5)
    plt.xticks([]), plt.yticks([-500,0,500]), plt.ylim(-900,900)
    plt.title('12 caminatas al azar',fontsize=14)
    ax = plt.gca()
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    plt.axhline(y=0, color = 'black', linewidth=0.1, alpha = 0.65)


plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
#%%
for i,dist in enumerate(distancias_maximas):
    if dist == max(distancias_maximas):
        plt.subplot(2, 2, 3)
        plt.plot(walks[i], color = 'red', label = 'Trayectoria max')
        plt.xticks([]), plt.yticks([-500,0,500]), plt.ylim(-900,900)
        plt.title('Mayor distancia al origen',fontsize=8)
        ax = plt.gca()
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(8)
            label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
        plt.xlabel('Tiempo', fontsize = 8)
        plt.ylabel('Distancia al origen', fontsize = 8)
        plt.axhline(y=0, color = 'red', linewidth=0.2)
        
        
    if dist == min(distancias_maximas):
        plt.subplot(2, 2, 4)
        plt.plot(walks[i], color = 'green', label = 'Trayectoria min')
        plt.xticks([]), plt.yticks([-500,0,500]), plt.ylim(-900,900)
        plt.title('Menor distancia al origen',fontsize=8)
        plt.xlabel('Tiempo', fontsize = 8)
        plt.ylabel('Distancia al origen', fontsize = 8) #Prob:Se superpone en gráfico del costado
        plt.axhline(y=0, color = 'green', linewidth=0.2)
     
#%%
import random 
def random_Walk_2(n):
    x, y = 0, 0
    
    for i in range(n):
        (dx,dy)= random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)
    
lista=[]
for e,i in enumerate(range(25),start=1):
   walk = random_Walk_2(10)
   lista.append(walk)
   print(f'{e}:Cordenada: {walk} \n{e}:Distancia de casa :{abs(walk[0]) + abs(walk[1])}')

lis_x = []
lis_y = []
for x, y in lista:
    lis_x.append(x)
    lis_y.append(y)
xi= lis_x
fi= lis_y
 
#%%
#GRAFICA
plt.plot(xi,fi,'o',label='puntos')# creamos la grafica que nos permita ver los puntos.
plt.xlabel("xi")
plt.ylabel("fi")
plt.title("Puntos Random Walks")
plt.show()
#%%
#Simulacion del Profesor John Guttag

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1
 #%%
class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = x
        self.y = y
 
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)
 
    def getX(self):
        return self.x
 
    def getY(self):
        return self.y
 
    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5
 
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
#%%
class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        #use move method of Location to get new location
        self.drunks[drunk] =\
            self.drunks[drunk].move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
#%%
class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
 
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
#%%
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
#%%
class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.1), (0.0,-0.9),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
#%%
def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
#%%  
def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0,
         dClass a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    Homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer,
                                    numTrials), 1))
    return distances
#%%
def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0
         numTrials an int > 0, dClass a subclass of Drunk
       For each number of steps in walkLengths, runs simWalks with
         numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))
        
random.seed(0)
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
#%%
def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)
        
#random.seed(0)
#simAll((UsualDrunk, MasochistDrunk),
#       (1000, 10000), 100)
#        
#xVals = [1, 2, 3, 4]
#yVals1 = [1, 2, 3, 4]
#pylab.plot(xVals, yVals1, 'b-', label = 'first')
#yVals2 = [1, 7, 3, 5]
#pylab.plot(xVals, yVals2, 'r--', label = 'second')
#pylab.legend()
#%%
class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
 
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
#%%  
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of',
              numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances
#%%
def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle,
                   label = dClass.__name__)
    pylab.title('Mean Distance from Origin ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
#%%
#random.seed(0)
#numSteps = (10,100,1000,10000,100000)
#simAll((UsualDrunk, MasochistDrunk), numSteps, 100)
#
#pylab.plot(numSteps, pylab.array(numSteps)**0.5, 'k-.',
#           label = 'Square root of steps')
#pylab.plot(numSteps, pylab.array(numSteps)*0.05, 'g-.',
#           label = 'numSteps*0.05')
#pylab.legend(loc = 'best')
#%%
def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = OddField()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs
#%%
def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                      label = dClass.__name__ +\
                      ' mean abs dist = <'
                      + str(meanX) + ', ' + str(meanY) + '>')
    pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower center')
 
#random.seed(0)
#plotLocs((UsualDrunk, MasochistDrunk), 10000, 1000)
#%%
class OddField(Field):
    def __init__(self, numHoles = 1000,
                 xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc
 
    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]
#%%           
#TraceWalk using oddField          
def traceWalk(fieldKinds, numSteps):
    styleChoice = styleIterator(('b+', 'r^', 'ko'))
    for fClass in fieldKinds:
        d = UsualDrunk()
        f = fClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label = fClass.__name__)
    pylab.title('Spots Visited on Walk ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'best')
 
#random.seed(0)
#traceWalk((Field, OddField), 500)
#%%