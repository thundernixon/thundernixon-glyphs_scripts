#MenuTitle: Center Selected Anchors
# -*- coding: utf-8 -*-
__doc__="""
If an anchor is selected, it will be centered in the current glyph.

Example:
- If the glyph /H is `1624` units wide, the selected "top" 
  anchor will be moved to x = 1624/2 = 812.
"""

layer = Glyphs.font.selectedLayers[0] # current layer
print layer

for anchor in layer.anchors:
    
    if anchor.selected == True:
        print anchor.x
        print layer.width
        centerXpos = layer.width/2
        anchor.x = centerXpos

        print(anchor.name, " moved to ", str(centerXpos))