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

    # Test function declaration:
    def test_empty_func_decl(self):
        input = """
        Function: foo
            Body: 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_func_decl_with_one_param(self):
        input = """
        Function: foo
            Parameter: n
            Body:
                n = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_func_decl_with_many_params(self):
        input = """
        Function: foo
            Parameter: n, a, b
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_func_decl_with_many_stmts_in_body(self):
        input = """
        Function: foo
            Parameter: a
            Body:
                a = a +. 10.0;
                b = a;
                If (c < a) Then c = a;
                EndIf. 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_func_decl_with_main_func(self):
        input = """
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
                
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_func_decl_with_global_var_decl(self):
        input = """
        Var: x;
        
        Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
                
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_array_var_decl(self):
        input = """Var: a[5] = {1,4,3,2,0};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_multi_dimension_array(self):
        input = """Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_array_in_parameter_of_func_decl(self):
        input = """
        Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_var_decl_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_var_lst_decl_stmt(self):
        input = """
        Function: main
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_assign_stmt(self):
        input = """
        Function: main
            Body: 
                Var: a;
                a = 100 * 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_if_stmt(self):
        input = """
        Function: main
            Body:
                If i < 10 Then i = i + 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_else_if_stmt(self):
        input = """
        Function: main
            Body:
                If i < 10 Then i = i + 1;
                ElseIf i < 20 && (j == i + 1) Then i = i + j \. j;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_many_else_if_stmt(self):
        input = """
        Function: main
            Body:
                If i < 10 Then i = i + 1;
                ElseIf i < 20 && (j == i + 1) Then i = i + j \. j;
                ElseIf i == 10 Then i = i + 3.14 *. r *. r *. r;
                ElseIf j -i == 12 Then i = (i * 10) \. 12.3;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_operator_AND_EQ(self):
        input = """
        Function: main
            Body:
                a = i < 20 && (j == i + 1);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_index_op(self):
        input = """
        Function: main
            Body: 
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_index_op_inside_index_op(self):
        input = """
        Function: main
            Body:
                a[3 + foo(2)][i[1][23 + i] + 10] = 20;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_func_call(self):
        input = """
        Function: foo
            Body:
            EndBody.
            
        Function: main
            Body: 
                a = foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_func_call_with_arguments(self):
        input = """
        Function: foo
            Body:
            EndBody.

        Function: main
            Body: 
                a = foo(a * 10);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_func_call_with_many_arguments(self):
        input = """
        Function: foo
            Body:
            EndBody.

        Function: main
            Body: 
                a = foo(a, a * 10, b[10], 23);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_call_stmt(self):
        input = """
        Function: main
            Body:
                foo(2 * x + 3);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_call_stmt_with_two_exprs_params(self):
        input = """
        Function: foo
            Body:
                foo (2 + x, 4. \.y);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_else_stmt(self):
        input = """
            Function: main
                Body:
                    If i == 0 Then i = i + 1;
                    Else i = i - 1;
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_if_inside_else_stmt(self):
        input = """
        Function: main
            Body: 
                If i == 0 Then i = i + 1;
                Else 
                    If i == j Then i = j + 1;
                    EndIf.
                EndIf.
            EndBody. 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_for_stmt_1(self):
        input = """
        Function: main
            Body:
                For (a = 0, a < 10, a + 1) Do
                    b = a;
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_for_stmt_2(self):
        input = """
        Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_while_stmt(self):
        input = """
        Function: main
            Body:
                While (i < 0) Do i = i - 1; EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_while_stmt_with_empty_stmt_list(self):
        input = """
        Function: main
            Body:
                While i - 2 Do EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_do_while_stmt(self):
        input = """
        Function: main
            Body:
                Do 
                    i = i - 2;
                    If (i == 0) Then i = i + 1; EndIf.
                While j == i EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_break_stmt(self):
        input = """
        Function: main
            Body: 
                Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_break_stmt_in_for_stmt(self):
        input = """
        Function: foo
            Parameter: a, b, a[12]
            Body:
                Var: i, j = 0;
                For (i = j, i < 100, i + 1) Do
                    If i < 90 Then Break;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_continue_stmt(self):
        input = """
        Function: main
            Body: 
                Continue;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_continue_stmt_in_while_stmt(self):
        input = """
        Function: foo
            Parameter: a, b, a[12]
            Body:
                Var: i, j = 0;
                While (i > 10) Do 
                    i = i *. i + 1 \. 12;
                    If i == 0 Then 
                        i = i *. 12.5;
                        Continue;
                    EndIf. 
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_return_stmt(self):
        input = """
        Function: main
            Parameter: a, b, a[10][12][13][14][15]
            Body:
                Var: a = {12, 14, 15};
                m(13) = {12, {12, 14, 15}};
                Return;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_errors_at_while_stmt(self):
        input = """
        Function: main
            Body:
                While True print("Hello World!"); EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_cmt_inside_array_lit(self):
        input = """
        Function: main
            Body:
                Var: a = { ** This is comment ** 1 };
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_empty_program(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_empty_program_with_cmt(self):
        input = """
        ** This is comment **
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_index_op_precedence(self):
        input = """
        Function: main
            Body:
                a = a[i[n + 1] - ae[10] && 100] \. 12.2; 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_type_coersion(self):
        input = """
        Function: main
            Body: 
                If bool_of_string (" True" ) Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_many_variables_stmt(self):
        input = """
        Function: main
            Body:
                Var: a, b = 10, c[20] = {1, {2, 3, {4, 5, {6, 7}}}}, f = 23.4;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_var_stmt_and_assign_stmt(self):
        input = """
        Function: main
            Body:
                a[m + 1][n \. 1][1232132] [j] = c[i[20 \. 1] + 1];
                Var: a = 203;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_break_stmt_in_function_decl(self):
        input = """
        Function: main
            Body:
                Break;Break;Break;Break;Break;Break;Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_continue_stmt_in_function_decl(self):
        input = """
        Function: main
            Body:
                Continue;Continue;Continue;Continue;Continue;Continue;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_return_stmt_with_normal_expression(self):
        input = """
        Function: main
            Body:
                Return 2 + 3;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_return_stmt_with_complex_expression(self):
        input = """
        Function: main
            Body:
                Return 2[i + 1] || 3[i - 1] * (23 \. a + ((a - c) *. 1));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_var_stmt_end_with_no_semi(self):
        input = """
        Function: main
            Body:
                Var: a = 10
            EndBody.
        """
        expect = "Error on line 5 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_global_var_decl_end_no_semi(self):
        input = """
        Var: a = 10
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_global_var_decl_after_func_decl(self):
        input = """
        Function: foo
            Parameter: a, b[1]
            Body:
            
            EndBody.
            
        Var: a = 10;
        """
        expect = "Error on line 8 col 8: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_params_contains_initial_val(self):
        input = """
        Function: foo
            Parameter: a, {1, {1, 2}}
            Body:
            EndBody.
        """
        expect = "Error on line 3 col 26: {"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_func_decl_with_no_body(self):
        input = """
        Function: foo
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_many_func_declar(self):
        input = """
        Function: foo Body: EndBody.
        Function: foo1 Body: EndBody.
        Function: foo2 Body: EndBody.
        Function: foo3 Body: EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_no_boolean_exp_in_if_stmt(self):
        input = """
        Function: main
            Body:
                If i == i + 2 || (i == i - 2) Then Return 1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_many_elses_in_if_stmt(self):
        input = """
        Function: main
            Body:
                If True Then 2 - 3 == 1 Else 2 - 3 == 2 Else 2 - 3 == 3;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))


















