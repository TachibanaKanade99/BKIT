import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    # Test Identifiers:
    def test_lower_id(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_id_followed_by_uppercase(self):
        self.assertTrue(TestLexer.checkLexeme("abcABC", "abcABC,<EOF>", 102))

    def test_lower_id_followed_by_uppercase_and_lowercase(self):
        self.assertTrue(TestLexer.checkLexeme("abcDef", "abcDef,<EOF>", 103))

    def test_lower_id_with_digit(self):
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 104))

    def test_id_with_lower_uppercase_and_digit(self):
        self.assertTrue(TestLexer.checkLexeme("abcABC123", "abcABC123,<EOF>", 105))

    def test_id_with_lower_digit_uppercase(self):
        self.assertTrue(TestLexer.checkLexeme("abc123ABC", "abc123ABC,<EOF>", 106))

    def test_id_with_uppercase(self):
        self.assertTrue(TestLexer.checkLexeme("ABCabc", "Error Token A", 107))

    def test_id_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("123abc", "Error Token 1", 108))

    def test_id_with_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("_abc", "Error Token _", 109))

    def test_id_with_lower_followed_by_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("abc_ABC123", "abc_ABC123,<EOF>", 110))

    def test_id_with_lower_and_underscore_only(self):
        self.assertTrue(TestLexer.checkLexeme("aB_1", "aB_1,<EOF>", 111))

    def test_id_with_lower_only(self):
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>", 112))

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**comment**", "<EOF>", 113))

    def test_block_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ ** this is a fsjfksjfls 
                 * multi-line
                 * comment.
                 **""",
            "<EOF>",
        114))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

