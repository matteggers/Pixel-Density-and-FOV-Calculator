import math
import numpy as np
import atexit
import json

reference_dimension = [65.4, 36.8] # 75 inch TV is reference. Currently only works with TV's =< 75, will soon work with numbers above
range_identifier = list(np.arange(40,80, 0.5))
sizeData = {
    40: '',
    45: '',
    50: '',
    55: '',
    60: '',
    65: '',
    70: '',
            }

def userInput():
    global user_size
    global user_distance
    
    try:
        user_size = float(input("What is the size of your screen? Round to the nearest half inch. \n"))
        user_size = round((user_size * 2) / 2 )
        user_distance = float(input("How far will you be from the screen in inches?\n"))
    except ValueError as Error:
        print(Error)
        exit()
    return user_size, user_distance


def sizeCalculator(user_size): #Finds the multiplier for physical size calculations by finding index difference
    global index_multiplier
    global size_index #-----------
    
    try:
        if user_size in range_identifier: 
            size_index = range_identifier.index(user_size) / 10
            index_multiplier = size_index - range_identifier.index(75) / 10
    except NameError as Error:
        print(Error)
        exit()
    return index_multiplier, size_index, user_size

          
def lowerEstimate(): #Uses dimension differences that result in lower estimations of width/height
    global lowerAlg
    
    lowerAlg = []
    
    lowerAlgWidth = round((reference_dimension[0] - (-4.4 * index_multiplier)), 2)
    lowerAlg.append(lowerAlgWidth)
    
    lowerAlgHeight = round((reference_dimension[1] - (-2.5 * index_multiplier)), 2)
    lowerAlg.append(lowerAlgHeight)
    
    return lowerAlg, lowerAlgWidth, lowerAlgHeight


def UpperEstimate(): #Uses dimension differences that result in upper estimations of width/height
    global upperAlg
    
    upperAlg = []
    
    upperAlgWidth = round((reference_dimension[0] - (-4.3 * index_multiplier)), 2)
    upperAlg.append(upperAlgWidth)
    
    upperAlgHeight = round((reference_dimension[1] - (-2.5 * index_multiplier)), 2)
    upperAlg.append(upperAlgHeight)
    
    return upperAlg, upperAlgWidth, upperAlgHeight

    
def lowerTriangulation(): #Gets the viewing angle: Pythag. Theorem -> arcsin for viewing angle -> * 2 for total
    global lowerViewEstimate
    
    a = (lowerAlg[0] / 2)
    b = user_distance
    c = math.sqrt((a*a) + (b*b))
    halfViewAngle = math.asin(a/c)
    lowerViewEstimate = round(((halfViewAngle * 100) * 2), 2) #Upper estimate of viewing angle of the nearest degree
    
    return a, b, c, halfViewAngle, lowerViewEstimate

    
def upperTriangulation(): #Gets the viewing angle: Pythag. Theorem -> arcsin for viewing angle -> * 2 for total
    global upperViewEstimate
    
    a = (upperAlg[0] / 2)
    b = user_distance
    c = math.sqrt((a*a) + ((b*b)))
    halfViewAngle = math.asin(a/c)
    upperViewEstimate = round(((halfViewAngle * 100) * 2), 2) #Upper estimate of viewing angle to the nearest degree

    return a, b, c, halfViewAngle, upperViewEstimate

    
def fovCheck():
    global fovEstimate
    fovEstimate = []
    
    fovEstimate.append(lowerViewEstimate)
    fovEstimate.append(upperViewEstimate)
    
    if fovEstimate[1] in np.arange(49,53,0.01): #49-52 degrees is optimal viewing.
        print(f"Your FOV with a {user_size} inch screen is between {fovEstimate[0]} and {fovEstimate[1]} degrees. This is an optimal viewing FOV.")
    if fovEstimate[1] > 60:
        print(f"Your FOV with a {user_size} inch screen is between {fovEstimate[0]} and {fovEstimate[1]} degrees. It should be below 60 degrees to remain within a human's Image Recognition FOV.")
        exit()
    elif fovEstimate[1] < 60:
        print(f"Your FOV with a {user_size} inch screen is between {fovEstimate[0]} and {fovEstimate[1]} degrees, which is below 60 degrees. Your FOV is within an acceptable range.")
        exit() 
        

def exit():

    return atexit.register(lambda: input("Press Enter to exit.")) #found on S/O


def caller():
    userInput()
    sizeCalculator(user_size)
    lowerEstimate()
    UpperEstimate()
    lowerTriangulation()
    upperTriangulation()
    fovCheck()

caller()
            
        
    
def dataWriter():
    slicedDimensions = [40, 45, 50, 55, 60, 65, 70, 75]
    #upperViewList = []
    
    for i in slicedDimensions:
        sizeCalculator(user_size=i)
        UpperEstimate()
        upperTriangulation()
        #upperViewList.append(i)
        #print(f"{i} inch screen")
        #print(f"{upperViewEstimate} Degrees - UPPER VIEW ESTIMATE\n")
        sizeData.update({i : upperViewEstimate})
        print(sizeData)
dataWriter()

##create function that asks what viewing distance, then shows max tv size. for loop
#for i in __ if viewing angle is greater than 60 discard and move on. if below 60 print size