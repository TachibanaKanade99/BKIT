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


























