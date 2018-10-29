#MenuTitle: Match Anchors Between Layers
# -*- coding: utf-8 -*-
__doc__="""
Matches anchors from one master to another. 

Assumes there are exactly two masters, and you want to 
copy anchors with same position from first master 
(e.g. "Regular") to second master (e.g. "Bold").
"""

import copy

font = Glyphs.font

for glyph in font.glyphs:
    if len(glyph.layers[0].anchors) !=  len(glyph.layers[1].anchors):
        print glyph.name
        # go through anchors
        for anchor in glyph.layers[0].anchors:
            # check if anchor exists in the anchors of next master
            if anchor.name not in glyph.layers[1].anchors.values():
                print anchor.name, anchor.x, anchor.y
                glyph.layers[1].anchors = copy.copy(glyph.layers[0].anchors)
                print "copied!"
                print "------", "\n" # separate anchors copied
        print "======", "\n" # separate glyphs