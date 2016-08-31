from strokeHMMbasic import*
execfile("strokeHMMbasic.py")
x = StrokeLabeler()
x.trainHMMDir("../trainingFiles/") #../ means go back a directory
x.testHMMDir("../trainingFiles/")
