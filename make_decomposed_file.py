#MenuTitle: Make New Decomposed Glyphs File
# -*- coding: utf-8 -*-
__doc__="""
Goes through all glyphs in the current file and decomposes components.

From the tutorial at https://glyphsapp.com/tutorials/scripting-glyphs-part-3
"""

from shutil import copyfile
# import os

font = Glyphs.font
fontPath = font.filepath

# make a copy of the current font file
def makeDecomposedCopy(fontPath):

    decomposedGlyphsPath = fontPath.replace(".glyphs", "-decomposed.glyphs")
    
    copyfile(fontPath, decomposedGlyphsPath)
    return(decomposedGlyphsPath)

# make a copy of the current font file
def decomposeAllGlyphs(font, fontPath):

    newFontPath = makeDecomposedCopy(fontPath)
    Glyphs.open(newFontPath)
    newFont = Glyphs.font

    print "Decomposed glyphs:"

    for glyph in newFont.glyphs:
        for layer in glyph.layers:
            if len(layer.components) >= 0:
                for component in layer.components:
                    component.decompose()
                    print ".",

    return(newFont)
 
 
decomposeAllGlyphs(font, fontPath)