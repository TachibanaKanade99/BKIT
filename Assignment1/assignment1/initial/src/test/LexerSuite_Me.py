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
        self.assertTrue(TestLexer.checkLexeme("123 abc", "123,abc,<EOF>", 108))

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

    # Test keywords:

    def test_body_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Bodyabc", "Body,abc,<EOF>", 115))

    def test_body_break_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("abcBody Break","abcBody,Break,<EOF>", 116))

    def test_if_keyword_with_id(self):
        self.assertTrue(TestLexer.checkLexeme("If abc", "If,abc,<EOF>", 117))

    def test_keyword_with_wrong_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var a ABC", "Var,a,Error Token A", 118))

    # Test operators:

    def test_div_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a \ b", "a,\,b,<EOF>", 119))
    
    def test_plus_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a + b", "a,+,b,<EOF>", 120))

    def test_float_plus_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a +. b", "a,+.,b,<EOF>", 121))

    def test_mod_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a % b", "a,%,b,<EOF>", 122))

    def test_not_operator(self):
        self.assertTrue(TestLexer.checkLexeme("If!aBc", "If,!,aBc,<EOF>", 123))

    def test_and_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a&&b&c", "a,&&,b,Error Token &", 124))

    # Test comment:
    
    def test_block_cmt_1(self):
        self.assertTrue(TestLexer.checkLexeme("*****", "*,<EOF>", 125))

    def test_block_cmt_2(self):
        self.assertTrue(TestLexer.checkLexeme("** ***", "*,<EOF>", 126))

    def test_block_cmt_3(self):
        self.assertTrue(TestLexer.checkLexeme("*** **", "<EOF>", 127))

    # Test operators:

    def test_eq_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a==Bc", "a,==,Error Token B", 128))

    def test_not_and_not_eq_operators(self):
        self.assertTrue(TestLexer.checkLexeme("!!=","!,!=,<EOF>", 129))

    def test_less_assign_and_less_eq_operators(self):
        self.assertTrue(TestLexer.checkLexeme("< = <=", "<,=,<=,<EOF>", 130))

    def test_float_not_eq_operator(self):
        self.assertTrue(TestLexer.checkLexeme("a =/=", "a,=/=,<EOF>", 131))

    def test_float_less_and_greater_operators(self):
        self.assertTrue(TestLexer.checkLexeme("a <. >.", "a,<.,>.,<EOF>", 132))
    
    def test_float_less_and_greater_eq_operators(self):
        self.assertTrue(TestLexer.checkLexeme("a <=. bC >=.", "a,<=.,bC,>=.,<EOF>", 133))

    # Test separators:

    def test_dot_separators(self):
        self.assertTrue(TestLexer.checkLexeme("a <. b .", "a,<.,b,.,<EOF>", 134))

    def test_LP_RP_separators(self):
        self.assertTrue(TestLexer.checkLexeme("(a)))", "(,a,),),),<EOF>", 135))

    def test_LB_RB_separators(self):
        self.assertTrue(TestLexer.checkLexeme("{aBC_123abc}{}{{", "{,aBC_123abc,},{,},{,{,<EOF>", 136))

    def test_LSB_RSB_separators(self):
        self.assertTrue(TestLexer.checkLexeme("[a]][]", "[,a,],],[,],<EOF>", 137))

    def test_colon_operator(self):
        self.assertTrue(TestLexer.checkLexeme("*:aBc", "*,:,aBc,<EOF>", 138))
    
    def test_semi_operator(self):
        self.assertTrue(TestLexer.checkLexeme("*;aBc", "*,;,aBc,<EOF>", 139))

    # Test Integer Literals:

    def test_int_lit(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 140))

    def test_large_int_lit(self):
        self.assertTrue(TestLexer.checkLexeme("199", "199,<EOF>", 141))

    def test_hexadecimal_1(self):
        self.assertTrue(TestLexer.checkLexeme("0xFF", "0xFF,<EOF>", 142))

    def test_hexadecimal_2(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC", "0XABC,<EOF>", 143))

    def test_octal_1(self):
        self.assertTrue(TestLexer.checkLexeme("0o567", "0o567,<EOF>", 144))

    def test_octal_2(self):
        self.assertTrue(TestLexer.checkLexeme("0O127", "0O127,<EOF>", 145))

    # Test Float Literals:
    def test_float_lit(self):
        self.assertTrue(TestLexer.checkLexeme("12000e-1", "12000e-1,<EOF>", 146))

    # Test String Literals:
    def test_string_lit(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcabc" """, """abcabc,<EOF>""", 147))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",148))

    # Test Unclose String

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """, 149))

    # Test unterminated cmt:

    def test_unterminated_cmt(self):
        self.assertTrue(TestLexer.checkLexeme("** This is unclose comment", "Unterminated Comment" , 150))

    # Test Illegal escape:

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",151))

    # Test normal string:

    def test_str_with_escape_char_prefix(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\nabc" """, """\\nabc,<EOF>""", 152))

    def test_str_with_escape_char_postfix(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\t" """, """abc\\t,<EOF>""", 153))

    def test_str_with_normal_chars_numbers(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ABCabc123ABC" """, """ABCabc123ABC,<EOF>""", 154))

    def test_str_with_single_quote_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'123\\nABC" """, """abc\\'123\\nABC,<EOF>""", 155))

    def test_str_with_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"ABC" """, """abc'"ABC,<EOF>""", 156))

    # Test variable_decl_tokens:
    def test_var_decl_tokens(self):
        self.assertTrue(TestLexer.checkLexeme("Var: a = 5;", "Var,:,a,=,5,;,<EOF>", 157))

    # Test array literal:
    def test_array_literal(self):
        self.assertTrue(TestLexer.checkLexeme("{1}", "{,1,},<EOF>", 158))

    # Test Illegal Escape for Single quote:
    def test_illegal_escape_for_single_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'abc" ""","""Illegal Escape In String: abc'a""", 159))

    # Test double quotes inside string:
    def test_double_quotes_inside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc123"abc"ABC" """, """abc123,abc,ABC,<EOF>""", 160))

    # Test float number:
    def test_float_number_with_decimal_point(self):
        input = "12.345"
        expect = "12.345,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_float_number_with_decimal_point_and_exp(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3", "12.0e3,<EOF>", 162))

    def test_float_number_with_no_digit_after_decimal_point(self):
        self.assertTrue(TestLexer.checkLexeme("12.", "12.,<EOF>", 163))

    def test_zero_and_float_number(self):
        self.assertTrue(TestLexer.checkLexeme("021.3", "021.3,<EOF>", 164))

    def test_float_number_with_positive_sign_exp(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e+3", "12.3e+3,<EOF>", 165))

    def test_float_number_with_neg_sign(self):
        self.assertTrue(TestLexer.checkLexeme("12e-3", "12e-3,<EOF>", 166))

    # Test string:
    def test_string_with_only_escape_chars(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b\\t\\n\\f\\\\" """, """\\b\\t\\n\\f\\\\,<EOF>""", 167))

    # Test int literals with hexadecimal and octal prefixes:
    def test_hexadecimal_with_prefix_only(self):
        self.assertTrue(TestLexer.checkLexeme("0x 0X", "0,x,0,Error Token X", 168))

    def test_octal_with_prefix_only(self):
        self.assertTrue(TestLexer.checkLexeme("0o 0O", "0,o,0,Error Token O", 169))

    # Test keywords:
    def test_keywords_no_space(self):
        self.assertTrue(TestLexer.checkLexeme("ElseIfIfEndIf", "ElseIf,If,EndIf,<EOF>", 170))

    # Test negative value in intlit and floatlit:
    def test_negative_intlit(self):
        self.assertTrue(TestLexer.checkLexeme("-1", "-,1,<EOF>", 171))

    def test_negative_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("-12.3e-12", "-,12.3e-12,<EOF>", 172))

    def test_array_literal_with_spaces(self):
        self.assertTrue(TestLexer.checkLexeme("{  1,2,  }", "{,1,,,2,,,},<EOF>", 173))

    # Test stringlit:
    def test_uppercase_inside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ABC"ABC """, """ABC,Error Token A""", 174))

    def test_special_chars_in_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "$#@~" """, """$#@~,<EOF>""", 175))

    def test_special_chars_outside_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "$#@~"$#@~ """, """$#@~,Error Token $""", 176))

    def test_string_inside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""abcAbcabc"" """, """,abcAbcabc,,<EOF>""", 177))

    def test_comment_inside_array_lit(self):
        self.assertTrue(TestLexer.checkLexeme("{ ** This is comment ** }", "{,},<EOF>", 178))

    def test_octal_with_id(self):
        self.assertTrue(TestLexer.checkLexeme("0o12oo", "0o12,oo,<EOF>", 179))

    def test_cmt_token(self):
        self.assertTrue(TestLexer.checkLexeme("123abc * * abc", "123,abc,*,*,abc,<EOF>", 180))

    def test_float_not_eq_op(self):
        self.assertTrue(TestLexer.checkLexeme("abc =/= 123 \. *. +.", "abc,=/=,123,\.,*.,+.,<EOF>", 181))

    def test_cmt_inside_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc **this is comment" """, """abc **this is comment,<EOF>""", 182))

    def test_unclose_str_inside_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcABC""abc """, """abcABC,Unclosed String: abc """, 183))

    def test_wrong_escape_for_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\"ABC" """, """Illegal Escape In String: abc\\\"""", 184))

    def test_single_quote_for__escape_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcABC\\n abc'b" """, """Illegal Escape In String: abcABC\\n abc'b""", 185))

    def test_escape_single_quote_follow_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'"" """, """abc\\',Unclosed String:  """, 186))

    def test_wrong_escape_with_number(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\1aBc%^&" """, """Illegal Escape In String: abc\\1""", 187))

    def test_single_quote_at_the_end_of_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcAbC'" """, """Unclosed String: abcAbC'" """, 188))

    def test_comment_in_new_line(self):
        self.assertTrue(TestLexer.checkLexeme("""
            ** This
            is
            a
            comment
            **
        ""","""<EOF>""", 189))

    def test_unterminated_comment_new_line(self):
        self.assertTrue(TestLexer.checkLexeme("""
        ** This
        is 
        unterminated
        * comment
        """, """Unterminated Comment""", 190))

    def test_illegal_escape_with_backslash_end_of_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcABC\\" """, """Illegal Escape In String: abcABC\\\"""", 191))

    def test_forward_slash(self):
        self.assertTrue(TestLexer.checkLexeme("this is / forward slash", "this,is,Error Token /", 192))

    def test_div_op_and_back_slash(self):
        self.assertTrue(TestLexer.checkLexeme("\ backslash \\", "\,backslash,\,<EOF>", 193))

    def test_four_spaces_in_str(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ABCabc   " """, """ABCabc   ,<EOF>""", 194))

    def test_zero_at_start_of_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("012.012e-03", "012.012e-03,<EOF>", 195))

    def test_zero_in_exponent_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e-000012", "12.0e-000012,<EOF>", 196))

    def test_zero_in_decimal_point_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("1200.0001203", "1200.0001203,<EOF>", 197))

    def test_many_dots_in_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("12.3.1.567.00","12.3,.,1.567,.,0,0,<EOF>", 198))

    def test_exponent_alone(self):
        self.assertTrue(TestLexer.checkLexeme("e-12", "e,-,12,<EOF>", 199))

    def test_zero_in_int_part(self):
        self.assertTrue(TestLexer.checkLexeme("0.12e-3", "0.12e-3,<EOF>", 200))










