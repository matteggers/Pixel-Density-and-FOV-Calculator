import math
import numpy as np

#tvDimensions = {
#   
#   
#   "70": [61, 34.3],
#   "75": [65.4, 36.8]
#   
#   
#}
reference_dimension = [65.4, 36.8]


user_size = int(input("What is the size of your screen? Round to the nearest increment of 5. \n"))
#user_distance = int(input("How far will you be from the screen?"))
#user_media = int(input("Please input height of the media station the TV will sit on.")) #add option for wall mounting and exception to the 3 inch addition of stand
#view_height = 0 #make user optino to default to 42.


range_identifier = list(range(40,80, 5))


#print(range_identifier)
#print(type(range_identifier))



def sizeCalculator():
    global index_multiplier
    
    if user_size in range_identifier:
        size_index = range_identifier.index(user_size)
        index_multiplier = size_index - range_identifier.index(75)
        
    return index_multiplier, size_index, user_size
          
def lowerEstimate():
    lowerAlg = []
    
    lowerAlgWidth = round((reference_dimension[0] - (-4.4 * index_multiplier)), 2)
    lowerAlg.append(lowerAlgWidth)
    
    lowerAlgHeight = round((reference_dimension[1] - (-2.5 * index_multiplier)), 2)
    lowerAlg.append(lowerAlgHeight)
    
    print(lowerAlg)
    return lowerAlg, lowerAlgWidth, lowerAlgHeight
    
def UpperEstimate():
    upperAlg = []
    
    upperAlgWidth = round((reference_dimension[0] - (-4.3 * index_multiplier)), 2)
    upperAlg.append(upperAlgWidth)
    
    upperAlgHeight = round((reference_dimension[1] - (-2.5 * index_multiplier)), 2)
    upperAlg.append(upperAlgHeight)
    
    print(upperAlg)
    return upperAlg, upperAlgWidth, upperAlgHeight
    
def caller():
    sizeCalculator()
    lowerEstimate()
    UpperEstimate()
    
caller()

              


 
#subtract index of reference by user_size to get index and use to multiple and subtract
    






#create formula for height and width additions of screens based on a pillar size.
# add option for link to bestbuy link and get exact width


#increments of 5 increase x by [] and y by []