from unittest import TestCase

from hsl import hsl

class HslTestCase(TestCase):
    colortest1 = "#FAFAFA"
    colortest1_hsl = (0, 0, 98)
    colortest2 = "#233009"
    colortest2_hsl = (80, 81, 19)
    colortest3 = "#FE1721"
    colortest3_hsl = (357, 91, 100)

    
    def test_rgb_parser_should_pass(self):
        for color_test in [self.colortest1, self.colortest2, self.colortest3]:
            result = hsl.parse_colorstring(color_test)
            result_string = '#' + ''.join(['%X' % i for i in result])
            self.assertEqual(result_string, color_test)

    def test_rgb_parser_should_fail(self):
        self.assertRaises(AssertionError,hsl.parse_colorstring("ABC"))
        self.assertRaises(AssertionError,hsl.parse_colorstring("#FA"))
        self.assertRaises(AssertionError,hsl.parse_colorstring("303030"))
        self.assertRaises(AssertionError,Hsl.parse_colorstring("#FAFAFAF"))
        
        
    def test_rgb_parser_should_pass(self):
        hsl.parse_colorstring("#ABC")
        hsl.parse_colorstring("#FAA")
        hsl.parse_colorstring("#FAFAFA")
        
    def test_convert_from_rgb(self):
        self.assertEqual(hsl.fromrgb(self.color_test1), self.colortest1_hsl)
        self.assertEqual(hsl.fromrgb(self.color_test2), self.colortest2_hsl)
        self.assertAlmostEqual(hsl.fromrgb(self.colortest3), self.colortest3_hsl)
    
    def convert_to_rgb(self):
        self.assertEqual(hsl.torgb(*self.colortest1_hsl), self.colortest1)
        self.assertEqual(hsl.torgb(*self.colortest2_hsl), self.colortest2)
        self.assertEqual(hsl.torgb(*self.colortest3_hsl), self.colortest3)
        