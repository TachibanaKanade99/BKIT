import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """ Simple Program """
        input = """
        Var: a = 5;
        Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_global_variable(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_array_global_variable(self):
        input = """Var: b[2][3] = { {2,3,4}, {4,5,6} };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_multiple_global_variable(self):
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    