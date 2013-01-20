from unittest import TestCase

from hsv import hsv, ColorParsingError

class hsvTestCase(TestCase):
    colortest1 = "#FAFAFA"
    colortest1_hsv = (0, 0, 98)
    colortest2 = "#233009"
    colortest2_hsv = (80, 81, 19)
    colortest3 = "#FF1723"
    colortest3_hsv = (357, 91, 100)

    
    def test_rgb_parser_should_pass(self):
        for color_test in [self.colortest1, self.colortest2, self.colortest3]:
            result = hsv.parse_colorstring(color_test)
            result_string = '#' + ''.join(['%X' % i for i in result])
            self.assertEqual(result_string, color_test)

    def test_rgb_parser_should_fail(self):
        self.assertRaises(ColorParsingError,hsv.parse_colorstring,  "ABC")
        self.assertRaises(ColorParsingError,hsv.parse_colorstring, "#FA")
        self.assertRaises(ColorParsingError,hsv.parse_colorstring, "303030")
        self.assertRaises(ColorParsingError,hsv.parse_colorstring, "#FAFAFAF")
        self.assertRaises(ValueError, hsv.parse_colorstring, "#FAFAFI")
        
        
    def test_rgb_parser_should_pass(self):
        hsv.parse_colorstring("#ABC")
        hsv.parse_colorstring("#FAA")
        hsv.parse_colorstring("#FAFAFA")
        
    def test_convert_from_rgb(self):
        self.assertEqual(hsv.fromrgb(self.colortest1), self.colortest1_hsv)
        self.assertEqual(hsv.fromrgb(self.colortest2), self.colortest2_hsv)
        self.assertAlmostEqual(hsv.fromrgb(self.colortest3), self.colortest3_hsv)
    
    def test_convert_to_rgb(self):
        self.assertEqual(hsv.torgb(*self.colortest1_hsv), self.colortest1)
        self.assertEqual(hsv.torgb(*self.colortest2_hsv), self.colortest2)
        self.assertEqual(hsv.torgb(*self.colortest3_hsv), self.colortest3)
        