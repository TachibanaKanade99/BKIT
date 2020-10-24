import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_no_declare(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_var_declare(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))
    
    def test_var_declare_nothing(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_var_declare_no_semi(self):
        input = """Var: x"""
        expect = "Error on line 1 col 6: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_var_declare_long_id(self):
        input = """Var: a55t9_jw8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_var_declare_many(self):
        input = """Var: as, gb2, y8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var_declare_id_index_no_index(self):
        input = """Var: a[];"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_var_declare_id_index(self):
        input = """Var: x[7];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_declare_index_many_id_index(self):
        input = """Var: th[12], uk[14], s2y[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 209))

    def test_var_declare_many_index_id(self):
        input = """Var: bh[6][5][26];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 210))

    def test_var_declare_many_index_many_id_index(self):
        input = """Var: bh[6][5][26], by[8][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 211))

    def test_var_declare_mix(self):
        input = """Var: ar, p, yt4[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_var_declare_wrong_id_index(self):
        input = """Var: cs[6][5][];"""
        expect = "Error on line 1 col 14: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_var_declare_number(self):
        input = """Var: 5;"""
        expect = "Error on line 1 col 5: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_var_declare_assign_integer(self):
        input = """Var: a=5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_var_declare_assign_string(self):
        input = """Var: a="ca";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_var_declare_assign_boolean(self):
        input = """Var: a=true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_var_declare_assign_float(self):
        input = """Var: a=5.6;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_var_declare_assign_float_e(self):
        input = """Var: a=e17;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_var_declare_assign_int_op_exp(self):
        input = """Var: a5 = 1 -. 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_var_declare_assign_bool_op_exp(self):
        input = """Var: a = y > x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_var_declare_assign_float_op_exp(self):
        input = """Var: a = y *. x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_var_declare_assign_and_or_exp(self):
        input = """Var: a = ty || re;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_var_declare_assign_not_exp(self):
        input = """Var: a = !aa;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_var_declare_assign_unary_exp(self):
        input = """Var: a = -hu;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_var_declare_assign_funcall(self):
        input = """Var: a = foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_var_declare_assign_array(self):
        input = """Var: a={5, 6, 9};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_var_declare_assign_array_in_array(self):
        input = """Var: a={{5, 6, 9},{6.5, 9.8, 2e1}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_var_declare_assign_many_id(self):
        input = """Var: a,b,c=5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_var_declare_assign_many_initvalue(self):
        input = """Var: a=5, 6, 8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_var_declare_assign_mix_initvalue(self):
        input = """Var: ad="yy", 6.5, 8e1, 7;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_var_declare_many_assigns(self):
        input = """Var: a, b, d2= gh, yu(), 8.9;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_var_declare_underline(self):
        input = """Var: _a5;"""
        expect = "_"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_var_declare_special_token(self):
        input = """Var: @ = 5;"""
        expect = "@"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_var_declare_backslash(self):
        input = """Var: \a;"""
        expect = "\a"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_type_coercion(self):
        input = """Var: a = int_of_float(as);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_simple_func_declare(self):
        input = """Function: foo
                Body:
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_func_declare_no_body(self):
        input = """Function: foo"""
        expect = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_func_declare_no_endBody(self):
        input = """Function: foo
                Parameter:
                Body: """
        expect = "Error on line 3 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_func_declare_no_dot(self):
        input = """Function: foo
                Parameter:
                Body:
                EndBody"""
        expect = "Error on line 3 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_var_declare_and_func_declare(self):
        input = """ Var : abc;
                Function: foo
                Body:
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_func_declare_single_parameter(self):
        input = """Function: foo
                Parameter: a
                Body:
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_func_declare_many_parameters(self):
        input = """Function: foo
                Parameter: a, b, c
                Body:
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_func_declare_no_parameter(self):
        input = """Function: foo
                Parameter:
                Body:
                EndBody."""
        expect = "Error on line 3 col 16: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_func_declare_return_nothing(self):
        input = """Function: foo
                Body:
                Return ;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_func_declare_return_integer(self):
        input = """Function: foo
                Body:
                Return 5;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_func_declare_return_float(self):
        input = """Function: foo
                Body:
                Return 589.248e54;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_func_declare_return_bool(self):
        input = """Function: foo
                Body:
                Return false;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_func_declare_return_string(self):
        input = """Function: foo
                Body:
                Return "das";
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_func_declare_return_id(self):
        input = """Function: foo
                Body:
                Return hy58_ut;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_func_declare_return_exp(self):
        input = """Function: foo
                Body:
                Return 5+8>6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_func_declare_return_funcall(self):
        input = """Function: foo
                Body:
                Return ghi();
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_func_declare_return_many(self):
        input = """Function: foo
                Body:
                Return hu, 5;
                EndBody."""
        expect = "Error on line 3 col 25: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_func_declare_return_special_token(self):
        input = """Function: foo
                Body:
                Return 5 + $;
                EndBody."""
        expect = "$"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_func_declare_many_returns(self):
        input = """Function: foo
                Body:
                Return 28;
                Return 15;
                EndBody."""
        expect = "Error on line 4 col 16: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_func_declare_return_wrong(self):
        input = """Return bg5;
                Function: foo
                Body:
                EndBody."""
        expect = "Error on line 1 col 0: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_func_declare_simple_assign_stmt(self):
        input = """Function: foo
                Body:
                a = b;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_func_declare_assign_stmt_exp(self):
        input = """Function: foo
                Body:
                a = b > 5.6;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_func_declare_assign_stmt_exp_wrong(self):
        input = """Function: foo
                Body:
                a = b > 5.6 < 6.5;
                EndBody."""
        expect = "Error on line 3 col 28: <"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_func_declare_assign_stmt_exp1(self):
        input = """Function: foo
                Body:
                a = b || c;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_func_declare_assign_stmt_many_exp1(self):
        input = """Function: foo
                Body:
                a = b || c && ft5;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_func_declare_assign_stmt_exp2(self):
        input = """Function: foo
                Body:
                a = b + c;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_func_declare_assign_stmt_many_exp2(self):
        input = """Function: foo
                Body:
                a = b + c - 16 +. 6.5 -. gt;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_func_declare_assign_stmt_exp3(self):
        input = """Function: foo
                Body:
                a = b *. gt;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_func_declare_assign_stmt_many_exp3(self):
        input = """Function: foo
                Body:
                a = b *. gt \ 56 % 9;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_func_declare_assign_stmt_exp4(self):
        input = """Function: foo
                Body:
                a = !69;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_func_declare_assign_stmt_wrong_exp4(self):
        input = """Function: foo
                Body:
                a = jkl!;
                EndBody."""
        expect = "Error on line 3 col 23: !"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_func_declare_assign_stmt_exp5(self):
        input = """Function: foo
                Body:
                a = -.5.9;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_func_declare_assign_stmt_wrong_exp5(self):
        input = """Function: foo
                Body:
                a = --9.8;
                EndBody."""
        expect = "Error on line 3 col 21: -"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_func_declare_assign_stmt_exp6(self):
        input = """Function: foo
                Body:
                a = 5 + [a * ui];
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_func_declare_assign_stmt_exp7(self):
        input = """Function: foo
                Body:
                a = 56 + gui();
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_func_declare_assign_stmt_exp8(self):
        input = """Function: foo
                Body:
                a = hy + (9 + 8.2 *. re4);
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_func_declare_simple_if_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If a == 5 Then b = 8; 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_func_declare_if_stmt_no_then(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 7 > 5 + 9 
                EndIf.
                EndBody."""
        expect = "Error on line 5 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_func_declare_if_stmt_no_bool_exp(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If  Then fg = ku(); 
                EndIf.
                EndBody."""
        expect = "Error on line 4 col 20: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_func_declare_if_stmt_no_stmt_in_then(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If fg <. a6 Then 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_func_declare_if_stmt_elseif(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 4 + 5 Then abc = 6; 
                    ElseIf 8 > 5 Then a = b; 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_func_declare_if_stmt_no_bool_exp_in_elseif(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 4 + 5 Then abc = 6; 
                    ElseIf Then a = b; 
                EndIf.
                EndBody."""
        expect = "Error on line 5 col 27: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_func_declare_if_stmt_else(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 4 + 5 Then abc = 6; 
                    Else a = bk; 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_func_declare_if_stmt_no_stmt_else(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 4 + 5 Then abc = yu[6][9]; 
                    Else 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_func_declare_if_stmt_full_component(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If 4 + 5 Then abc = 6; 
                    ElseIf yu >. 6 + 7 \. 9 Then hy[5] = a5v(); 
                        Else pn = a(); u = k -. (9 || r); 
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_func_declare_for_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=5, i > 69 + 3, 2 + 1) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_func_declare_for_stmt_wrong_initExpr(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i > 98, i > 69 + 3, 2 + 1) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 23: >"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_func_declare_for_stmt_wrong_conditionExpr(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=0, fr = 9 , 8) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 29: ="
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_func_declare_for_stmt_wrong_updateExpr(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=5, i > 69 + 3, b = 8) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 40: ="
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_func_declare_for_stmt_no_first_condition(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i > 69 + 3, 2 + 1) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 23: >"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_func_declare_for_stmt_no_second_condition(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=0, 8) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 27: )"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_func_declare_for_stmt_no_third_condition(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=5, i > 69 + 3) Do
                    c = 5 + i;
                EndFor.
                EndBody."""
        expect = "Error on line 4 col 36: )"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_func_declare_for_stmt_do_no_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=5, i > 69 + 3, 8) Do
                EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_func_declare_for_stmt_do_many_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                For (i=5, i > 69 + 3, 8) Do
                    If 5 > 2 Then h = k; EndIf.
                    k = 5 + 6;
                EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_func_declare_while_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                While true Do 
                a = b; 
                EndWhile.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_func_declare_while_stmt_no_conditionExpr(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                While Do 
                a = b; 
                EndWhile.
                EndBody."""
        expect = "Error on line 4 col 22: Do"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_func_declare_while_stmt_no_body(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                While true Do 
                a = b; 
                EndWhile.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_func_declare_do_while_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Do g = k - 2; a = b();
                While hy == 56.e1
                EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_func_declare_do_while_stmt_no_conditionExpr(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Do g = k - 2;
                While
                EndDo.
                EndBody."""
        expect = "Error on line 6 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_func_declare_do_while_stmt_no_body(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Do
                While hy == 56.e1
                EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_func_declare_break_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Do Break; g = h;
                While hy == 56.e1
                EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_func_declare_continue_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Do
                    For (i = 7, i > 69 + 3, 2 + 1) Do
                        c = 5 + i;
                    EndFor. 
                    Continue; 
                While hy == 56.e1
                EndDo.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_func_declare_wrong_break_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                Break;
                Do
                    For (i = 7, i > 69 + 3, 2 + 1) Do
                        c = 5 + i;
                    EndFor. 
                While hy == 56.e1
                EndDo.
                EndBody."""
        expect = "Error on line 4 col 16: Break"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_func_declare_wrong_continue_stmt(self):
        input = """Function: foo
                Parameter: d, ki8
                Body:
                If fg <. a6 Then Continue;
                EndIf.
                EndBody."""
        expect = "Error on line 4 col 33: Continue"
        self.assertTrue(TestParser.checkParser(input, expect, 300))