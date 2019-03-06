#MenuTitle: Remove All Caret Anchors
# -*- coding: utf-8 -*-
__doc__="""
If a font has carets marked in ligatures, this will rename them.

This is to prevent failing OTS checks -- see https://github.com/googlefonts/fontbakery/issues/2268.
"""

font = Glyphs.font

for glyph in font.glyphs:
    for layer in glyph.layers:
        for anchor in layer.anchors:
            if "caret" in anchor.name:
                print glyph.name, anchor
                anchor.name = anchor.name.replace("caret", "lig_carrot_temp_off")
                print glyph.name, anchor