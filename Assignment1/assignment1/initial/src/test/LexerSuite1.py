import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_0_init(self):
        self.assertTrue(TestLexer.checkLexeme("_id",
                                              "Error Token _", 100))

    def test_1_keywords(self):
        """test legal keywords"""
        self.assertTrue(TestLexer.checkLexeme("BodyBreakContinueDoElseElseIfEndBodyEndIf"
                                              "EndForEndWhileForFunctionIfParameter"
                                              "ReturnThenVarWhileTrueFalseEndDo",
                                              "Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,"
                                              "Function,If,Parameter,Return,Then,Var,"
                                              "While,True,False,EndDo,<EOF>", 101))

    def test_2_identifier(self):
        """test legal id"""
        self.assertTrue(TestLexer.checkLexeme("id id2 id_number_two id_number_2 iD_NuMbEr_TwO",
                                              "id,id2,id_number_two,id_number_2,iD_NuMbEr_TwO,<EOF>", 102))

    def test_3_operator(self):
        """test legal operator"""
        self.assertTrue(TestLexer.checkLexeme("+ +. - -. * *. \\ \\. % ! && || == != <> <= >= =/= <. >. <=. >=.",
                                              "+,+.,-,-.,*,*.,\\,\\.,%,!,&&,||,"
                                              "==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>", 103))

    def test_4_seperator(self):
        """test seperators"""
        self.assertTrue(TestLexer.checkLexeme("()[]{}:.,;", "(,),[,],{,},:,.,,,;,<EOF>", 104))

    def test_5_interger_lit(self):
        """test interger literal"""
        self.assertTrue(TestLexer.checkLexeme("012 12 102 0x1234567890ABCDEF 0X1234567890ABCDEF "
                                              "0o12345670 0O12345670",
                                              "0,12,12,102,0x1234567890ABCDEF,0X1234567890ABCDEF,"
                                              "0o12345670,0O12345670,<EOF>", 105))

    def test_6_interger_lit(self):
        """test auto interger id no space"""
        self.assertTrue(TestLexer.checkLexeme("0120x1234567890ABCDEF",
                                              "0,120,x1234567890ABCDEF,<EOF>", 106))

    def test_7_interger_lit(self):
        """test error in interger"""
        self.assertTrue(TestLexer.checkLexeme("0120X1234567890ABCDEF",
                                              "0,120,Error Token X", 107))

    def test_8_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12. 12.123456890 12e+1234567890 12e1234 12.12e12344",
                                              "12.,12.123456890,12e+1234567890,12e1234,12.12e12344,<EOF>", 108))

    def test_9_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12e12e34",
                                              "12.12e12,e34,<EOF>", 109))

    def test_10_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12.123456890",
                                              "12.12,.,123456890,<EOF>", 110))

    def test_11_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12.12e+3456890",
                                              "12.12,.,12e+3456890,<EOF>", 111))

    def test_12_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12.e+12",
                                              "12.12,.,e,+,12,<EOF>", 112))

    def test_13_bool_lit(self):
        """test bool literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12eTrue",
                                              "12.12,eTrue,<EOF>", 113))

    def test_14_bool_lit(self):
        """test bool literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12e True",
                                              "12.12,e,True,<EOF>", 114))

    def test_15_bool_lit(self):
        """test bool literal"""
        self.assertTrue(TestLexer.checkLexeme("12.12e-12212 0FalseTrue",
                                              "12.12e-12212,0,False,True,<EOF>", 115))

    def test_16_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"This is 1st case wan wan \"",
                                              "This is 1st case wan wan ,<EOF>", 116))

    def test_17_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"This is 2st case quack\\tWhat does the fox say? \"",
                                              "This is 2st case quack\\tWhat does the fox say? ,<EOF>", 117))

    def test_18_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"Test all support escape sequences: "
                                              "\\b \\f \\r \\n \\t \\' \\\\ \"",
                                              "Test all support escape sequences:"
                                              " \\b \\f \\r \\n \\t \\' \\\\ ,<EOF>", 118))

    def test_19_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"Testallsupportescapesequencesnospace:"
                                              "\\b\\f\\r\\n\\t\\'\\\\\"",
                                              "Testallsupportescapesequencesnospace:"
                                              "\\b\\f\\r\\n\\t\\'\\\\,<EOF>", 119))

    def test_20_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"Test double quote: \'\" \'\"",
                                              "Unclosed String: Test double quote: \'\" \'\"", 120))

    def test_21_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"Test double quote: \'\" \\'\"",
                                              "Test double quote: \'\" \\',<EOF>", 121))

    def test_22_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"Test double quote: \'\" \\'\"",
                                              "Unclosed String: Test double quote:\n", 122))

    def test_23_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 123))

    def test_24_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" **This is a test *  """, """Unterminated Comment""", 124))

    def test_25_illegal_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(""" "abc xyz " " abc \\n xyz " """,
                                              """Unclosed String: abc \n""", 125))

    def test_26_double_quote_intring(self):
        self.assertTrue(TestLexer.checkLexeme("\" this is a string: \'\"abc\\nxyz\'\"\"",
                                              " this is a string: \'\"abc\\nxyz\'\",<EOF>", 126))

    def test_27_string_lit(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: **This is a comment** \"",
                                              "This is a string: **This is a comment** ,<EOF>", 127))

    def test_28_string_lit(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: **This is a comment* \"",
                                              "This is a string: **This is a comment* ,<EOF>", 128))

    def test_29_string_lit(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: **This is a comment \"",
                                              "This is a string: **This is a comment ,<EOF>", 129))

    def test_30_string_lit(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: \\t 12e6 **This is a comment** \"",
                                              "This is a string: \\t 12e6 **This is a comment** ,<EOF>", 130))

    def test_31_string_int(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: \\r\"1234",
                                              "This is a string: \\r,1234,<EOF>", 131))

    def test_32_string_int(self):
        self.assertTrue(TestLexer.checkLexeme("\"This is a string: \\r\"12340x1230o123",
                                              "This is a string: \\r,12340,x1230o123,<EOF>", 132))

    def test_33_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 133))

    def test_34_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 134))

    def test_35_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn", "ab,Error Token ?", 135))

    def test_36_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 136))

    def test_37_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 137))

    def test_38_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 138))

    def test_39_string_int_float(self):
        self.assertTrue(TestLexer.checkLexeme("**Hello world**\"This is a string: \\r\"12.0x1230o123",
                                              "This is a string: \\r,12.0,x1230o123,<EOF>", 139))

    def test_40_string_int_float(self):
        self.assertTrue(TestLexer.checkLexeme("**Hello \\t \t \ff world**\"This is a string: \\r\"12.0e120 0o123",
                                              "This is a string: \\r,12.0e120,0o123,<EOF>", 140))

    def test_41_string_int_float(self):
        self.assertTrue(TestLexer.checkLexeme("""**Hello Var Id{} \\t \t \ff world
                                              **\"This is a string: \'\"He told me\\'\"\\r\"123 123e120X123""",
                                              """This is a string: \'\"He told me\\',\\,r,Unclosed String: 123 123e120X123""", 141))

    def test_42_string(self):
        self.assertTrue(TestLexer.checkLexeme("""** Helo To Duy Hung
        hihihaha ** \"This is an illegal string: \'\"leu leu \' \"""",
        "Illegal Escape In String: This is an illegal string: \'\"leu leu \' ",142))

    def test_43_string_int_float(self):  # \\ la token DIV
        self.assertTrue(TestLexer.checkLexeme("""123 123e120o123**Hello Var Id{} \\t \t \ff world"
                                              "**\"This is a string: \'\"He told me\\'\"\\r""",
                                              "123,123e120,o123,This is a string: \'\"He told me\\',\\,r,<EOF>", 143))

    def test_44_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Var: a=5, arr[1][2]={{12e-6,12},{2,3}}",
                                              "Var,:,a,=,5,,,arr,[,1,],[,2,],=,"
                                              "{,{,12e-6,,,12,},,,{,2,,,3,},},<EOF>", 144))

    def test_45_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Var: a=5, arr[1][2]={{\"str\\t\",\"\'\"\"},"
                                              "{\"\\\\\",**comment**4}} 12..2",
                                              "Var,:,a,=,5,,,arr,[,1,],[,2,],=,"
                                              "{,{,str\\t,,,\'\",},,,{,\\\\,,,4,},},12.,.,2,<EOF>", 145))

    def test_46_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("For (i=0,i<10,2) Do \n \t s=s+1;\n EndFor.",
                                              "For,(,i,=,0,,,i,<,10,,,2,),Do,s,=,s,+,1,;,EndFor,.,<EOF>", 146))

    def test_47_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("If (i_am_hand_some == True) Then \n killme();"
                                              "\n ElseIf (i_am_hand_some != notSo) Then \n makeUp();"
                                              "\n Else eatMore();"
                                              "\n EndIf.",
                                              "If,(,i_am_hand_some,==,True,),Then,killme,(,),;,"
                                              "ElseIf,(,i_am_hand_some,!=,notSo,),Then,makeUp,(,),;,"
                                              "Else,eatMore,(,),;,EndIf,.,<EOF>", 147))

    def test_48_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("If (i_am_hand_some == True) Then \n killme();"
                                              "\n ElseIf (i_am_hand_some != NotSo) Then \n makeUp();"
                                              "\n Else eatMore();"
                                              "\n EndIf.",
                                              "If,(,i_am_hand_some,==,True,),Then,killme,(,),;,"
                                              "ElseIf,(,i_am_hand_some,!=,Error Token N", 148))

    def test_49_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("While (weight >=.70.5e0) Do \n\texercise();\n\tdiet();\nEndWhile.",
                                              "While,(,weight,>=.,70.5e0,),Do,"
                                              "exercise,(,),;,diet,(,),;,EndWhile,.,<EOF>", 149))

    def test_50_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Do \n\texercise();\n\tdiet();\nWhile (!handsome)\nEndDo.",
                                              "Do,exercise,(,),;,diet,(,),;,While,(,!,handsome,),EndDo,.,<EOF>",
                                              150))

    def test_51_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Break.", "Break,.,<EOF>", 151))

    def test_52_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Continue.", "Continue,.,<EOF>", 152))

    def test_53_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("fact(2+x ,4.\\.y);", "fact,(,2,+,x,,,4.,\\.,y,),;,<EOF>", 153))

    def test_54_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Return fact(2+x ,4.\\.y);",
                                              "Return,fact,(,2,+,x,,,4.,\\.,y,),;,<EOF>", 154))

    def test_55_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("\"str1!,str2 \" {\"abc\"} 123\"abc",
                                              "str1!,str2 ,{,abc,},123,Unclosed String: abc", 155))

    def test_56_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("\"AnnaToYukiNoOu\\uOlaf\"",
                                              "Illegal Escape In String: AnnaToYukiNoOu\\u", 156))

    def test_57_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(" func(2)[4][5][6]+5+(6-9)>-5||!t+5",
                                              "func,(,2,),[,4,],[,5,],[,6,],+,5,+,"
                                              "(,6,-,9,),>,-,5,||,!,t,+,5,<EOF>", 157))

    def test_58_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("!-func(12)[a+4]*(4+7)\\(2-3)%(4-9)&&(5-9)||(6-7)>=.(9<=.9)=/=2e1",
                                              "!,-,func,(,12,),[,a,+,4,],*,(,4,+,7,),\\,(,2,-,3,),"
                                              "%,(,4,-,9,),&&,(,5,-,9,),||,"
                                              "(,6,-,7,),>=.,(,9,<=.,9,),=/=,2e1,<EOF>", 158))

    def test_59_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Function: main"
                                              "Body: \nVar: a[1][2];\n "
                                              "a[1][2] = a > 4+!a;\n a[1]=!!a>4;\n z=  a*b+c;\n res = 2 * ( a + b );\n "
                                              "EndBody.",
                                              "Function,:,mainBody,:,Var,:,a,[,1,],[,2,],;,"
                                              "a,[,1,],[,2,],=,a,>,4,+,!,a,;,a,[,1,],=,!,!,a,>,4,;"
                                              ",z,=,a,*,b,+,c,;,res,=,2,*,(,a,+,b,),;,EndBody,.,<EOF>", 159))

    def test_60_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Var: b[2][3] = {{2,3,4},{4,5,6}}",
                                              "Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},<EOF>", 160))

    def test_61_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("Var: b[2][3] = {{2,3,4},{4,5,6}}",
                                              "Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},<EOF>", 161))

    def test_62_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is the first string!\\n" "This is the \'\"2^!@#$%^&*\'\"" """,
                                              "This is the first string!\\n,This is the \'\"2^!@#$%^&*\'\",<EOF>", 162))

    def test_63_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is the first string!\\n" "This is the \'\"2^!@#$%^&*\'\""
                                              "Hell yeah! """,
                                              "This is the first string!\\n,This is the \'\"2^!@#$%^&*\'\","
                                              "Unclosed String: Hell yeah! ", 163))

    def test_64_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Kira Kira a la mode!\\n" "Franciso \'\"!@#$%^&*\'\""
                                              "Wut!\t" """,
                                              "Kira Kira a la mode!\\n,Franciso \'\"!@#$%^&*\'\","
                                              "Wut!\t,<EOF>", 164))

    def test_65_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "OoinarU\\t kibou\\r no chikara, Kyua Doriimu!\\n"
                                              "CocoNuts And then Every\\b One go Nuts\'\"" """,
                                              "OoinarU\\t kibou\\r no chikara, Kyua Doriimu!\\n,"
                                              "CocoNuts And then Every\\b One go Nuts\'\",<EOF>", 165))

    def test_66_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "OoinarU\\t kibou\\z no chikara, Kyua Doriimu!\\n"
                                              "CocoNuts And then Every\\n One go Nuts\'\"" """,
                                              "Illegal Escape In String: OoinarU\\t kibou\\z", 166))

    def test_67_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Significant understanding is nothing at all?\\f"
                                              "The body of mind ever stuns the onlooker." Those was func_call """,
                                              "Significant understanding is nothing at all?\\f,"
                                              "The body of mind ever stuns the onlooker.,Error Token T", 167))

    def test_68_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(""" "U9ExX2MmDm" 1231412123operands roger roger >><!rr "LCK\\ " """,
                                              "U9ExX2MmDm,1231412123,operands,roger,roger,>,>,"
                                              "<,!,rr,Illegal Escape In String: LCK\\ ", 168))

    def test_69_string_int_float_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("""<html class="client-nojs" lang="en" dir="ltr" <head>
                                              <meta charset="UTF-8"/> <title>Asphalt Wiki | Fandom</title> <script>""",
                                              "<,html,class,=,client-nojs,lang,=,en,dir,=,ltr,<,head,>,"
                                              "<,meta,charset,=,UTF-8,Error Token /", 169))

    def test_70_index_keywords(self):
        self.assertTrue(TestLexer.checkLexeme("a[3 + foo(2)] = a[b[2][3]] + 4",
                                              "a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,<EOF>", 170))

    def test_71_statement(self):
        self.assertTrue(TestLexer.checkLexeme(" Var: r = 10., v; v = (4. \. 3.) *. 3.14 *. r *. r *. r; ",
                                              "Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>",
                                              171))

    def test_72_call(self):
        self.assertTrue(TestLexer.checkLexeme(" duy(18 + x, 10. \. 198); hung(); ",
                                              "duy,(,18,+,x,,,10.,\.,198,),;,hung,(,),;,<EOF>",
                                              172))

    def test_73_string_lit(self):
        """ "Test double quote: \n '" \'" -> lack of " at the end """
        self.assertTrue(TestLexer.checkLexeme("\"Test double quote:\\n \'\" \\'\"",
                                              "Test double quote:\\n \'\" \\',<EOF>", 173))

    def test_74_string_lit(self):
        """illegal escape because of ' in string"""
        self.assertTrue(TestLexer.checkLexeme("\"Test double quote:\\n \'\\\" \\'\"",
                                              "Illegal Escape In String: Test double quote:\\n \'\\", 174))

    def test_75_identifier(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("aDH_198_bcdef", "aDH_198_bcdef,<EOF>", 175))

    def test_76_upper_letter(self):
        """fail because Upper letter first"""
        self.assertTrue(TestLexer.checkLexeme("ADH_198_bcdef", "Error Token A", 176))

    def test_77_underscore_first(self):
        """fail because Underscore first"""
        self.assertTrue(TestLexer.checkLexeme("_aDH_198_bcdef", "Error Token _", 177))

    def test_78_number_first(self):
        """fail because Number first"""
        self.assertTrue(TestLexer.checkLexeme("1aDH_198_bcdef", "1,aDH_198_bcdef,<EOF>", 178))

    def test_79_keyword(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("EndBody", "EndBody,<EOF>", 179))

    def test_80_keyword(self):
        """first token is not keyword and begin with upper letter"""
        self.assertTrue(TestLexer.checkLexeme("End While", "Error Token E", 180))

    def test_81_integer_lit(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810198", "1810198,<EOF>", 181))

    def test_82_integer_lit(self):
        """2 intlit"""
        self.assertTrue(TestLexer.checkLexeme("01810198", "0,1810198,<EOF>", 182))

    def test_83_hex(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("0x123ABCD", "0x123ABCD,<EOF>", 183))

    def test_84_hex(self):
        """fail because no X in hex number"""
        self.assertTrue(TestLexer.checkLexeme("0x123ABCX", "0x123ABC,Error Token X", 184))

    def test_85_oc(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("0O1234567", "0O1234567,<EOF>", 185))

    def test_86_oc(self):
        """fail because not int, hex or octal"""
        self.assertTrue(TestLexer.checkLexeme("0H1810198", "0,Error Token H", 186))

    def test_87_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810.198", "1810.198,<EOF>", 187))

    def test_88_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810.198E5", "1810.198E5,<EOF>", 188))

    def test_89_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810E198", "1810E198,<EOF>", 189))

    def test_90_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810.E198", "1810.E198,<EOF>", 190))

    def test_91_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("1810198.", "1810198.,<EOF>", 191))

    def test_92_float(self):
        """success"""
        self.assertTrue(TestLexer.checkLexeme("181019e-8", "181019e-8,<EOF>", 192))

    def test_93_float(self):
        """3 token"""
        self.assertTrue(TestLexer.checkLexeme("18101e9.8", "18101e9,.,8,<EOF>", 193))

    def test_94_float(self):
        """sign is another token"""
        self.assertTrue(TestLexer.checkLexeme("-18.10e-198", "-,18.10e-198,<EOF>", 194))

    def test_95_comment(self):
        """comment 1 line"""
        self.assertTrue(TestLexer.checkLexeme(" ** To Duy Hung 1810 ** 198 ", "198,<EOF>", 195))

    def test_96_comment(self):
        """multi-line comment"""
        self.assertTrue(TestLexer.checkLexeme(" ** To abcd 18 \n * Duy efgh 10 \n ** 198 ", "198,<EOF>", 196))

    def test_97_comment(self):
        """unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme(" ** To abcd 18 \n * Duy efgh 10 \n * 198 ", "Unterminated Comment", 197))

    def test_98_array(self):
        self.assertTrue(TestLexer.checkLexeme(" {1,1.5,True,\"abc\",{1,1.5,True,\"abc\"}} ",
                                              "{,1,,,1.5,,,True,,,abc,,,{,1,,,1.5,,,True,,,abc,},},<EOF>", 198))

    def test_99_esc_str(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(" \"abc\\axyz\" ", "Illegal Escape In String: abc\\a", 199))

    def test_100_esc_str(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme("\"hello lexer \\t \"     asdf", "hello lexer \\t ,asdf,<EOF>", 0))

    def test_101_esc_str(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme("\"Backspace  \\b\"", "Backspace  \\b,<EOF>", 1))

    def test_102_esc_str(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme("\"Formfeed   \\f\"", "Formfeed   \\f,<EOF>", 2))

    def test_103_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Return     \\r\"", "Return     \\r,<EOF>", 3))

    def test_104_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Newline    \\n\"", "Newline    \\n,<EOF>", 4))

    def test_105_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Newline    \\n\"", "Newline    \\n,<EOF>", 5))

    def test_106_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Single Quote    \\' \"", "Single Quote    \\' ,<EOF>", 6))

    def test_107_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Single Quote    \\' \"", "Single Quote    \\' ,<EOF>", 7))

    def test_108_esc_str(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme("\"Single Quote    \' \"",
                                              "Illegal Escape In String: Single Quote    \' ", 8))

    def test_109_string(self):
        self.assertTrue(TestLexer.checkLexeme(" \"abc**f**\"", "abc**f**,<EOF>", 9))

    def test_110_string(self):
        self.assertTrue(TestLexer.checkLexeme(" \"Neu nhu ngay ay \\n\" ", "Neu nhu ngay ay \\n,<EOF>", 10))

    def test_111_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"He asked me:\\n  \'\"Where is John\'\"\"",
                                              "He asked me:\\n  '\"Where is John'\",<EOF>", 11))

    def test_112_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"\\\\n\"", "\\\\n,<EOF>", 12))

    def test_113_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"\\\\n\"", "Unclosed String: \\\\\n", 13))  # => Unclosed Sring

    def test_114_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"Var int a \\n = 8\"", "Var int a \\n = 8,<EOF>", 14))

    def test_115_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc\\\\n def\"", "abc\\\\n def,<EOF>", 15))

    def test_116_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc \\r def\"", "abc \\r def,<EOF>", 16))

    def test_117_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"Toi laTA\"", "Unclosed String: Toi la", 17))

    def test_118_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"hihihaha \a \"", "hihihaha \a ,<EOF>", 18))

    def test_119_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"alo alo 1234 \'\"\"", "alo alo 1234 \'\",<EOF>", 19))

    def test_120_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"alo ola \'\" 1234 \'\"\" \"ua ua \'\\a \"",
                                              "alo ola \'\" 1234 \'\",Illegal Escape In String: ua ua \'\\", 20))

    def test_121_string(self):
        self.assertTrue(TestLexer.checkLexeme("\" abc \'a \"", "Illegal Escape In String:  abc \'a", 21))

    def test_122_string(self):
        """test string literal"""
        self.assertTrue(
            TestLexer.checkLexeme(""" "hello my fen \\h"  """, "Illegal Escape In String: hello my fen \\h", 22))

    def test_123_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen '" hi"  """, """hello my fen '" hi,<EOF>""", 23))

    def test_124_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen \\' hi"  """, """hello my fen \\' hi,<EOF>""", 24))

    def test_125_string(self):
        """test string literal"""
        self.assertTrue(
            TestLexer.checkLexeme(""" "hello my fen ' hi"  """, """Illegal Escape In String: hello my fen ' """, 25))

    def test_126_string(self):
        """test string literal"""
        self.assertTrue(
            TestLexer.checkLexeme(""" "hello my fen \\h hi"  """, """Illegal Escape In String: hello my fen \\h""", 26))

    def test_127_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen"  """, """hello my fen,<EOF>""", 27))

    def test_128_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen \\\\c"  """, """hello my fen \\\\c,<EOF>""", 28))

    def test_129_string(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen""  """, """hello my fen,Unclosed String:   """, 29))

    def test_130_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(" **hello my fen** ", "<EOF>", 30))

    def test_131_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(" **hello my fen\n*hi you** ", "<EOF>", 31))

    def test_132_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(" ***hello my fen*** ", "*,<EOF>", 32))

    def test_133_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(" **hello my fen ", "Unterminated Comment", 33))

    def test_134_keywords(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("BodyElseEndForIfVarEndDo", "Body,Else,EndFor,If,Var,EndDo,<EOF>", 34))

    def test_135_keywords(self):
        """test keywords"""
        self.assertTrue(
            TestLexer.checkLexeme("BreakElseIfEndWhileParameterWhile", "Break,ElseIf,EndWhile,Parameter,While,<EOF>",
                                  35))

    def test_136_keywords(self):
        """test keywords"""
        self.assertTrue(
            TestLexer.checkLexeme("ContinueEndBodyForReturnTrue", "Continue,EndBody,For,Return,True,<EOF>", 36))

    def test_137_keywords(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("DoEndIfFunctionThenFalse", "Do,EndIf,Function,Then,False,<EOF>", 37))

    def test_138_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("+*%==<=>.", "+,*,%,==,<=,>.,<EOF>", 38))

    def test_139_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("+.*.!!=>=<=.", "+.,*.,!,!=,>=,<=.,<EOF>", 39))

    def test_140_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("- \ && < =/= >=.", "-,\,&&,<,=/=,>=.,<EOF>", 40))

    def test_141_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("-.\\.||><.", "-.,\\.,||,>,<.,<EOF>", 41))

    def test_142_id(self):
        """test id"""
        self.assertTrue(TestLexer.checkLexeme("x[1][2] = 3", "x,[,1,],[,2,],=,3,<EOF>", 42))

    def test_143_id(self):
        """test id"""
        self.assertTrue(TestLexer.checkLexeme("x[1][2] = {2, 3}", "x,[,1,],[,2,],=,{,2,,,3,},<EOF>", 43))

    def test_id_3(self):
        """test id"""
        self.assertTrue(TestLexer.checkLexeme("x = -3", "x,=,-,3,<EOF>", 44))

    def test_id_4(self):
        """test id"""
        self.assertTrue(TestLexer.checkLexeme("x = -.3.5 +. 12e4", "x,=,-.,3.5,+.,12e4,<EOF>", 45))

    def test_mix_1(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(r"""
        Function: foo
            Body:
                x = 10;
                ok();
            EndBody.
        """, "Function,:,foo,Body,:,x,=,10,;,ok,(,),;,EndBody,.,<EOF>", 46))

    def test_mix_2(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(r"""
        value = "string nay la value;
        value2 = "string string string";
        """, "value,=,Unclosed String: string nay la value;\n", 47))

    def test_mix_3(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(r"""
        For (i = 1, i < 5, 2) Do
            writeln(i);
        EndFor.
        """, "For,(,i,=,1,,,i,<,5,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>", 48))

    def test_mix_4(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(r"""
        x = x+y-z*y\f-t1 && 123123;
        """, r"x,=,x,+,y,-,z,*,y,\,f,-,t1,&&,123123,;,<EOF>", 49))

    def test_mix_5(self):
        """test mix"""
        self.assertTrue(TestLexer.checkLexeme(r"""
        b[1+2] + int(3) + float_to_int(5.1) - 2 * 3 - 5 + 4 + f[a || b] % 2
        """, r"b,[,1,+,2,],+,int,(,3,),+,float_to_int,(,5.1,),-,2,*,3,-,5,+,4,+,f,[,a,||,b,],%,2,<EOF>", 50))

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 51))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 52))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn", "ab,Error Token ?", 53))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 54))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 55))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 56))

    def test_int_lit_1(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("1234 00", "1234,0,0,<EOF>", 57))

    def test_int_lit_2(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("0199 0xFF 0XABC 0o567 0O77", "0,199,0xFF,0XABC,0o567,0O77,<EOF>", 58))

    def test_int_lit_3(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("0x0987", "0,x0987,<EOF>", 59))

    def test_int_lit_4(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("0xEFGH", "0xEF,Error Token G", 60))

    def test_int_lit_5(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("0o768", "0o76,8,<EOF>", 61))

    def test_float_lit_1(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5", "12.0e3,12e3,12.e5,<EOF>", 62))

    def test_float_lit_2(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12000. 120000e-1", "12.0e3,12000.,120000e-1,<EOF>", 63))

        ########????????

    def test_float_lit_3(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("000.000", "0,0,0.000,<EOF>", 64))

    def test_float_lit_4(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12E0", "12E0,<EOF>", 65))

    def test_boolean_lit_1(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = True", "Var,x,=,True,<EOF>", 66))

    def test_boolean_lit_2(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = False", "Var,x,=,False,<EOF>", 67))

    def test_boolean_lit_3(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = true", "Var,x,=,true,<EOF>", 68))

    def test_boolean_lit_4(self):
        "test boolean literal"
        self.assertTrue(TestLexer.checkLexeme("Var x = TRUE", "Var,x,=,Error Token T", 69))

    def test_string_lit_1(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen"  """, "hello my fen,<EOF>", 70))

    def test_string_lit_2(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "hello my fen \\t \\n"  """, "hello my fen \\t \\n,<EOF>", 71))

    def test_172_hex(self):
        self.assertTrue(TestLexer.checkLexeme("0X012ABCD", "0,Error Token X", 72))

    def test_173_string(self):
        self.assertTrue(TestLexer.checkLexeme("\" toduyhung \' \"", "Illegal Escape In String:  toduyhung \' ", 73))

    def test_174_string(self):
        self.assertTrue(TestLexer.checkLexeme("\" toduyhung \'\"", "Unclosed String:  toduyhung \'\"", 74))
