from StrokeHmm import*
execfile("StrokeHmm.py")
x = StrokeLabeler()
x.trainHMMDir("../trainingFiles/") #../ means go back a directory
x.testHMMDir("../trainingFiles/")
