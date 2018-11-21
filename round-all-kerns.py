#MenuTitle: Round All Kerns
# -*- coding: utf-8 -*-
__doc__="""
If there are any floating-point kern values in the font, this will round them to the nearest integer.
"""

font = Glyphs.font

# print(font.kerning)

# for each value in kerning dictionary
for key, value in font.kerning.items():
    for key, value in font.kerning.items():
        print(value)
        # if type(value) == float
        if type(value) == float:
            print(value)
            # print(value)
            # value = round(value)
            # print(value)