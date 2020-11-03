import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_single_char(self):
        self.assertTrue(TestLexer.checkLexeme("x", "x,<EOF>", 101))

    def test_lower_many_char(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 102))

    def test_lower_many_char_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("fk yu", "fk,yu,<EOF>", 103))

    def test_upper_single_char(self):
        self.assertTrue(TestLexer.checkLexeme("Y", "Error Token Y", 104))

    def test_upper_many_char(self):
        self.assertTrue(TestLexer.checkLexeme("XYZ", "Error Token X", 105))

    def test_lower_upper_char(self):
        self.assertTrue(TestLexer.checkLexeme("koDCak", "koDCak,<EOF>", 106))

    def test_lower_char_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("afc45", "afc45,<EOF>", 107))
      
    def test_upper_char_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("RU58I", "Error Token R", 108))

    def test_mix_character(self):
        self.assertTrue(TestLexer.checkLexeme("gtx1080TI", "gtx1080TI,<EOF>", 109))

    def test_mix_first_upper_character(self):
        self.assertTrue(TestLexer.checkLexeme("Yy58io", "Error Token Y", 110))

    def test_underline(self):
        self.assertTrue(TestLexer.checkLexeme("_", "Error Token _", 111))

    def test_char_with_underline_first(self):
        self.assertTrue(TestLexer.checkLexeme("_abc_xyz", "Error Token _", 112))

    def test_char_with_underline(self):
        self.assertTrue(TestLexer.checkLexeme("s_A5", "s_A5,<EOF>", 113))

    def test_single_number(self):
        self.assertTrue(TestLexer.checkLexeme("9", "9,<EOF>", 114))

    def test_integer(self):
        self.assertTrue(TestLexer.checkLexeme("152836", "152836,<EOF>", 115))

    def test_number_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("2 6  84", "2,6,84,<EOF>", 116))

    def test_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("a8", "a8,<EOF>", 117))

    def test_many_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("a85789", "a85789,<EOF>", 118))

    def test_number_many_character(self):
        self.assertTrue(TestLexer.checkLexeme("auy8lo", "auy8lo,<EOF>", 119))

    def test_many_number_many_character(self):
        self.assertTrue(TestLexer.checkLexeme("fr59u3op", "fr59u3op,<EOF>", 120))

    def test_number_first_with_character(self):
        self.assertTrue(TestLexer.checkLexeme("25yui98", "25,yui98,<EOF>", 121))

    def test_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("88 yu t5", "88,yu,t5,<EOF>", 122))

    def test_complex_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("8yu iu y8 5u", "8,yu,iu,y8,5,u,<EOF>", 123))

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("3.5", "3.5,<EOF>", 124))

    def test_float_unary(self):
        self.assertTrue(TestLexer.checkLexeme("-5.6", "-,5.6,<EOF>", 125))

    def test_float_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("5.9  6.8", "5.9,6.8,<EOF>", 126))

    def test_float_error_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("5. 9", "5,.,9,<EOF>", 127))

    def test_float_error_character(self):
        self.assertTrue(TestLexer.checkLexeme("6.a9d", "6,.,a9d,<EOF>", 128))

    def test_single_e(self):
        self.assertTrue(TestLexer.checkLexeme("e5", "e5,<EOF>", 129))

    def test_float_with_e_1(self):
        self.assertTrue(TestLexer.checkLexeme("5e4", "5e4,<EOF>", 130))

    def test_float_with_e_2(self):
        self.assertTrue(TestLexer.checkLexeme("5.89e58", "5.89e58,<EOF>", 131))

    def test_float_with_e_unary_number(self):
        self.assertTrue(TestLexer.checkLexeme("89e-5", "89e-5,<EOF>", 132))

    def test_float_with_e_error(self):
        self.assertTrue(TestLexer.checkLexeme("1.5e", "1.5,e,<EOF>", 133))

    def test_single_E(self):
        self.assertTrue(TestLexer.checkLexeme("E89", "E89,<EOF>", 134))

    def test_float_with_E_1(self):
        self.assertTrue(TestLexer.checkLexeme("7E5", "7E5,<EOF>", 135))

    def test_float_with_E_2(self):
        self.assertTrue(TestLexer.checkLexeme("6.E7", "6.E7,<EOF>", 136))

    def test_float_with_E_unary_number(self):
        self.assertTrue(TestLexer.checkLexeme("7.89E+64", "7.89E+64,<EOF>", 137))

    def test_float_with_E_error(self):
        self.assertTrue(TestLexer.checkLexeme("7.89E", "7.89,E,<EOF>", 138))

    def test_int_op(self):
        self.assertTrue(TestLexer.checkLexeme("+-*\\%", "+,-,*,\,%,<EOF>", 139))

    def test_int_op_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("8+92\\7", "8,+,92,\,7,<EOF>", 140))

    def test_int_op_character(self):
        self.assertTrue(TestLexer.checkLexeme("th%i-q", "th,%,i,-,q,<EOF>", 141))

    def test_int_op_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("8-at*9", "8,-,at,*,9,<EOF>", 142))

    def test_int_op_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("89  * 6 \\   a", "89,*,6,\,a,<EOF>", 143))

    def test_int_op_number_character_other_token(self):
        self.assertTrue(TestLexer.checkLexeme("as+_", "as,+,Error Token _", 144))

    def test_float_op(self):
        self.assertTrue(TestLexer.checkLexeme("+.-.*.\\.", "+.,-.,*.,\.,<EOF>", 145))

    def test_float_op_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("8+.92\\7", "8,+.,92,\,7,<EOF>", 146))

    def test_float_op_character(self):
        self.assertTrue(TestLexer.checkLexeme("th*.i-.q", "th,*.,i,-.,q,<EOF>", 147))

    def test_float_op_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("8-.at*.9", "8,-.,at,*.,9,<EOF>", 148))

    def test_float_op_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("89  *. 6 \\.   a", "89,*.,6,\.,a,<EOF>", 149))

    def test_float_op_number_character_other_token(self):
        self.assertTrue(TestLexer.checkLexeme("as+._", "as,+.,Error Token _", 150))

    def test_int_bool_op(self):
        self.assertTrue(TestLexer.checkLexeme("><>=<=!=", ">,<,>=,<=,!=,<EOF>", 151))

    def test_int_bool_op_number(self):
        self.assertTrue(TestLexer.checkLexeme("5<=9", "5,<=,9,<EOF>", 152))

    def test_int_bool_op_character(self):
        self.assertTrue(TestLexer.checkLexeme("er>p", "er,>,p,<EOF>", 153))

    def test_int_bool_op_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("ty>8!=59", "ty,>,8,!=,59,<EOF>", 154))

    def test_int_bool_op_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("ty  >  9", "ty,>,9,<EOF>", 155))

    def test_int_bool_op_number_character_other_token(self):
        self.assertTrue(TestLexer.checkLexeme("5>#<9", "5,>,Error Token #", 156))

    def test_float_bool_op(self):
        self.assertTrue(TestLexer.checkLexeme("=/=>.<.>=.<=.", "=/=,>.,<.,>=.,<=.,<EOF>", 157))

    def test_float_bool_op_number(self):
        self.assertTrue(TestLexer.checkLexeme("5<=9", "5,<=,9,<EOF>", 158))

    def test_float_bool_op_character(self):
        self.assertTrue(TestLexer.checkLexeme("er>p", "er,>,p,<EOF>", 159))

    def test_float_bool_op_number_character(self):
        self.assertTrue(TestLexer.checkLexeme("ty>8!=59", "ty,>,8,!=,59,<EOF>", 160))

    def test_float_bool_op_number_character_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme("ty  >  9", "ty,>,9,<EOF>", 161))

    def test_float_bool_op_number_character_other_token(self):
        self.assertTrue(TestLexer.checkLexeme("5>#<9", "5,>,Error Token #", 162))

    def test_bool_literal(self):
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 163))
        
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 164))

    def test_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme("""\"""", """\",<EOF>""", 165))

    def test_many_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme("""\"\"\"\"\"\"""", """"","","",<EOF>""", 166))

    def test_quote(self):
        self.assertTrue(TestLexer.checkLexeme("""\'""", """\',<EOF>""", 167))

    def test_many_quote(self):
        self.assertTrue(TestLexer.checkLexeme("""\'\'\'\'\'\'""", """'','','',<EOF>""", 168))

    def test_string_literal_lower(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"hello\" """, """"hello",<EOF>""", 169))

    def test_string_literal_upper(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"MEGA\" """, """"MEGA",<EOF>""", 170))

    def test_string_literal_number(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"789632145\" """, """"789632145",<EOF>""", 171))

    def test_string_literal_special_token(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"+)-#&<.\" """, """"+)-#&<.",<EOF>""", 172))

    def test_string_literal_whitespace(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"  8  _p\" """, """"  8  _p",<EOF>""", 173))

    def test_string_literal_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"er\yui\" """, """Illegal Escape In String: er\y""", 174))

    def test_string_literal_backslash_number(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"er\5\" """, """"er\5",<EOF>""", 175))

    def test_string_literal_backslash_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"er\n8\" """, """Unclosed String: er""", 176))

    def test_double_quote_character_number(self):
        self.assertTrue(TestLexer.checkLexeme("""e5\"6\"""", """e5,"6",<EOF>""", 177))

    def test_many_double_quote_mix(self):
        self.assertTrue(TestLexer.checkLexeme(""" nh8\"  2r\"+ """, """nh8,"  2r",+,<EOF>""", 178))

    def test_quote_character_number(self):
        self.assertTrue(TestLexer.checkLexeme("""3v\'s6rg\'""", """3,v,\',s6rg,\',<EOF>""", 179))

    def test_many_quote_mix(self):
        self.assertTrue(TestLexer.checkLexeme(""" d\'\'a+8\'6+o """, """d,\'\',a,+,8,\',6,+,o,<EOF>""", 180))

    def test_whitespaces(self):
        self.assertTrue(TestLexer.checkLexeme("9\n8\r  5", """9,8,5,<EOF>""", 181))

    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("**Hi**", "**Hi**,<EOF>", 182))

    def test_comment_with_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme("**violet\n**", """**violet

**,<EOF>""", 183))

    def test_comment_wrong_form(self):
        self.assertTrue(TestLexer.checkLexeme("** a**b **", "** a**,b,Unterminated Comment", 184))

    def test_hexadecimal_integer_with_x(self):
        self.assertTrue(TestLexer.checkLexeme("0xAF", "0xAF,<EOF>", 185))

    def test_hexadecimal_integer_with_X(self):
        self.assertTrue(TestLexer.checkLexeme("0X2D6", "0X2D6,<EOF>", 186))

    def test_hexadecimal_integer_with_0(self):
        self.assertTrue(TestLexer.checkLexeme("0X0", "0X0,<EOF>", 187))

    def test_hexadecimal_integer_error(self):
        self.assertTrue(TestLexer.checkLexeme("0X5T2", "0X5,Error Token T", 188))

    def test_octal_integer_with_o(self):
        self.assertTrue(TestLexer.checkLexeme("0o65", "0o65,<EOF>", 189))

    def test_octal_integer_with_O(self):
        self.assertTrue(TestLexer.checkLexeme("0O124", "0O124,<EOF>", 190))

    def test_octal_integer_with_0(self):
        self.assertTrue(TestLexer.checkLexeme("0o0", "0o0,<EOF>", 191))

    def test_octal_integer_error(self):
        self.assertTrue(TestLexer.checkLexeme("0O82", "0,Error Token O", 192))

    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme("$", "Error Token $", 193))

    def test_error_tokens(self):
        self.assertTrue(TestLexer.checkLexeme("@^#", "Error Token @", 194))

    def test_error_token_with_character(self):
        self.assertTrue(TestLexer.checkLexeme("a+i$", "a,+,i,Error Token $", 195))

    def test_error_token_with_number(self):
        self.assertTrue(TestLexer.checkLexeme("98-9@5", "98,-,9,Error Token @", 196))

    def test_error_token_with_backslash(self):
        self.assertTrue(TestLexer.checkLexeme("\#", "\,Error Token #", 197))

    def test_error_token_in_comment(self):
        self.assertTrue(TestLexer.checkLexeme(" ** $&@~ **", "** $&@~ **,<EOF>", 198))

    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 199))

    def test_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** abc def  """, """Unterminated Comment""", 200))
