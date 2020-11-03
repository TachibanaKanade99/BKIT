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
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_many_elses_in_if_stmt(self):
        input = """
        Function: main
            Body:
                If True Then i = 2 - 3 == 1; Else i = 2 - 3 == 2 Else i = 2 - 3 == 3;
                EndIf.
            EndBody.
        """
        expect = "Error on line 4 col 65: Else"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_arr_decl(self):
        input = """
        Var: a[2] = {1, {1, 2}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_exp_is_lit(self):
        input = """
        Function: main
            Body:
                While False Do print(i); EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_wrong_scalar_variable_in_for_stmt(self):
        input = """
        Function: main
            Body:    
                For (a[2] = i + 1, i < 2, i + 1) Do j = i; EndFor.
            EndBody.
        """
        expect = "Error on line 4 col 22: ["
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_array_decl_with_many_dimen(self):
        input = """
        Function: main
            Body:
                Var: arr[1][2][3][4][5][6][7][8] = {1, {3, 4, {5, 6, {7, 8,{9, 10}}}}};
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_printLn_function(self):
        input = """
        Function: main
            Body:
                printLn();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_print_function(self):
        input = """
        Function: main
            Body:
                print(arg);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_printStrLn_function(self):
        input = """
        Function: main
            Body:
                printStrLn(arg);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_float_lit_with_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 12.3;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_wrong_float_lit_with_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 012.3;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_int_lit_with_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 12;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_wrong_int_lit_with_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 0012;
            EndBody.
        """
        expect = "Error on line 4 col 26: 0"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_stringlit_in_if_stmt(self):
        input = """
        Function: main
            Body: 
                If {1} Then Return True;
                Else If "Hey this is string \\n\\t" Then Return False; EndIf.
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_many_stringlits_in_if_stmt(self):
        input = """
                Function: main
                    Body: 
                        If {1} Then Return True;
                        Else If "Hey this is string \\n\\t" + "True" Then Return False; EndIf.
                        EndIf.
                    EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_read_function(self):
        input = """
        Function: main
            Body:
                read(printLn());
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_comment_in_stmt(self):
        input = """
        Function: main
            Body:
                Var: a;
                a = ** this is comment **;
            EndBody.
        """
        expect = "Error on line 5 col 41: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_octal_inlit_in_stmt(self):
        input = """
        Function: main
            Body:
                Var: a[2] = {10, {20, 30}};
                b = b *. c \. 0O77;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_precedence_of_logical_op(self):
        input = """
        Function: main
            Body:
                Var: a[2][3] = {2.3, {1.20e-3}};
                a[0][0] = b <= c[2][3] || b >= d[2][3];
            EndBody.
        """
        expect = "Error on line 5 col 44: >="
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_precedence_of_greater_eq_op_in_parenthesis(self):
        input = """
        Function: main
            Body:
                Var: a[2][3] = {2.3, {1.20e-3}};
                a[0][0] = b <= c[2][3] || (b >= d[2][3]);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_predence_of_left_operand_of_logical_op(self):
        input = """
        Function: main
            Body:
                a = (1 < 2) || a <= b;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_prededence_of_plus_mul_div_op(self):
        input = """
        Function: main
            Body:
                a = 2 * 3 \. 3 - 2;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_precedence_of_parenthesis(self):
        input = """
        Function: main
            Body:
                a = (1 == (a <= b || (abc - 45)));
                a = -b + -.c;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_many_if_while_stmt(self):
        input = """
        Function: main
            Body: 
                While False Do
                    If 1 Then 
                        If 2 Then
                        ElseIf 4 Then 
                        ElseIf 6 Then
                        ElseIf 7 Then
                        EndIf.
                    EndIf.
                EndWhile.     
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_str_as_exp_in_for_stmt(self):
        input = """
        Function: main
            Body:
                For (a = "str", "str", "Hiiii") Do EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_octal_in_exp_while_stmt(self):
        input = """
        Function: main
            Body:
                While 0X123ABF || a && c Do Var: a,b,c; Return; EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_greater_op(self):
        input = """
        Function: main
            Body:
                object = 4123542 > 7 > 4;
            EndBody.
        """
        expect = "Error on line 4 col 37: >"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_continue_as_expr(self):
        input = """
        Function: main
            Body:
                Continue = 2;
            EndBody.
        """
        expect = "Error on line 4 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_return_is_operand(self):
        input = """
        Function: main
            Body:
                a = Return + 12 \. 4.5;
            EndBody.
        """
        expect = "Error on line 4 col 20: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_index_exp_in_var_decl(self):
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
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_dimension_is_not_intlit(self):
        input = """
        Function: main
            Body:
                Var: a[i] = 10;
            EndBody.
        """
        expect = "Error on line 4 col 23: i"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_none_association_on_eq(self):
        input = """
        Function: main
            Body:
                a = 1 == 2 == 4;
            EndBody.
        """
        expect = "Error on line 4 col 27: =="
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_none_association_on_float_eq(self):
        input = """
        Function: main
            Body:
                a = 1 =/= 2 == 4;
            EndBody.
        """
        expect = "Error on line 4 col 28: =="
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_array_literal_as_operand(self):
        input = """
        Function: main
            Body:
                foo = {123, 435, 423} * foo;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_empty_aray_literal(self):
        input = """
        Function: main
            Body:
                a = {};
            EndBody.
        """
        expect = "Error on line 4 col 21: }"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_define_parameter_empty(self):
        input = """
        Function: main
            Parameter:
            Body:
            EndBody.
        """
        expect = "Error on line 4 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_if_stmt_no_then(self):
        input = """
        Function: main
            Body: 
                If True EndIf.
            EndBody.
        """
        expect = "Error on line 4 col 24: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_while_stmt_no_do(self):
        input = """
        Function: main
            Body:
                While False || (i == 2) EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_do_while_stmt_no_while(self):
        input = """
        Function: main
            Body:
                Do i = i + 2; EndDo.
            EndBody.
        """
        expect = "Error on line 4 col 30: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_many_cmts_in_assign_stmt(self):
        input = """
        Function: main
            Body:
                inp = ppapa[**4235 dasfj dd 44 ** g(-----------**-----**----------------f())];
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_for_if_stmt_in_func_decl(self):
        input = """ 
        Function: fact
            Parameter: x, a[2]
            Body:
                For (i = 0, i < 10, 2) Do
                    If x Then Break; EndIf.
                EndFor.
                If x Then Break; EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_init_exp_in_for_stmt_not_scalar_var(self):
        input = """
        Function: main
            Body:
                For (i, i, i) Do EndFor.
            EndBody.
        """
        expect = "Error on line 4 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 300))



