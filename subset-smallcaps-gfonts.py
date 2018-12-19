#MenuTitle: Subset Smallcaps for Gfonts
# -*- coding: utf-8 -*-
__doc__="""
Make a separate glyphs file that replaces lowercase glyphs with small caps, for exporting via FontMake.
"""

smallCapSuffix = ".smcp"

font = Glyphs.font

Glyphs.showMacroWindow()
typeFamilyName = font.familyName

# you must redefine components...

for glyph in font.glyphs:
    if smallCapSuffix in glyph.name:
        print(glyph.name)
        rootName = glyph.name.replace(smallCapSuffix, "").lower()

        print(rootName)

        if rootName in font.glyphs:
            del font.glyphs[rootName]
        else:
            "no non-smallcap version of " + glyph.name

for glyph in font.glyphs:
    if smallCapSuffix in glyph.name:
        rootName = glyph.name.replace(smallCapSuffix, "").lower()

        glyph.name = rootName

        for i, component in enumerate(layer.components):
            if smallCapSuffix in component.name:
                component.name = rootName


# make sure kerning is preserved
    # a.smcp v.smcp is -86
    # l.smcp v.smcp is -146
    # it is!

# make sure component glyphs are taken care of
    # correct components
    # correct placement

# fontPath = font.filepath
# font.save((str(fontPath.replace(".glyphs","-sc.glyphs"))))
# document.close(True)