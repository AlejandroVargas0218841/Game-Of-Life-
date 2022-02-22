"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import date

ON = 255
OFF = 0
vals = [ON, OFF]

contGlider = 0
contBlock = 0
contBeehive=0
contLoaf=0
contBoat=0
contTub=0
contBlinker=0
contToad=0
contBeacon =0
contSpaceship =0 
total =0 

def randomGrid(width, height):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, width*height, p=[0.2, 0.8]).reshape(width, height)

def objEvaluaor(grid , width, height, gens):
    
    
    
    glider = np.array([[0, 0,    0,   0, 0],
                       [0, 0,    0, 255, 0],
                       [0, 255,  0, 255, 0], 
                       [0, 0,  255, 255, 0],
                       [0, 0,    0,   0, 0]])
    
    glider1 = np.array([[0,  0,    0,   0, 0],
                       [0,   0,    255, 0, 0],
                       [0,   0,  0,   255, 0], 
                       [0, 255,  255, 255, 0],
                       [0, 0,    0,   0, 0]])
    
    glider2 = np.array([[0, 0,    0,     0,  0],
                       [0, 255,   0,    255, 0],
                       [0, 0,   255,    255, 0], 
                       [0, 0,   255,    0,   0],
                       [0, 0,    0,     0,   0]])
    
    glider3 = np.array([[0, 0,      0,     0,  0],
                       [0, 255,     0,     0, 0],
                       [0, 0,     255,    255, 0], 
                       [0, 255,   255,    0,   0],
                       [0, 0,    0,     0,   0]])
    
    block  = np.array([[ 0,    0,      0,  0],
                       [ 0,   255,    255, 0],
                       [ 0,   255,    255, 0], 
                       [ 0,   0,        0, 0]])
    
    beehive = np.array([[0, 0,      0,     0,  0,0], #6x5
                       [0, 0,     255,   255, 0, 0],
                       [0, 255,     0,   0, 255, 0], 
                       [0, 0,   255,    255, 0, 0 ],
                       [0, 0,    0,     0,   0 ,0 ]])
    
    loaf   = np.array([[0, 0,      0,     0,   0, 0], #6x6
                       [0, 0,     255,   255,  0, 0],
                       [0, 255,     0,    0, 255, 0], 
                       [0, 0,   255,      0, 255, 0],
                       [0, 0,    0,     255,   0, 0],
                       [0, 0,    0,       0,   0, 0]])
    
    boat = np.array([[0,   0,   0,   0, 0],
                    [0, 255, 255,   0, 0], 
                    [0, 255,   0, 255, 0], 
                    [0,   0, 255,   0, 0],
                    [0,   0,   0,   0, 0]])
    
    tub = np.array([[0,   0,   0,   0, 0],
                    [0,   0, 255,   0, 0], 
                    [0, 255,   0, 255, 0], 
                    [0,   0, 255,   0, 0],
                    [0,   0,   0,   0, 0]])
    
    blinker = np.array([[  0,   0,   0], #3x5
                    [   0, 255,    0], 
                    [   0, 255,    0], 
                    [   0, 255,    0],
                    [   0,   0,    0]])
    
    toad = np.array([[0,  0,   0,     0,   0,   0], #6x5
                    [0,   0,   0,     255,   0, 0], 
                    [0, 255,   0,     0,   255, 0], 
                    [0, 255,   0,     0,   255, 0],
                    [0,   0,   255,   0,   0, 0]])
    
    toad1 = np.array([[0,  0,   0,     0,   0,      0], #6x4
                    [0,   0,   255,     255,   255, 0], 
                    [0, 255,   255,     255,   0,   0], 
                    [0, 0,   0,           0,    0,  0]])
    
    beacon=np.array([[0,    0,   0,     0,   0,  0], #6x6
                    [0,   255, 255,     0,   0, 0], 
                    [0,   255, 255,     0,   0, 0], 
                    [0, 0,   0,     255,   255, 0],
                    [0,   0,   0,   255,   255, 0],
                    [0,    0,   0,     0,   0,  0]])
    
    beacon1=np.array([[0,    0,   0,     0,   0,  0], #6x6
                    [0,   255, 255,     0,   0, 0], 
                    [0,   255, 0,     0,   0, 0], 
                    [0, 0,   0,     0,   255, 0],
                    [0,   0,   0,   255,   255, 0],
                    [0,    0,   0,     0,   0,  0]])
    
    spaceship=np.array([[0,    0,   0,     0,   0,  0,  0], #7x6
                      [0,   255, 0,     0,   255,   0,  0], 
                      [0,   0,  0,     0,      0,  255, 0], 
                      [0, 255,   0,     0,       0, 255, 0],
                      [0,   0,   255,   255,   255, 255,0],
                      [0,    0,   0,     0,   0,  0, 0]])
    
    spaceship1=np.array([[0,    0,   0,     0,   0,  0,  0], #7x6
                      [0,   0,   255,     255,  255, 255,   0], 
                      [0,   255,  0,     0,      0,  255, 0], 
                      [0, 0,   0,     0,       0,    255, 0],
                      [0,   255,   0,   0,   255,      0,  0],
                      [0,    0,   0,     0,   0,  0, 0]])
    
    spaceship2=np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0,   0,   0, 255, 255,   0,   0], 
                        [0, 255, 255,   0, 255, 255,   0], 
                        [0, 255, 255, 255, 255,   0,   0],
                        [0,   0, 255, 255,   0,   0,   0],
                         [0,   0,   0,   0,   0,   0,   0]])
    
    spaceship3 = np.array([[0,   0,   0,   0,   0,   0,   0],
                 [0,   0, 255, 255,   0,   0,   0], 
                 [0, 255, 255, 255, 255,   0,   0], 
                 [0, 255, 255,   0, 255, 255,   0],
                 [0,   0,   0, 255, 255,   0,   0],
                 [0,   0,   0,   0,   0,   0,   0]])
    
    
    
    
    global contGlider
    global contBlock 
    global contBeehive
    global contLoaf
    global contBoat
    global contTub
    global contBlinker
    global contToad
    global contBeacon
    global contSpaceship 
    global total
    
    contGlider = 0
    contBlock = 0
    contBeehive=0
    contLoaf=0
    contBoat=0
    contTub=0
    contBlinker=0
    contToad=0  
    contBeacon =0
    contSpaceship =0 
    total =0 
    
    output = open("output.txt", "a")
    
    for i in range(width):
        for j in range(height):
            if(np.array_equal(grid[ i:i+5, j:j+5] , glider, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider,3), equal_nan=True))):
                contGlider +=1
            if(np.array_equal(grid[ i:i+5, j:j+5] , glider1, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1,3), equal_nan=True))):
                contGlider +=1
            if(np.array_equal(grid[ i:i+5, j:j+5] , glider2, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2,3), equal_nan=True))):
                contGlider +=1
            if(np.array_equal(grid[ i:i+5, j:j+5] , glider3, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3,3), equal_nan=True))):
                contGlider +=1
            if(np.array_equal(grid[ i:i+4, j:j+4] , block, equal_nan=True)):
                contBlock +=1
            if(np.array_equal(grid[ i:i+5, j:j+6] , beehive, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(beehive), equal_nan=True))):
                contBeehive +=1 
            if(np.array_equal(grid[ i:i+6, j:j+6] , loaf, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf), equal_nan=True)) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf, 2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf,3), equal_nan=True))):
                contLoaf +=1
            if(np.array_equal(grid[ i:i+5, j:j+5] , tub, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub,3), equal_nan=True))):
                contTub +=1
            if(np.array_equal(grid[ i:i+5, j:j+3] , blinker, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+3] , np.rot90(blinker), equal_nan=True))):
                contBlinker +=1
            if(np.array_equal(grid[ i:i+5, j:j+6] , toad, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(toad), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(toad,2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(toad,3), equal_nan=True))):
                contToad +=1 
            if(np.array_equal(grid[ i:i+4, j:j+6] , toad1, equal_nan=True) or (np.array_equal(grid[ i:i+4, j:j+6] , np.rot90(toad1), equal_nan=True))):
                contToad +=1
            if(np.array_equal(grid[ i:i+6, j:j+6] , beacon, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon), equal_nan=True))):
                contBeacon +=1
            if(np.array_equal(grid[ i:i+6, j:j+6] , beacon1, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1,3), equal_nan=True))):
                contBeacon +=1
            if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship,3), equal_nan=True))):
                contSpaceship +=1
            if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship1, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1,3), equal_nan=True))):
                contSpaceship +=1
            if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship2, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2,3), equal_nan=True))):
                contSpaceship +=1
            if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship3, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3,3), equal_nan=True))):
                contSpaceship +=1
            

    total = contGlider+contBlock+contBeehive+contLoaf+contBoat+contTub+contBlinker+contToad+contBeacon+contSpaceship
    
    today = date.today()
    output.write("%s  %s\n" %("Simulation at: ", today))
    output.write("%s  %sx%s\n\n" %("Universe Size: ", width, height))
    output.write("%s  %s\n" %("Iteration: ", gens))
    output.write("--------------------------\n")
    output.write("|       \t|  Count  |  Percent  |\n")
    output.write("%s  \t%s\t%s\n" %("Gliders: ", contGlider, (100*contGlider)/total))
    output.write("%s  \t%s\t%s\n" %("Blocks: ", contBlock, (100*contBlock)/total))
    output.write("%s  \t%s\t%s\n" %("Loafs: ", contLoaf, (100*contLoaf)/total))
    output.write("%s  \t%s\t%s\n" %("Tubs: ", contTub, (100*contTub)/total))
    output.write("%s  \t%s\t%s\n" %("Blinkers: ", contBlinker, (100*contBlinker)/total))
    output.write("%s  \t%s\t%s\n" %("Toads: ", contToad, (100*contToad)/total))
    output.write("%s  \t%s\t%s\n" %("Beacons: ", contBeacon, (100*contBeacon)/total))
    output.write("%s  \t%s\t%s\n" %("Spaceships: ", contSpaceship, (100*contSpaceship)/total))
    output.write("%s  %s\n\n\n" %("Total: ", total))
    output.write("--------------------------\n")
    
    
                
    
                
    
                
    
    

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0,    0,   0, 0],
                       [0, 0,    0, 255, 0],
                       [0, 255,  0, 255, 0], 
                       [0, 0,  255, 255, 0],
                       [0, 0,    0,   0, 0]])
    
    grid[i:i+5, j:j+5] = glider
    

def update(frameNum, img, grid, width, height):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(width):
        for j in range(height):
            total = int((grid[i, (j-1)%height] + grid[i, (j+1)%height] +
						grid[(i-1)%width, j] + grid[(i+1)%width, j] +
						grid[(i-1)%width, (j-1)%height] + grid[(i-1)%width, (j+1)%height] +
						grid[(i+1)%width, (j-1)%height] + grid[(i+1)%width, (j+1)%height])/255)
            
            if grid[i,j] == ON:
                if(total<2) or (total > 3):
                    newGrid[i,j]=OFF
            else:
                if total ==3:
                    newGrid[i,j]=ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    
    global contGlider
    global contBlock 
    global contBeehive
    global contLoaf
    global contBoat
    global contTub
    global contBlinker
    global contToad
    global contBeacon
    global contSpaceship 
    global total
    
    
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    parser.add_argument('--tamano-grid', dest='N',required=False)
    parser.add_argument('--archivo-vid', dest='archVid', required=False)
    parser.add_argument('--intervalo', dest='intervalo', required=False)
    parser.add_argument('--deslizador', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
    
    lista=[]
    input="input.txt"
    objInput=open(input, "r")
    lineas = objInput.read().splitlines()
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            signo = palabra.split()
            lista.append(signo)
            
    width = int(lista[0][0])
    height = int(lista[1][0])
    gens = int(lista[4][0])
    
    
        
    
    # set grid size
    #print('Enter the size of your universe: ')
    #N = int(input())
    
    
        
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(width, height)
    # Uncomment lines to see the "glider" demo
    
    celulasVivasX=[]
    celulasVivasY=[]
    
    grid = np.zeros(width*height).reshape(width, height)
    for i in range(6 , len(lista)):
        if lista[i][0].isnumeric():
            if i==0 or i%2==0:
                celulasVivasX.append(int(lista[i][0]))
            else:
                celulasVivasY.append(int(lista[i][0]))
                
    for i, j in zip(celulasVivasX,celulasVivasY):
        addGlider(i, j, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width,height, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()
    
    objEvaluaor(grid , width, height, gens)
    

    

    

# call main
if __name__ == '__main__':
    main()