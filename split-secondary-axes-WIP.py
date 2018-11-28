#MenuTitle: Make Split Files with Instance familyName
# -*- coding: utf-8 -*-
__doc__="""
Separate a two-axis family into multiple weight-only Glyphs files.
File separated based on Instance custom parameter `familyName`.
Assumes a rectangular designspace. (?)
"""

currentFont = Glyphs.font

currentLightFont = currentFont.instances[0].interpolatedFont

print(currentLightFont)
print(currentLightFont.masters)