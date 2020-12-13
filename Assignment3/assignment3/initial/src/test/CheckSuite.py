import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    """
    **************************************
    Testcases start here!!!
    **************************************  
    """

    def test_redeclared_global_var(self):
        input = """
        Var: a;
        Var: a = 1;
        Function: main
            Body: 
            EndBody.       
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_many_global_var(self):
        input = """
        Var: b = {1, 2, 3};
        Var: a;
        Var: b = 1;
        Function: main
            Body:
            EndBody.        
        """
        expect = str(Redeclared(Variable(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_func(self):
        input = """
        Var: foo = 1.2;
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_param(self):
        input = """
        Function: foo
            Parameter: a, b[10], a
            Body:
            EndBody.

        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_param_is_array_lit(self):
        input = """
        Function: foo
            Parameter: a
            Body:
            EndBody.

        Function: main
            Body:
            EndBody.

        Function: foo2
            Parameter: b[10], b[1]
            Body:
            EndBody.
        """
        expect = str(Redeclared(Parameter(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_var_in_func_body(self):
        input = """
        Function: foo
            Parameter: a
            Body:
                Var: a = 1;
            EndBody.

        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_var_declared_in_func_body(self):
        input = """
        Var: a;
        Function: foo
            Parameter: b
            Body:
                Var: a = 1;
                Var: b = {1, 2, 3};
            EndBody.

        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Variable(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_undeclared_identifier(self):
        input = """
        Function: foo
            Body:
                a = 1;
            EndBody.

        Function: main
            Body:
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_undeclared_function(self):
        input = """
        Function: foo
            Parameter: a
            Body:
                a = foo1();
            EndBody.

        Function: main
            Body:
            EndBody.
        """
        expect = str(Undeclared(Function(), "foo1"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_simple_bin_op(self):
        input = """
        Function: main
            Body:
                Var: a, x = 1.2;
                a = 1 + x;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(1), Id("x"))))
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_simple_unary_op(self):
        input = """
        Function: main
            Body:
                Var: a, x = 1.2;
                a = -x;
            EndBody.
        """ 
        expect = str(TypeMismatchInExpression(UnaryOp("-", Id("x"))))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_simple_func_call(self):
        input = """
        Function: foo
            Parameter: a, b
            Body:
                a = 10;
                b = 20;
            EndBody.

        Function: main
            Body:
                Var: a;
                a = foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_simple_call_stmt(self):
        input = """
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
                foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_simple_if(self):
        input = """
        Function: main
            Body:
                Var: i = 1;
                If i Then i = False; EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id("i"), [], [Assign(Id("i"), BooleanLiteral(False))])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_redeclared_in_if_stmt(self):
        input = """
        Function: main
            Body:
                If True Then 
                    Var: i = 10;
                    Var: i; 
                EndIf.
            EndBody.
        """
        expect = str(Redeclared(Variable(), "i"))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_undeclared_var_in_if_stmt(self):
        input = """
        Function: main
            Body:
                If False Then
                    i = 10;
                EndIf.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "i"))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_simple_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: i;
                For (i = 10.1, i < 10, 2) Do
                    read();
                EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("i"), FloatLiteral(10.1), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id("read"),[])]))))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_simple_type_mismatch_in_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: i = 10;
                For (i = 1, 2, 2) Do EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("i"), IntLiteral(1), IntLiteral(2), IntLiteral(2), ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_index_in_for_stmt(self):
        input = """
        Function: main
            Body:
                For (i = 1, False, i) Do EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "i"))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclared_var_decl_in_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: i = 0;
                For (i = 1, True, 2) Do
                    Var: i = "Hello World!";
                    Var: a = 10;
                    Var: a;
                EndFor.
            EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_simple_dowhile_stmt(self):
        input = """
        Function: main
            Body:
                Var: i = 10;
                Do 
                    i = i + 1;
                While i
                EndDo.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Dowhile(([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]), Id("i"))))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_simple_while_stmt(self):
        input = """
        Function: main
            Body:
                Var: i = 1;
                While i Do
                    i = i + 2;
                EndWhile.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(While(Id("i"), ([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(2)))]))))
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_simple_no_main_func(self):
        input = """
        Var: a = "No Main Function!!!";
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_simple_return_stmt(self):
        input = """
        Function: foo
            Body:
                Return 10;
            EndBody.
        Function: main
            Body:
                foo();
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [])))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_call_func_itself(self):
        input = """
        Function: main
            Body:
                main(main());
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [CallExpr(Id("main"), [])])))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_simple_arr_cell(self):
        input = """
        Var: a[10] = {1, 2, 3};
        Function: main
            Body:
                Var: b = 1;
                b = a[0] + 1;
                c = b;
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_expr_3_in_for_not_int_type(self):
        input = """
        Function: main
            Body:
                Var: a, b = True, c = "Hmm";
                For (a = 1, b, c) Do EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("a"), IntLiteral(1), Id("b"), Id("c"), ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_expr_1_is_expr(self):
        input = """
        Function: main
            Body:
                Var: i;
                Var: j = 12.1;
                For (i = j +. 1.1, i < 10, i+1) Do EndFor.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id("i"), BinaryOp("+.", Id("j"), FloatLiteral(1.1)), BinaryOp("<", Id("i"), IntLiteral(10)), BinaryOp("+", Id("i"), IntLiteral(1)), ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_redeclared_in_while_stmt(self):
        input = """
        Function: main
            Body:
                Var: b;
                While b Do 
                    Var: c = 12.3;
                    Var: c[10] = {1}; 
                EndWhile.
            EndBody.
        """
        expect = str(Redeclared(Variable(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_redeclared_in_dowhile_stmt(self):
        input = """
        Function: main
            Body:
                Var: b;
                Do 
                    Var: c = 12.3;
                    Var: c[10] = {1}; 
                While b
                EndDo.
            EndBody.
        """
        expect = str(Redeclared(Variable(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_else_if_stmt(self):
        input = """
        Function: main
            Body:
                Var: i = {{1, 2, 4}, {1, 2}};
                If True Then
                ElseIf i Then
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(BooleanLiteral(True) , [], []), (Id("i"), [], [])], ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_undeclared_in_elseif_stmt(self):
        input = """
        Var: b[10] = {1, 2};
        Function: foo
            Parameter: a, c
            Body:
            EndBody.
        Function: main
            Body:
                If True Then
                ElseIf False Then foo(b, abc);
                EndIf.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "abc"))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_of_func_call(self):
        input = """
        Function: foo
            Parameter: a
            Body:
            EndBody.
        Function: main
            Body:
                Var: i = 10;
                foo(12);
                i = i + foo(i);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("i"), CallExpr(Id("foo"), [Id("i")]))))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_call_function_before_declar(self):
        input = """
        Function: main
            Body:
                foo();
            EndBody.
        Function: foo
            Body:
            EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_call_global_var_before_declar(self):
        input = """
        ** Var: a; **
        Function: main
            Body:
                foo(a);
            EndBody.
        Function: foo
            Parameter: b
            Body:
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_simple_type_mismatch_array_cell(self):
        input = """
        Function: foo
            Parameter: a, b[10]
            Body:
            EndBody.
        Function: main
            Body:
                Var: a = 1, b[10] = {1};
                foo(a, b[1.2]);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("b"), [FloatLiteral(1.2)])))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_plue_op_between_None_op(self):
        input = """
        Function: main
            Body:
                Var: a, b;
                a = a + b;
            EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_type_mismatch_when_op_type_is_inferred(self):
        input = """
        Function: main
            Body:
                Var: a, b;
                Var: c = 12.3;
                a = a + b;
                c = c +. a;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+.", Id("c"), Id("a"))))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_call_stmt_infer_inside_itself_1(self):
        input = """
        Function: main
            Parameter: x
            Body:
                Var: y = 1;
                x = 1.0;
                main(y);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [Id("y")])))
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_call_stmt_infer_inside_itself_2(self):
        input = """
        Function: main
            Parameter: x
            Body:
                Var: y = 1;
                main(y);
                x = 1.0;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_infer_type_for_func_call(self):
        input = """
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
                Var: a;
                a = a + foo();
                foo();
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [])))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_simple_type_cannot_inferred_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: x, y;
                x = y;
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_lhs_is_void_type_assign_stmt(self):
        input = """
        Function: foo1
            Body:
            EndBody.
        Function: foo2
            Body:
            EndBody.
        Function: main
            Body:
                foo1();
                foo1() = foo2();
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("foo1"), []), CallExpr(Id("foo2"), []))))
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_both_side_different_type_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 1, b = "Hi";
                a = b;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_param_returned_by_binary_op(self):
        input = """
        Function: foo
            Parameter: a, b, c
            Body:
                ** a = 1;
                b = 2;
                c = "Hey"; **
            EndBody.
        Function: foo1
            Parameter: a
            Body:
            EndBody.
        Function: main
            Body:
                Var: a;
                a = foo(1, 2, "Hmm") + foo1(a);
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("a"), BinaryOp("+", CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2), StringLiteral("Hmm")]), CallExpr(Id("foo1"), [Id("a")])))))
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_simple_binary_op_has_type_cannot_inferred(self):
        input = """
        Function: main
            Parameter: a
            Body:
                Var: b = 10;
                b = main(a);
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("b"), CallExpr(Id("main"), [Id("a")]))))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_simple_unary_op_type_cannot_inferred(self):
        input = """
        Function: main
            Body:
                Var: a, x;
                a = -foo1(x);
            EndBody.
        Function: foo1
            Parameter: a
            Body:
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("a"), UnaryOp("-", CallExpr(Id("foo1"), [Id("x")])))))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_type_mismatch_float_bin_op(self):
        input = """
        Function: main
            Parameter: a
            Body:
                Var: b = 12.3, c = 10;
                a = a +. a *. -b;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp("-", Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_same_name_function_var(self):
        input = """
        Function: main
            Body:
                Var: foo = 0;
                foo = foo + foo();
                c = foo;
                EndBody.
        Function: foo
            Body:
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_simple_type_mismatch_logical_op(self):
        input = """
        Function: main
            Body:
                Var: a = True, b, c = 1;
                a = a || a && b && c;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("&&", BinaryOp("&&", BinaryOp("||", Id("a"), Id("a")), Id("b")),Id("c"))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_simple_int_eq_op(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
                Var: b = 20;
                Var: c, res;
                c = 12.45e-12 =/= 12.3;
                res = a <. b;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("<.", Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_call_stmt_as_operand(self):
        input = """
        Function: main
            Body:
                Var: res = False;
                main();
                res = main() != 10;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("!=", CallExpr(Id("main"), []), IntLiteral(10))))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_simple_float_divide_op(self):
        input = """
        Function: main
            Body:
                Var: a;
                Var: b = 10;
                a = 12.0 \. 12.;
                a = a \. b;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("\.", Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_simple_type_cannot_inferred_inside_un_op(self):
        input = """
        Function: main
            Parameter: a
            Body:
                Var: b = 1.1, c = 20.;
                b = -.c +. b *. -.main(a); 
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("b"), BinaryOp("+.", UnaryOp("-.", Id("c")), BinaryOp("*.", Id("b"), UnaryOp("-.", CallExpr(Id("main"), [Id("a")])))))))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_cannot_inferred_call_stmt(self):
        input = """
        Function: main
            Parameter: a
            Body:
                Var: x;
                main(x);
            EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id("main"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_call_expr_before_call_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
                main() = a;
                main();
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [])))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_diff_argument_func_call(self):
        input = """
        Function: main
            Body:
                Var: a = 12.;
                a = main(1, 2, 3);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_diff_argument_call_stmt(self):
        input = """
        Function: main
            Body:
                main(1, 2, 3);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_one_lhs_is_None_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a;
                Var: b = 10;
                a = b;
                a = 12.1;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(12.1))))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_one_rhs_is_None_assign_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
                Var: b;
                a = b;
                b = 12.11111;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),FloatLiteral(12.11111))))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_redeclared_param_inside_func(self):
        input = """
        Function: main
            Parameter: a
            Body:
                Var: b[10] = {1, 2, 3};
                Var: a = 1;
            EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_redeclared_func_with_global_param(self):
        input = """
        Var: main;
        Function: main
            Body:
            EndBody.
        """
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_type_mismatch_in_return_stmt(self):
        input = """
        Function: main
            Body:
                foo();
            EndBody.
        Function: foo
            Body:
                Return 1;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_return_expr_does_not_have_type(self):
        input = """
        Function: main
            Body:
                foo(1);
            EndBody.
        Function: foo
            Parameter: a
            Body:
                Return a;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("a"))))
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_simple_type_not_inferred_in_op(self):
        input = """
        Function: main
            Body:
                Var: a, x;
                a = - foo(x);
            EndBody.
        Function: foo
            Parameter: a
            Body:
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("a"), UnaryOp("-", CallExpr(Id("foo"), [Id("x")])))))
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_redclared_var_in_do_while_stmt(self):
        input = """
        Function: main
            Body:
                Var: b = 1;
                Do
                    Var: i;
                    Var: b[10] = {1, 2};
                    Var: i;
                While True
                EndDo.
            EndBody.
        """
        expect = str(Redeclared(Variable(), "i"))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_undeclared_var_inside_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: i;
                For (i = i + 1, False, i) Do
                    Var: a;
                    i = a + b;
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_undeclared_func_inside_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
                For (a = 2, 1 < 2, 1) Do
                    Var: i;
                    i = foo();
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_type_mismatch_expr_in_nested_if(self):
        input = """
        Function: main
            Body:
                Var: i = True;
                If True Then
                ElseIf False Then
                    i = 1;
                ElseIf i Then
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("i"), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_undeclared_var_nested_if(self):
        input = """
        Function: main
            Body:
            Var: i, a;
            If i Then Var: j = False;
            ElseIf i Then
                If a Then a = b;
                EndIf.
            EndIf.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_simple_type_mismatch_array_type(self):
        input = """
        Function: main
            Body:
                Var: a[1] = {1, 2, 3};
                Var: b[0] = {1};
                a = b;
                foo();
            EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_array_lit_inside_array_lit(self):
        input = """
        Function: main
            Body:
                Var: a[1] = {{1, 2}};
                Var: b[0] = {{4}, {5}};
                Var: a;
            EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_many_return_in_func(self):
        input = """
        Function: main
            Body:
                If True Then Return 1;
                ElseIf False Then Return 0;
                Else Return -1;
                EndIf.
                a = 1;
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_call_func_inside_func(self):
        input = """
        Function: main
            Body:
                main(1);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_call_return_in_do_while_stmt(self):
        input = """
        Function: main
            Body:
                Do
                    Var: i;
                    i = i + 1;
                    main();
                    Return i;
                While True
                EndDo.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("i"))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_call_return_in_while_stmt(self):
        input = """
        Function: main
            Body:
                While 2.3 >. 4.5 Do
                    Return 2.3;
                    main();
                EndWhile.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [])))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_relational_op_for_float_op(self):
        input = """
        Function: main
            Body:
                Var: a;
                a = 1 + (2.3 =/= 3.4);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(1), BinaryOp("=/=", FloatLiteral(2.3), FloatLiteral(3.4)))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_simple_no_entry_point(self):
        input = """
        Var: main;
        Function: foo
            Body:
            EndBody.
        Function: foo1
            Body:
            EndBody.
        Function: foo2
            Body:
            EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input ,expect, 478))

    def test_diff_in_param_func_call(self):
        input = """
        Function: main
            Body:
                Var: a;
                a = main(1, a) + 10;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"), [IntLiteral(1), Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_call_return_in_for_stmt(self):
        input = """
        Function: main
            Body:
                Var: i;
                For (i = 1, i < 10, i +1 ) Do
                    If (i > 5) Then Return i;
                    Else Return i + 1;
                    EndIf.
                EndFor.
                a = i;
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_type_mismatch_in_var(self):
        input = """
        Function: main
            Body:
                Var: a, b[0] = {1, 2};
                a = b[0] + c;
            EndBody.
        """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_simple_type_cannot_inferred_array_cell(self):
        input = """
        Function: foo
            Parameter: a
            Body:
            EndBody.
        Function: main
            Body:
                Var: a = 1;
                a = foo(1)[1];
            EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("a"), ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input, expect, 482))

    
    

    
    

    

    

    


    
    

    