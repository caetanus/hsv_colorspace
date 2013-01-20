# -*- coding: utf-8 -*-
import math

class hsl(object):

    @classmethod
    def parse_colorstring(cls, color_string):
        assert color_string.startswith('#')
        assert color_string.count('#') == 1
        color_string = color_string[1:]
        assert len(color_string) in (3, 6)
        if len(color_string) == 3:
            return [int(i + '0',16)\
                    for i in color_string]
        else:
            r = int(color_string[:2], 16)
            g = int(color_string[2:4], 16)
            b = int(color_string[4:6], 16)
            
            return [r,g,b]

    @classmethod
    def fromrgb(cls, color_string):
        r, g, b = cls.parse_colorstring(color_string)

        l_max = max((r, g, b))
        l_min = min((r, g, b))

        h = s = l = (l_max - l_min) / 2.

        if l_max == l_min:
            h = s = 0

        else:
            diff = float(l_max - l_min)
            s = diff / (2 - l_max - l_min)\
                    if l > 0.5 \
                    else diff / (l_max - l_min)

            if r == l_max:
                h = (g - b) / diff + (6. \
                                    if g < b\
                                    else 0)
            elif g == l_max:
                h = (b - r) / diff + 2
            
            elif b == l_max:
                h = (r - g) / diff + 4

            h /= 6.
        
        return (h, s, l)

    @classmethod
    def torgb_tuple(cls, h, s, v):
        h = (h%1 + 1) % 1
        i = int(math.floor(h * 6))
        f = h * 6 - i
        p = v * (1 - s)
        q = v * (1 - s*f)
        t = v * (1 - s*(1 - f))
        if i == 0:
            return [v, t, p]
        elif i == 1:
            return [q, v, p]
        elif i == 2:
            return [p, v, t]
        elif i == 3:
            return [p, q, v]
        elif i == 4:
            return [t, p, v]
        elif i == 5:
            return [v, p, q]
    
    @classmethod
    def torgb(cls, h, s, v):
        r, g, b = cls.torgb_tuple(h, s, v)
        return "#%02X%02X%02X" % (r, g, b)

