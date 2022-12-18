import math
#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php


#commonDimensions = {'24': [20.918, 11.766],
#                    '24.5': [21.354, 12.011]
#    
#    }
#
#
#
##math.sqrt((w*w)+(h*h))
#
#def pixelDensity(size):
#    values = list(commonDimensions.get(size))
#    w = values[0]
#    h = values[1]
#    
#    pixDens = math.sqrt((w*w)+(h*h))
#    print(pixDens)
#    return pixDens
#    
#
#size = input("What is the diagonal screen size in inches? ")
#
#
#pixelDensity(size)


def diagonalPixels(size):
    w = 1920
    h = 1080
    res = math.sqrt((w*w) + (h*h))
    rounded_res = round(res, 2)
    
    PPI = rounded_res // size
    print(PPI)
    
    #print(res)
    return res, PPI

size = input("Diagonal size of monitor: ")



diagonalPixels(int(size))



#def callAll():
#    diagonalPixels(int(size))