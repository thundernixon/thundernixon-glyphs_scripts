#MenuTitle: Make Split Files with Instance familyName
# -*- coding: utf-8 -*-
__doc__="""
Separate a two-axis family into multiple weight-only Glyphs files.
File separated based on Instance custom parameter `familyName`.
Assumes a rectangular designspace. (?)
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
buildPath = parentFilePath + "/build"

if os.path.exists(buildPath) == False:
    os.mkdir(buildPath)

# # make new glyph font doc for each familyName in list
for currentFamilyName in splitFamilies:
    buildFileName = currentFamilyName.replace(" ", "-") + "-build.glyphs"
    
    buildFilePath = os.path.split(font.filepath)[0] + "/build/" + buildFileName

    print(buildFileName)
    print(buildFilePath)
    font.save((buildFilePath))

    currentFont = Glyphs.open((buildFilePath), True)

#     # TODO: make currentFont family name = currentFamilyName

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
    

#     # make masters from each end of that instance for the current secondary axis
#         # ~MAKE DEF ABOVE~ make master from instance makeMaster(instance, index) # 
#             # get instance.interpolatedFont
#             # f.masters.append(instanceFont.masters[index])
#             # get new master ID
#             # copy in glyphs
#             # copy in kerning

#     # assumes instances are ordered by weight value (this may need to be an added step above)

    # currentBoldFont = currentFont.instances[-1].interpolatedFont
    # print(currentBoldFont.fontMasters()[0].id)
    # currentFont.masters.append(currentBoldFont.masters[0])
    # currentBoldFontMasterID = currentBoldFont.fontMasters()[0].id

    # currentBoldFontMasterID = currentBoldFont.fontMasters()[0].id
    # print(currentBoldFontMasterID)

    # for glyph in currentFont.glyphs:
    #     # make variable for glyph of interpolated font
    #     currentBoldGlyph = currentBoldFont.glyphs[glyph.name]
    #     # bring glyph data into glyph of new master
    #     glyph.layers[currentBoldFontMasterID] = currentLightGlyph.layers[currentBoldFontMasterID]

    

    # currentFont.save(buildFilePath)

    # # make an interpolated font of the new instance
    # currentLightFont = currentFont.instances[0].interpolatedFont
    
    # print(currentLightFont.fontMasters()[0])
    # print(currentLightFont.fontMasters()[0].id)
    
    # # add the master of the interpolated font to the masters
    # currentFont.masters.append(currentLightFont.masters[0])

    # # get the id from the master of the interpolated font
    # currentLightFontMasterID = currentLightFont.fontMasters()[0].id
    # print(currentLightFontMasterID)


    # for glyph in currentFont.glyphs:
    #     # make variable for glyph of interpolated font
    #     currentLightGlyph = currentLightFont.glyphs[glyph.name]
    #     # bring glyph data into glyph of new master
    #     glyph.layers[currentLightFontMasterID] = currentLightGlyph.layers[currentLightFontMasterID]

    # currentFont.save(buildFilePath)

    # currentBoldFont = currentFont.instances[len(currentInstances)-1].interpolatedFont
    # print(currentBoldFont.fontMasters()[0])
    # print(currentBoldFont.fontMasters()[0].id)


    currentFont.close()

Glyphs.open("/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/sources/build/Encode-Sans-SemiCondensed-build.glyphs", True)

#     currentLightFontMasterID = currentLightFont.fontMasters()[0].id()
#     currentBoldFontMasterID = currentBoldFont.fontMasters()[0].id()

#     # currentFont.fontMasters().append(currentLightFont.fontMasters[0])
#     # currentFont.fontMasters().append(currentBoldFont.fontMasters[0])
#     # currentFont.insertFontMaster_atIndex_(currentLightFont.fontMasters()[0], 0)
#     # currentFont.insertFontMaster_atIndex_(currentBoldFont.fontMasters()[0],1)
#     currentFont.addFontMaster_(currentLightFont.fontMasters()[0])
#     currentFont.addFontMaster_(currentBoldFont.fontMasters()[0])

#     newLightMaster = currentFont.fontMasters()[-2]
#     newBoldMaster = currentFont.fontMasters()[-1]
#     newLightMasterID = newLightMaster.id()
#     newBoldMasterID = newBoldMaster.id()

#     for index,glyph in enumerate(currentFont.glyphs()):
#         # make variable for glyph of interpolated font
#         # currentGlyph = currentFont.glyphs()[glyph.name()]
#         currentGlyph = currentFont.glyphs()[index]

#         ## these need to be layer indexes, it seems
#         # bring glyph data into glyph of new master
#         glyph.layers()[newMasterID] = currentGlyph.layers()[currentLightFontMasterID]
#         # bring glyph data into glyph of new master
#         glyph.layers()[newMasterID] = currentGlyph.layers()[currentBoldFontMasterID]

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

# #  


# # for instance in font.instances():
# #     for param in instance.customParameters():
# #         print(param)
# #     # print(instance.customParameters)
# #     print(instance.interpolatedFont)
#     # print(instance.interpolatedFont().font().fontMasters()[0].name())
#     # if re.match('^Light$', instance.name()) != None or re.match('^Black$', instance.name()) != None:
#     #     print(instance.interpolatedFont().font().fontMasters()[0].name())
#     #     font.addFontMaster_(instance.interpolatedFont().font().fontMasters()[0])

# # for master in font.fontMasters():
# #    print(master.name())


# font.save((str(directory + "/" + filename)))
# document.close(True)