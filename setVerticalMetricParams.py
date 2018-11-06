#MenuTitle: Set Vertical Metric Params
# -*- coding: utf-8 -*-
__doc__="""
  Assumes the masters keep the same vertical metrics. I am not sure whether winAscent and winDescent should be different between masters, otherwise, but you should check if that's the case before using this script on a font where min/max heights are different between styles. 
"""

font = Glyphs.font

font.customParameters["Use Typo Metrics"] = True

# starter values
maxDescent = 0
maxAscent = 0

# find highest and lowest point in font
for glyph in font.glyphs:
  for layer in glyph.layers:
    
    # get descender of current layer
    descent = layer.bounds.origin.y
    
    # get ascender of current layer
    ascent = layer.bounds.size.height + descent  

    # if descent/ascent of current layer is greater than previous max descents/ascents, update the max descent/ascent
    if descent <= maxDescent:
      maxDescent = descent
      
    if ascent >= maxAscent:
      maxAscent = ascent
      

# check values for sanity
print(maxDescent, maxAscent)

# make lineGap so that the total of `ascent + descent + lineGap` equals 120% of UPM size

UPM = font.upm

totalSize = maxAscent + abs(maxDescent)

lineGap = int((UPM * 1.2)) - totalSize

print(UPM, UPM * 1.2, totalSize, lineGap)

# use highest/lowest points to set custom parameters for winAscent and winDescent
# following vertical metric schema from https://github.com/googlefonts/gf-docs/tree/master/VerticalMetrics
for master in font.masters:

  # Typo Ascender = either Cap Height or Ascender height, whichever is tallest
  if master.ascender >= master.capHeight:
    typoAscender = master.ascender
  else:
    typoAscender = master.capHeight
  master.customParameters["typoAscender"] = typoAscender

  # Typo Descender = Typo Ascender - UPM
  typoDescender = typoAscender - UPM
  master.customParameters["typoDescender"] = typoAscender - UPM
  
  # Typo LineGap = 0.25 * UPM
  typoLineGap = 0.25 * UPM
  master.customParameters["typoLineGap"] = typoLineGap

  # Hhea Ascender = Typo Ascender
  master.customParameters["hheaAscender"] = typoAscender

  # Hhea Descender = Typo Descender
  master.customParameters["hheaDescender"] = typoDescender

  # Hhea LineGap = Typo LineGap
  master.customParameters["hheaLineGap"] = typoLineGap


  # Win Ascent = Font bbox yMax
  master.customParameters["winAscent"] = maxAscent
  # Win Descent = Font bbox yMin
  master.customParameters["winDescent"] = abs(maxDescent)
  
  

