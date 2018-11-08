#MenuTitle: Report Path Direction
# -*- coding: utf-8 -*-
__doc__="""
Go through all glyphs and report path directions.
"""

font = Glyphs.font

clockwise = 0
counterClockwise = 0

for glyph in font.glyphs:
    for layer in glyph.layers:
        for path in layer.paths:
            if path.direction == 1:
                clockwise += 1
            if path.direction == -1:
                counterClockwise += 1

report = "clockwise paths = " + str(clockwise) + "\n" + "counterClockwise paths = " + str(counterClockwise)
print(report)