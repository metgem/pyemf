#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from builtins import range
from past.utils import old_div
import pyemf

print("Test of SetPixel")

width=8
height=6
dpi=100
pointstopixels=dpi/72.0

emf=pyemf.EMF(width,height,dpi,verbose=False)

for x in range(150,500):
    y=old_div(x,2)
    emf.SetPixel(x,y,(0x80,x%256,0x90))
print("after SetPixel")


ret=emf.save("test-setpixel.emf")
print("save returns %d" % ret)

