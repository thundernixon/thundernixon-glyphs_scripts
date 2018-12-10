#MenuTitle: Make Split Instances into Masters
# -*- coding: utf-8 -*-
__doc__="""
A second step after script "Make Split Files with Instance familyName."
"""


f = Glyphs.font

def instanceToMaster(index):
    # make an interpolated font of the new instance
	instanceFont = f.instances[index].interpolatedFont
	# add the master of the interpolated font to the masters
	f.masters.append(instanceFont.masters[0])
	# get the id from the master of the interpolated font
	newMasterID = instanceFont.masters[0].id
	
	for glyph in f.glyphs:
	    # make variable for glyph of interpolated font
		instanceGlyph = instanceFont.glyphs[glyph.name]
	    # bring glyph data into glyph of new master
		glyph.layers[newMasterID] = instanceGlyph.layers[newMasterID]

    # bring kerning in from interpolated font
	f.kerning[newMasterID] = instanceFont.kerning[newMasterID]

instanceToMaster(0)
instanceToMaster(-1)

lenMasters = len(f.masters)

deleteCount = 0

for index, master in enumerate(f.masters):
    # delete old master
    print(index)
    if index <= (lenMasters - 2 - 1):
        print(deleteCount, index)
        del f.masters[deleteCount]
        
    print("--------------")