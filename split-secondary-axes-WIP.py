#MenuTitle: Make Split Files with Instance familyName
# -*- coding: utf-8 -*-
__doc__="""
Separate a two-axis family into multiple weight-only Glyphs files.
File separated based on Instance custom parameter `familyName`.
Assumes a rectangular designspace. (?)

Currently only splitting files and isolating associated instances. Not yet updating masters.

TODO: only try to make instances into masters where they *do not* match existing master values.
E.g. in Encode Sans Condensed, simply delete Extended masters, 
but in Encode Sans Extended, only delete Condensed masters,
but in between, move interpolated instances into new masters, then delete old ones.

TODO: also update the extreme master names (new masters take on extreme instance names, 
and also the split masters shouldn't have width names)
"""


font = Glyphs.font

Glyphs.showMacroWindow()
typeFamilyName = font.familyName

print(typeFamilyName)


# # if axes besides Weight & Width exist, get this as a dictionary
styleAxes = font.customParameters['Axes']

print(styleAxes)

# # make list for custom-axis families
splitFamilies = []

# # go through instances
for instance in font.instances:
    customFamilyName = instance.customParameters["familyName"]

    if customFamilyName != None:
        splitFamilies.append(customFamilyName)
    else:
        splitFamilies.append(typeFamilyName)


# # de-duplicate families list
splitFamilies = set(splitFamilies)

print(splitFamilies)

parentFilePath = os.path.split(font.filepath)[0]
buildPath = parentFilePath + "/split"

if os.path.exists(buildPath) == False:
    os.mkdir(buildPath)

# # make new glyph font doc for each familyName in list
for currentFamilyName in splitFamilies:
    buildFileName = currentFamilyName.replace(" ", "-") + "-split.glyphs"
    
    buildFilePath = os.path.split(font.filepath)[0] + "/split/" + buildFileName

    print(buildFileName)
    print(buildFilePath)
    font.save((buildFilePath))

    currentFont = Glyphs.open((buildFilePath), True)

    # make currentFont family name = currentFamilyName
    currentFont.familyName = currentFamilyName

#     # make list of current instances, delete others
    currentInstances = []

    for index, instance in enumerate(currentFont.instances):

        hasFamilyNameParam = False

        if instance.customParameters["familyName"] != None:
            hasFamilyNameParam = True

            if instance.customParameters["familyName"] == currentFamilyName:
                    currentInstances.append(index)
        

        # if there's not a "familyName" param and the currentFamilyName matches the overall name, it's a default style
        if instance.customParameters["familyName"] == None and currentFamilyName == typeFamilyName:
            currentInstances.append(index)
            # print(instance.interpolationWidth())

    print(currentInstances, currentFamilyName)

    # in each new file, delete instances that don't match the current width

    deleteCounter = 0
    indexCounter = 0

    for instance in currentFont.instances:
        if indexCounter not in currentInstances:
            currentFont.removeObjectFromInstancesAtIndex_(deleteCounter)

        if indexCounter in currentInstances:
            deleteCounter += 1
        
        indexCounter += 1

    currentFont.save(buildFilePath)

#     # assumes instances are ordered by weight value (this may need to be an added step above)

    # def instanceToMaster(index):
    #     # make an interpolated font of the new instance
    #     instanceFont = currentFont.instances[index].interpolatedFont
    #     # add the master of the interpolated font to the masters
    #     currentFont.masters.append(instanceFont.masters[0])
    #     # get the id from the master of the interpolated font
    #     newMasterID = instanceFont.masters[0].id

    #     for glyph in currentFont.glyphs:
    #         # make variable for glyph of interpolated font
    #         instanceGlyph = instanceFont.glyphs[glyph.name]
    #         # bring glyph data into glyph of new master
    #         glyph.layers[newMasterID] = instanceGlyph.layers[newMasterID]

    #     # bring kerning in from interpolated font
    #     # currentFont.kerning[newMasterID] = instanceFont.kerning[newMasterID]

    # instanceToMaster(0)
    # instanceToMaster(-1)

    # currentFont.save(buildFilePath)

    # lenMasters = len(currentFont.masters)

    # deleteCount = 0

    # for index, master in enumerate(currentFont.masters):
    #     # delete old master
    #     print(index)
    #     if index <= (lenMasters - 2 - 1):
    #         print(deleteCount, index)
    #         del currentFont.masters[deleteCount]
            
    #     print("--------------")


    currentFont.save(buildFilePath)

    # currentFont.close()

# Glyphs.open("/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/sources/build/Encode-Sans-SemiCondensed-build.glyphs", True)


#     # delete previous masters
#         # for index, master in enumerate(masters):
#             # if index != or index == len(masters):
#                 # delete master

#     # delete secondary axis 
#         # for axis in font.axes
#             # if axis.name != "Weight"
#                 # del axis

#     # font.save((str(directory + "/" + buildFileName)))
#     # document.close(True)

# # result: should be several fonts, each with just 

# ## assuming there aren't middle masters for weight

# # get lightest and boldest masters


# font.save((str(directory + "/" + filename)))
# document.close(True)