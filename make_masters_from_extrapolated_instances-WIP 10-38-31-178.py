
#MenuTitle: Masters from Extrapolated Instances
# -*- coding: utf-8 -*-
__doc__="""
Goes through all instances and makes the heaviest and lightest into masters, if these don't already exist.
"""

font = Glyphs.font

instWghtDict= {}

for instance in font.instances:
# 	print(instance.weightValue)
	if instance.name not in instWghtDict:
		instWghtDict[instance.name] = []
    # add weights into lists of dictionary
	instWghtDict[instance.name].append(instance.weightValue)

print(instWghtDict)

# find heaviest and lightest instances

def getExtemeInstances(axisDict):
    simplifiedDict = {}

    # go through dictionary
    for key in instWghtDict:
        # reduce each value list into max and min values
        simplifiedDict[key]=[max(instWghtDict[key]),min(instWghtDict[key])]

    print(simplifiedDict)

    # find list with highest value

    

    # find list with lowest value

    # # get key of max and min values
    # maxInstance = max(simplifiedDict, key=simplifiedDict.get)
    # minInstance = min(simplifiedDict, key=simplifiedDict.get)

    # # return max and min keys and values
    # return(maxInstance, simplifiedDict[maxInstance], minInstance, simplifiedDict[minInstance])

print(getExtemeInstances(instWghtDict))

# make master of lightest instance in dictionary
    #check if one exists at that value already

# make master of heaviest instance
    #check if one exists at that value already


{u'--------': [100.0, 100.0, 100.0], u'Extrabold': [1170.0, 1089.0, 1170.0, 1089.0], u'Semibold': [650.0, 577.0, 650.0, 577.0], u'Bold': [920.0, 843.0, 920.0, 843.0], u'Light': [50.0, -15.0, 50.0, -15.0], u'Regular': [360.0, 291.0, 360.0, 291.0], u'Black': [1350.0, 1265.0, 1350.0, 1265.0]}

# blackMaster = GSFontMaster()
# blackMaster.name = "Black"
# Font.masters.append(blackMaster)