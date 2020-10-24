import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #test identifiers -5
    def test_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("abcAB", "abcAB,<EOF>", 101))
    def test_identifier_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("abc12", "abc12,<EOF>", 102))
    def test_identifier_wrong_id(self):
        self.assertTrue(TestLexer.checkLexeme("_123", "Error Token _", 103))
    def test_identifier_id_underscores(self):
        self.assertTrue(TestLexer.checkLexeme("123ac", "123,ac,<EOF>", 104))
    def test_identifier_id_with_uppercase(self):
        self.assertTrue(TestLexer.checkLexeme("abcAB", "abcAB,<EOF>", 105))
    #test integer-5
    def test_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 106))
    def test_integer_with_character(self):
        self.assertTrue(TestLexer.checkLexeme("123a", "123,a,<EOF>", 107))
    def test_wrong_integer(self):
        self.assertTrue(TestLexer.checkLexeme("-123", "-,123,<EOF>", 108))
    def test_integer_start_with_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 109))
    def test_integer_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 110))
    def test_integer_hexa_number(self):
        self.assertTrue(TestLexer.checkLexeme("0x123", "0x123,<EOF>", 111))
    def test_integer_hexa_number_X(self):
        self.assertTrue(TestLexer.checkLexeme("0X123", "0X123,<EOF>", 112))
    def test_integer_Octal(self):
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>", 113))
    def test_integer_Octal_O(self):
        self.assertTrue(TestLexer.checkLexeme("0O123", "0O123,<EOF>", 114))
    def test_integer_hexa_upercase(self):
        self.assertTrue(TestLexer.checkLexeme("0xABC", "0xABC,<EOF>", 115))
    #test float number
    def test_float_number_1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0", "12.0,<EOF>", 116))
    def test_float_number_2(self):
        self.assertTrue(TestLexer.checkLexeme("12.3", "12.3,<EOF>", 117))
    def test_float_number_3(self):
        self.assertTrue(TestLexer.checkLexeme("12000.", "12000.,<EOF>", 118))
    def test_float_number_4(self):
        self.assertTrue(TestLexer.checkLexeme("12e+5", "12e+5,<EOF>", 119))
    def test_float_number_5(self):
        self.assertTrue(TestLexer.checkLexeme("2e-1", "2e-1,<EOF>", 120))
    def test_float_number_6(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e9", "12.0e9,<EOF>", 121))
    def test_float_number_7(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3", "12.0e3,<EOF>", 122))
    def test_float_number_8(self):
        self.assertTrue(TestLexer.checkLexeme("12e3", "12e3,<EOF>", 123))
    def test_float_number_9(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5", "12.e5,<EOF>", 124))
    def test_float_number_10(self):
        self.assertTrue(TestLexer.checkLexeme("12000e-1", "12000e-1,<EOF>", 125))
    #test keywords-21
    def test_keyword_body(self):
        self.assertTrue(TestLexer.checkLexeme("Body", "Body,<EOF>", 126))
    def test_keyword_Else(self):
        self.assertTrue(TestLexer.checkLexeme("Else", "Else,<EOF>", 127))
    def test_keyword_EndFor(self):
        self.assertTrue(TestLexer.checkLexeme("EndFor", "EndFor,<EOF>", 128))
    def test_keyword_If(self):
        self.assertTrue(TestLexer.checkLexeme("If", "If,<EOF>", 129))
    def test_keyword_Var(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 130))
    def test_keyword_EndDo(self):
        self.assertTrue(TestLexer.checkLexeme("EndDo", "EndDo,<EOF>", 131))
    def test_keyword_Break(self):
        self.assertTrue(TestLexer.checkLexeme("Break", "Break,<EOF>", 132))
    def test_keyword_ElseIf(self):
        self.assertTrue(TestLexer.checkLexeme("ElseIf", "ElseIf,<EOF>", 133))
    def test_keyword_EndWhile(self):
        self.assertTrue(TestLexer.checkLexeme("EndWhile", "EndWhile,<EOF>", 134))
    def test_keyword_Parameter(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter", "Parameter,<EOF>", 135))
    def test_keyword_While(self):
        self.assertTrue(TestLexer.checkLexeme("While", "While,<EOF>", 136))
    def test_keyword_Continue(self):
        self.assertTrue(TestLexer.checkLexeme("Continue", "Continue,<EOF>", 137))
    def test_keyword_EndBody(self):
        self.assertTrue(TestLexer.checkLexeme("EndBody", "EndBody,<EOF>", 138))
    def test_keyword_For(self):
        self.assertTrue(TestLexer.checkLexeme("For", "For,<EOF>", 139))
    def test_keyword_Return(self):
        self.assertTrue(TestLexer.checkLexeme("Return", "Return,<EOF>", 140))
    def test_keyword_True(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 141))
    def test_keyword_Do(self):
        self.assertTrue(TestLexer.checkLexeme("Do", "Do,<EOF>", 142))
    def test_keyword_EndIf(self):
        self.assertTrue(TestLexer.checkLexeme("EndIf", "EndIf,<EOF>", 143))
    def test_keyword_Function(self):
        self.assertTrue(TestLexer.checkLexeme("Function", "Function,<EOF>", 144))
    def test_keyword_Then(self):
        self.assertTrue(TestLexer.checkLexeme("Then", "Then,<EOF>", 145))
    def test_keyword_False(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 146))
    #test operators-24
    def test_operator_add(self):
        self.assertTrue(TestLexer.checkLexeme("1+2", "1,+,2,<EOF>", 147))
    def test_operator_mul(self):
        self.assertTrue(TestLexer.checkLexeme("1*2", "1,*,2,<EOF>", 148))
    def test_operator_mod(self):
        self.assertTrue(TestLexer.checkLexeme("1%2", "1,%,2,<EOF>", 149))
    def test_operator_equal(self):
        self.assertTrue(TestLexer.checkLexeme("1==2", "1,==,2,<EOF>", 150))
    def test_operator_lessthanorequal(self):
        self.assertTrue(TestLexer.checkLexeme("1<=2", "1,<=,2,<EOF>", 151))
    def test_operator_larger_float(self):
        self.assertTrue(TestLexer.checkLexeme("12.3>.2.4", "12.3,>.,2.4,<EOF>", 152))
    def test_operator_add_float(self):
        self.assertTrue(TestLexer.checkLexeme("12.3+.2.4", "12.3,+.,2.4,<EOF>", 153))
    def test_operator_mul_float(self):
        self.assertTrue(TestLexer.checkLexeme("12.3*.2.4", "12.3,*.,2.4,<EOF>", 154))
    def test_operator_lessorequal_float(self):
        self.assertTrue(TestLexer.checkLexeme("3.5<=.4.5", "3.5,<=.,4.5,<EOF>", 155))
    def test_operator_largerorequal_float(self):
        self.assertTrue(TestLexer.checkLexeme("4.5>=.3.5", "4.5,>=.,3.5,<EOF>", 156))
    def test_operator_sub_float(self):
        self.assertTrue(TestLexer.checkLexeme("4.5-.3.5", "4.5,-.,3.5,<EOF>", 157))
    def test_operator_div_float(self):
        self.assertTrue(TestLexer.checkLexeme("4.5\.3.5", "4.5,\.,3.5,<EOF>", 158))
    def test_operator_lessthan_float(self):
        self.assertTrue(TestLexer.checkLexeme("4.5<.5.5", "4.5,<.,5.5,<EOF>", 159))
    def test_operator_not(self):
        self.assertTrue(TestLexer.checkLexeme("!3", "!,3,<EOF>", 160))
    def test_operator_not_equal(self):
        self.assertTrue(TestLexer.checkLexeme("3!=4", "3,!=,4,<EOF>", 161))
    def test_operator_larger_than_or_equal(self):
        self.assertTrue(TestLexer.checkLexeme("4>=3", "4,>=,3,<EOF>", 162))
    def test_operator_minus(self):
        self.assertTrue(TestLexer.checkLexeme("-3", "-,3,<EOF>", 163))
    def test_operator_div(self):
        self.assertTrue(TestLexer.checkLexeme("6\\3", "6,\,3,<EOF>", 164))
    def test_operator_and(self):
        self.assertTrue(TestLexer.checkLexeme("True&&False", "True,&&,False,<EOF>", 165))
    def test_operator_smaller_than(self):
        self.assertTrue(TestLexer.checkLexeme("4<9", "4,<,9,<EOF>", 166))
    def test_operator_differ(self):
        self.assertTrue(TestLexer.checkLexeme("3=/=4", "3,=/=,4,<EOF>", 167))
    def test_operator_or(self):
        self.assertTrue(TestLexer.checkLexeme("True || False", "True,||,False,<EOF>", 168))
    def test_operator_larger_than(self):
        self.assertTrue(TestLexer.checkLexeme("5>3", "5,>,3,<EOF>", 169))
    def test_operator_assign(self):
        self.assertTrue(TestLexer.checkLexeme("a=3", "a,=,3,<EOF>", 170))
    #test separators-7
    def test_seperator_round_bracket(self):
        self.assertTrue(TestLexer.checkLexeme("(a)", "(,a,),<EOF>", 171))
    def test_seperator_square_bracket(self):
        self.assertTrue(TestLexer.checkLexeme("[a]", "[,a,],<EOF>", 172))
    def test_seperator_colon(self):
        self.assertTrue(TestLexer.checkLexeme("a:b", "a,:,b,<EOF>", 173))
    def test_seperator_dot(self):
        self.assertTrue(TestLexer.checkLexeme("a.b", "a,.,b,<EOF>", 174))
    def test_seperator_comma(self):
        self.assertTrue(TestLexer.checkLexeme("a,b", "a,,,b,<EOF>", 175))
    def test_seperator_semicolon(self):
        self.assertTrue(TestLexer.checkLexeme("a;b", "a,;,b,<EOF>", 176))
    def test_seperator_pathensis(self):
        self.assertTrue(TestLexer.checkLexeme("{a}", "{,a,},<EOF>", 177))
    #test boolean-3
    def test_boolean_true(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 178))
    def test_boolean_false(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 179))
    def test_wrong_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("false true", "false,true,<EOF>", 180))
    #test comment-5
    def test_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**abc**", "<EOF>", 181))
    def test_multiline_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**a*b*c***", "<EOF>", 182))
    def test_comment_with_multi_star(self):
        self.assertTrue(TestLexer.checkLexeme("** * **", "<EOF>", 183))
    def test_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**abc", "Unterminated Comment", 184))
    def test_unterminated_comment_with_star(self):
        self.assertTrue(TestLexer.checkLexeme("***abc*", "Unterminated Comment", 185))
    #test string-5
    def test_normal_string(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello"''',"Hello,<EOF>", 186))
    def test_normal_string_with_escape(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello\\b"''',"Hello\\b,<EOF>", 187))
    def test_normal_string_with_escape_t(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello\\t"''',"Hello\\t,<EOF>", 188))
    def test_normal_string_contain_single_quote(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello:'"TA'"''',"Hello:'TA',<EOF>", 189))
    def test_normal_string_containing_tab(self):
        self.assertTrue(TestLexer.checkLexeme('''"this is a string containing tab \\t"''',"this is a string containing tab \\t,<EOF>", 190))
 
    #test unclosed string-2
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme('''Hello"''','''Unclosed String: Hello"''', 191))
    def test_unclosed_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello''','''Error Token "''', 192))
    #illegal escape-3
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello\z"''','''Illegal Escape In String: "Hello\z''', 193))
    def test_illegal_escape_inside_string(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello\z my friend"''','''Illegal Escape In String: "Hello\z''', 194))
    def test_illegal_escape_some(self):
        self.assertTrue(TestLexer.checkLexeme('''"Hello\z my\t friend"''','''Illegal Escape In String: "Hello\z''', 195))
    #test more complex -5
    def test_normal_string_containing_some_tabs(self):
        self.assertTrue(TestLexer.checkLexeme('''"this is a string\\b containing tab \\t"''',"this is a string\\b containing tab \\t,<EOF>", 196))
    def test_normal_string_containing_some_tabs_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a\nb" """,'''Unclosed String:  "''', 197))
    def test_unterminated_comment_left(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc** ""","""Unterminated Comment""", 198))
    def test_unterminated_complex_string(self):
        self.assertTrue(TestLexer.checkLexeme('''"abcde"''','''abcde,<EOF>''', 199))
    def test_unterminated_complex_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('''"abcde"''','''abcde,<EOF>''', 200))
    
    
    
    









    
    
    
 


 
  

 


   