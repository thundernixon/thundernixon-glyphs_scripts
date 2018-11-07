#MenuTitle: Add Caret Anchor
# -*- coding: utf-8 -*-
__doc__="""
If a ligature has no 'caret_1' anchors, this will add one in the horizontal middle, at the baseline.

If run again, it will add subsequent `caret` anchors with a suffix of `_2`, `_3`, etc, adding 50 units each time.

You need to manually reposition added anchors to sensible positions.

This script could be smarter, but I'm doing a limited quantity of glyphs, so it doesn't make sense to over-optimize.

Assumes there are not anchors named simply 'caret'.
"""

layer = Glyphs.font.selectedLayers[0] # current layer

# get middle of baseline
middle = int(round(layer.width / 2))

currentAnchors = []

# access all anchors:
for a in layer.anchors:
    currentAnchors.append(a.name)

print(currentAnchors)

if 'caret_1' not in currentAnchors:
    # add a new anchor called 'caret'
    layer.anchors['caret_1'] = GSAnchor()
    
    # set position of caret to (middle, 0)
    layer.anchors['caret_1'].position = NSPoint(middle, 0)

else:

    carets = []

    for a in layer.anchors:
        if 'caret' in a.name:
            carets.append(a.name)


    newCaret = 'caret_' + str((len(carets) + 1))
    # add a new anchor
    layer.anchors[newCaret] = GSAnchor()

    # distance to move new caret anchors, to avoid overlap
    unitsToMove = 50

    # set position
    layer.anchors[newCaret].position = NSPoint(middle, 0)
    # increase vertical position by 50 units
    layer.anchors[newCaret].position = NSPoint(layer.anchors[newCaret].position.x + (unitsToMove * len(carets)), 0)