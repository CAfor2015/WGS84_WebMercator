#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pi as PI
from math import log, tan, atan, exp

# lonLat is from GPS's WGS84
# webMercator is the fromat in baidumap, googlemap

# longitude and latitude to web Mercator
def convertor1(lonLat):
  x = lonLat[0]
  y = log(tan(lonLat[1]+90)*PI/360))/(PI/180)
  return map(lambda x: x*20037508.34/180 , [x, y])

# web Mercator to longitude and latitude
def convertor2(mercator):
  x, y = map(lambda x: x/20037508.34*180 , mercator)
  y = 180/PI*(2*atan(exp(y*PI/180))-PI/2)
  return [x, y]


