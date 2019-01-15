#MenuTitle: Set horizontal guides to x=0
# -*- coding: utf-8 -*-
__doc__="""
If a guide has a 0 deg slope, set its origin to x=0. 

This just cleans up your edit view a bit. :)
"""

font = Glyphs.font

for master in font.masters:
    for guide in master.guides:
        if guide.angle == 0.0 or guide.angle == 180.0:
            print(guide.position.x)
            guide.position= NSPoint(0, guide.position.y)
