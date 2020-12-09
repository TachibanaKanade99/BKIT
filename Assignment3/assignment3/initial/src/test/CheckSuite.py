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

    # def test_redeclared_global_var(self):
    #     input = """
    #     Var: a;
    #     Var: a = 1;
    #     Function: main
    #         Body: 
    #         EndBody.       
    #     """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_redeclared_many_global_var(self):
    #     input = """
    #     Var: b = {1, 2, 3};
    #     Var: a;
    #     Var: b = 1;
    #     Function: main
    #         Body:
    #         EndBody.        
    #     """
    #     expect = str(Redeclared(Variable(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_redeclared_func(self):
    #     input = """
    #     Var: foo = 1.2;
    #     Function: foo
    #         Body:
    #         EndBody.
    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_param(self):
    #     input = """
    #     Function: foo
    #         Parameter: a, b[10], a
    #         Body:
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Parameter(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_redeclared_param_is_array_lit(self):
    #     input = """
    #     Function: foo
    #         Parameter: a
    #         Body:
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.

    #     Function: foo2
    #         Parameter: b[10], b[1]
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Parameter(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_redeclared_var_in_func_body(self):
    #     input = """
    #     Function: foo
    #         Parameter: a
    #         Body:
    #             Var: a = 1;
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_var_declared_in_func_body(self):
    #     input = """
    #     Var: a;
    #     Function: foo
    #         Parameter: b
    #         Body:
    #             Var: a = 1;
    #             Var: b = {1, 2, 3};
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_undeclared_identifier(self):
    #     input = """
    #     Function: foo
    #         Body:
    #             a = 1;
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_undeclared_function(self):
    #     input = """
    #     Function: foo
    #         Parameter: a
    #         Body:
    #             a = foo1();
    #         EndBody.

    #     Function: main
    #         Body:
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Function(), "foo1"))
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_simple_bin_op(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: a, x = 1.2;
    #             a = 1 + x;
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(1), Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # def test_simple_unary_op(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: a, x = 1.2;
    #             a = -x;
    #         EndBody.
    #     """ 
    #     expect = str(TypeMismatchInExpression(UnaryOp("-", Id("x"))))
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_simple_func_call(self):
    #     input = """
    #     Function: foo
    #         Parameter: a, b
    #         Body:
    #             a = 10;
    #             b = 20;
    #         EndBody.

    #     Function: main
    #         Body:
    #             Var: a;
    #             a = foo(1);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test_simple_call_stmt(self):
    #     input = """
    #     Function: foo
    #         Body:
    #         EndBody.
    #     Function: main
    #         Body:
    #             foo(1);
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test_simple_if(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i = 1;
    #             If i Then i = False; EndIf.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(If([(Id("i"), [], [Assign(Id("i"), BooleanLiteral(False))])], ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 414))
    
    # def test_redeclared_in_if_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             If True Then 
    #                 Var: i = 10;
    #                 Var: i; 
    #             EndIf.
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), "i"))
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test_undeclared_var_in_if_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             If False Then
    #                 i = 10;
    #             EndIf.
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), "i"))
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test_simple_for_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i;
    #             For (i = 10.1, i < 10, 2) Do
    #                 read();
    #             EndFor.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(For(Id("i"), FloatLiteral(10.1), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id("read"),[])]))))
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test_simple_type_mismatch_in_for_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i = 10;
    #             For (i = 1, 2, 2) Do EndFor.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(For(Id("i"), IntLiteral(1), IntLiteral(2), IntLiteral(2), ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test_undeclared_index_in_for_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             For (i = 1, False, i) Do EndFor.
    #         EndBody.
    #     """
    #     expect = str(Undeclared(Identifier(), "i"))
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test_redeclared_var_decl_in_for_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i = 0;
    #             For (i = 1, True, 2) Do
    #                 Var: i = "Hello World!";
    #                 Var: a = 10;
    #                 Var: a;
    #             EndFor.
    #         EndBody.
    #     """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test_simple_dowhile_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i;
    #             Do 
    #                 i = i + 1;
    #             While i
    #             EndDo.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Dowhile(([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]), Id("i"))))
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_simple_while_stmt(self):
    #     input = """
    #     Function: main
    #         Body:
    #             Var: i = 1;
    #             While i Do
    #                 i = i + 2;
    #             EndWhile.
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(While(Id("i"), ([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(2)))]))))
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test_simple_no_main_func(self):
    #     input = """
    #     Var: a = "No Main Function!!!";
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_simple_return_stmt(self):
    #     input = """
    #     Function: foo
    #         Body:
    #             Return 10;
    #         EndBody.
    #     Function: main
    #         Body:
    #             foo();
    #         EndBody.
    #     """
    #     expect = str(TypeMismatchInStatement(Return(IntLiteral(10))))
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    def test_call_func_itself(self):
        input = """
        Function: main
            Body:
                main(main());
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [CallExpr(Id("main"), [])])))
        self.assertTrue(TestChecker.test(input, expect, 425))
    