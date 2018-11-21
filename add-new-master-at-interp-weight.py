#MenuTitle: Adjust Master weight
# -*- coding: utf-8 -*-
__doc__="""
Add new master at interpolated position, then delete existing master. Good for subtle adjustments in a build process. Set variables in script to configure.
"""

### set vars ##########################

oldMasterWeightValue = 400.0
newMasterWeightValue = 440.0

#######################################

f = Glyphs.font

# create new instance
newInstance = GSInstance()
f.instances.append(newInstance)

# set new instance weight value to variable from above
newInstance.weightValue = newMasterWeightValue

# make an interpolated font of the new instance
instanceFont = f.instances[-1].interpolatedFont
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

for i, instance in enumerate(f.instances):
    # delete generated instance
    if instance.weightValue == newMasterWeightValue:
        print("delete " + str(instance))
        del f.instances[i]

for i, master in enumerate(f.masters):
    # delete old master
    if master.weightValue == oldMasterWeightValue:
        print("delete " + str(master))
        del f.masters[i]
    # set new master value as old master value (round to nearest integer to match)
    if round(master.weightValue) == round(newMasterWeightValue):
        print("update weight value of " + str(master))
        f.masters[i].weightValue = oldMasterWeightValue
