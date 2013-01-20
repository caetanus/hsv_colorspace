# -*- coding: utf-8 -*-
import math

class ColorParsingError(Exception):
    pass

class hsv(object):

    @classmethod
    def parse_colorstring(cls, color_string):
        if not color_string.startswith('#'):
            raise ColorParsingError, "string must starts with #"
        if color_string.count('#') != 1:
            raise ColorParsingError, "invalid colorstring"
        color_string = color_string[1:]

        if not (len(color_string) in (3, 6)):
            raise ColorParsingError, "string must have 4 or 7 lenght"

        if len(color_string) == 3:
            return [int(i + '0',16)\
                    for i in color_string]
        else:
            r = int(color_string[:2], 16)
            g = int(color_string[2:4], 16)
            b = int(color_string[4:6], 16)
            
            return (r, g, b)
    
    @classmethod
    def _get_hue_and_chroma(cls, r, g, b):
        
        return hd / 6

    @classmethod
    def fromrgb(cls, color_string):
        r, g, b = cls.parse_colorstring(color_string)
        
        r /= 255.
        g /= 255.
        b /= 255.
        
        M = max((r, g, b))
        m = min((r, g, b))
        v = M
        c = M - m
        if c == 0.0:
            h = s = 0
        else:
            s = c / M
            delta_color = lambda color: (((M - color) / 6) + (c / 2.)) / c
            del_R = delta_color(r)
            del_G = delta_color(g)
            del_B = delta_color(b)
            
            if M == r:
                h = del_B - del_G 
            elif M == g:
                h =  (1 / 3.) + del_R - del_B 
            else: #if M == b:
                h = (2 / 3.) + del_G - del_R 
            
        if h < 0:
            h += 1.
        if h > 1:
            h += 1
            
        h *= 360.0
        s *= 100.
        v *= 100.
        
        return tuple([int(round(i)) for i in (h, s, v)])
          

    @classmethod
    def torgb_tuple(cls, h, s, v):

        h /= 360.
        s /= 100.
        v /= 100.

        if s == 0:
            r = g = b = v 
        
        else:
            h *= 6.
            i = math.floor(h)
            v1 = v * (1 - s)
            v2 = v * (1 - s * (h - i))
            v3 = v * (1 - s * (1 - (h - i)))
            
            if i == 0:
                r, g, b = v, v3, v1
            elif i == 1:
                r, g, b = v2, v, v1
            elif i == 2:
                r, g, b = v1, v, v3
            elif i == 3:
                r, g, b = v1, v2, v
            elif i == 4:
                r, g, b = v3, v1, v
            else: #if i == 5:
                r, g, b = v, v1, v2
            
        r = int(round(r * 255))
        g = int(round(g * 255))
        b = int(round(b * 255))
        return (r, g, b) 
    
    @classmethod
    def torgb(cls, h, s, v):
        r, g, b = cls.torgb_tuple(h, s, v)
        return "#%02X%02X%02X" % (r, g, b)

