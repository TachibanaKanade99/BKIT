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
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_one_dimension_global_var_decl(self):
        input = """Var: a[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

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
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_multi_dimension_global_var_decl(self):
        input = """Var: a[10][20];"""
        expect = Program(
            [
                VarDecl(Id("a"), [IntLiteral(10), IntLiteral(20)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_multiple_global_var_decl(self):
        input = """Var: a, b[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("b"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_global_var_decl_with_initial_val(self):
        input = """Var: a = 10;"""
        expect = Program(
            [
                VarDecl(Id("a"), [], IntLiteral(10))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    
    def test_multiple_global_var_decl_with_initial_val(self):
        input = """Var: a = 12e-3, b[10];"""
        expect = Program(
            [
                VarDecl(Id("a"), [], FloatLiteral(0.012)),
                VarDecl(Id("b"), [IntLiteral(10)], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_globl_var_decl_with_array_lit_(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = Program(
            [
                VarDecl(Id("b"), 
                    [IntLiteral(2), IntLiteral(3)],
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]),
                        ArrayLiteral([IntLiteral(4), IntLiteral(5),IntLiteral(6)])
                    ])
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_simple_var_decl_stmt(self):
        input = """
        Var: a;
        Function: main
            Body:
                Var: a;
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"), [], None), 
            FuncDecl(
                Id("main"), [], 
                ([VarDecl(Id("a"), [], None)], [])
            )
        ]) 
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_elseif_stmt(self):
        input = """
        Function: main
            Body:
                If i Then i = i + 1;
                ElseIf j Then j = j \. 1;
                Else i = i * j;
                EndIf.
            EndBody.
        """
        expect = Program(
            [FuncDecl(
                Id("main"), [], 
                ([], 
                [If(
                    [
                        (Id("i"), [], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]
                        ), 
                        (Id("j"), [], [Assign(Id("j"), BinaryOp("\.", Id("j"), IntLiteral(1)))])
                    ], 
                    ([], [Assign(Id("i"), BinaryOp("*", Id("i"), Id("j")))])
                    )
                ])
            )]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_multiple_global_variable(self):
        input = """Var: c, d = 6, e, f;"""
        expect = Program(
            [
                VarDecl(Id("c"), [], None), 
                VarDecl(Id("d"), [], IntLiteral(6)), 
                VarDecl(Id("e"), [], None), 
                VarDecl(Id("f"), [], None)
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_empty_func_decl(self):
        input = """
        Function: foo
            Body: 
            EndBody.
        """
        expect = Program(
            [
                FuncDecl(Id("foo"), [], ([], []))
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    
    def test_func_decl_with_one_param(self):
        input = """
        Function: foo
            Parameter: n
            Body:
                n = 10;
            EndBody.
        """
        expect = Program(
            [
                FuncDecl(
                    Id("foo"), 
                    [Id("n")], 
                    (
                        [], 
                        [Assign(Id("n"), IntLiteral(10))]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_func_decl_with_many_params(self):
        input = """
        Function: foo
            Parameter: n, a, b
            Body:
            EndBody.
        """
        expect = Program(
            [
                FuncDecl(
                    Id("foo"), 
                    [Id("n"), Id("a"), Id("b")], 
                    ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    
    
