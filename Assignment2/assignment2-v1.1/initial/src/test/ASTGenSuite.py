import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_global_var_decl(self):
        input = """Var:x;"""
        expect = Program(
            [
                VarDecl(Id("x"), [], None)
            ]
        ) 
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_one_dimension_global_var_decl(self):
        input = """Var: a[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_if_stmt(self):
        input = """
        Function: main
            Body:
                If i < 2 Then i = i + 1;
                EndIf.
            EndBody.
        """
        expect = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            If(
                                [
                                    (
                                        BinaryOp("<",Id("i"),IntLiteral(2)),
                                        [],
                                        [
                                            Assign(
                                                Id("i"),
                                                BinaryOp("+",Id("i"),IntLiteral(1))
                                            )
                                        ]
                                    )
                                ],
                                []    
                            )
                        ]
                    )
                )
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_multi_dimension_global_var_decl(self):
        input = """Var: a[10][20];"""
        expect = Program(
            [
                VarDecl(Id("a"), [IntLiteral(10), IntLiteral(20)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_multiple_global_var_decl(self):
        input = """Var: a, b[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("b"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_global_var_decl_with_initial_val(self):
        input = """Var: a = 10;"""
        expect = Program(
            [
                VarDecl(Id("a"), [], IntLiteral(10))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    
    def test_multiple_global_var_decl_with_initial_val(self):
        input = """Var: a = 12e-3, b[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [], FloatLiteral(0.012)),VarDecl(Id("b"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    
