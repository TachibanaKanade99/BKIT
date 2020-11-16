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
                                ([], [])    
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
                    [VarDecl(Id("n"), [], None)], 
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
                    [
                        VarDecl(Id("n"), [], None), 
                        VarDecl(Id("a"), [], None), 
                        VarDecl(Id("b"), [], None), 
                    ], 
                    ([], [])
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_func_decl_with_many_stmts(self):
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
        expect = Program([
            FuncDecl(
                Id("foo"), 
                [VarDecl(Id("a"), [], None)], 
                (
                    [], 
                    [
                        Assign(
                            Id("a"), 
                            BinaryOp("+.", Id("a"), FloatLiteral(10.0))), 
                            Assign(Id("b"),Id("a")), 
                            If(
                                [
                                    (
                                        BinaryOp("<",Id("c"),Id("a")), 
                                        [], 
                                        [Assign(Id("c"),Id("a"))]
                                    )
                                ], 
                                ([], [])
                            )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_two_func_decl(self):
        input = """
            Function: foo
                Body:
                EndBody.
            Function: main
                Body:
                    Var: a;
                    Var: b = 10;
                EndBody.
        """
        expect = Program(
            [
                FuncDecl(
                    Id("foo"), 
                    [], 
                    ([], [])
                ), 
                FuncDecl(
                    Id("main"), 
                    [], 
                    (
                        [
                            VarDecl(Id("a"), [], None), 
                            VarDecl(Id("b"), [], IntLiteral(10))
                        ], 
                        []
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_global_var_decl_and_two_func_decls(self):
        input = """
        Var: a;
        Function: foo
            Body:
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"), [], None), 
            FuncDecl(Id("foo"), [], ([], [])), 
            FuncDecl(Id("main"), [],([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_array_global_var_decl(self):
        input = """Var: a[5] = {1,4,3,2,0};"""
        expect = Program([
            VarDecl(
                Id("a"), 
                [IntLiteral(5)], 
                ArrayLiteral([
                    IntLiteral(1), 
                    IntLiteral(4), 
                    IntLiteral(3), 
                    IntLiteral(2), 
                    IntLiteral(0)
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_multi_dimension_array(self):
        input = """Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = Program([
            VarDecl(
                Id("b"), 
                [IntLiteral(2), IntLiteral(3)], 
                ArrayLiteral([
                    ArrayLiteral([
                        IntLiteral(1), 
                        IntLiteral(2), 
                        IntLiteral(3)
                    ]), 
                    ArrayLiteral([
                        IntLiteral(4), 
                        IntLiteral(5), 
                        IntLiteral(6)
                    ])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_array_in_param_func_decl(self):
        input = """
        Function: foo
            Parameter: a[10], b
            Body:
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("foo"), 
                [
                    VarDecl(Id("a"),[IntLiteral(10)], None), VarDecl(Id("b"), [], None)
                ], 
                ([], [])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_var_decl_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), 
                [], 
                (
                    [VarDecl(Id("a"), [], IntLiteral(10))], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_many_var_decl_stmt(self):
        input = """
        Function: main
            Body:
                Var: a = 10, b, c[10];
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), 
                [], 
                (
                    [
                        VarDecl(Id("a"), [], IntLiteral(10)), VarDecl(Id("b"), [], None), 
                        VarDecl(Id("c"), [IntLiteral(10)], None)
                    ], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_assign_stmt(self):
        input = """
        Function: main
            Body: 
                Var: a;
                a = 100 * 10;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), 
                [], 
                (
                    [VarDecl(Id("a"), [], None)], 
                    [Assign(Id("a"), BinaryOp("*", IntLiteral(100), IntLiteral(10)))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))
    
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
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                ([], [
                        If(
                            [
                                (
                                    BinaryOp("<", Id("i"), IntLiteral(10)), 
                                    [], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]
                                ), 
                                (
                                    BinaryOp("<", Id("i"), BinaryOp("&&", IntLiteral(20),BinaryOp("==", Id("j"), BinaryOp("+", Id("i"), IntLiteral(1))))), 
                                    [], [Assign(Id("i"), BinaryOp("+", Id("i"), BinaryOp("\.", Id("j"), Id("j"))))]
                                ), 
                                (
                                    BinaryOp("==", Id("i"), IntLiteral(10)), 
                                    [], [Assign(Id("i"), BinaryOp("+", Id("i"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", FloatLiteral(3.14), Id("r")), Id("r")), Id("r"))))]
                                ),
                                (
                                    BinaryOp("==", BinaryOp("-", Id("j"), Id("i")), IntLiteral(12)), 
                                    [], [Assign(Id("i"), BinaryOp("\.", BinaryOp("*", Id("i"), IntLiteral(10)), FloatLiteral(12.3)))]
                                )
                            ], 
                            (
                                [], []
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    
    def test_func_call_expr(self):
        input = """
        Function: main
            Parameter: a
            Body:
                a = foo(2);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), 
                [VarDecl(Id("a"), [], None)], 
                (
                    [], 
                    [Assign(Id("a"), CallExpr(Id("foo"),[IntLiteral(2)]))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_simple_index_expr(self):
        input = """
        Function: main
            Body: 
                a = a[2][3][4];
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Assign(
                            Id("a"), 
                            ArrayCell(
                                Id("a"), 
                                [
                                    IntLiteral(2), 
                                    IntLiteral(3), 
                                    IntLiteral(4)
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_index_expr(self):
        input = """
        Function: main
            Body: 
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        ArrayCell(
                            Id("a"), 
                            [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]
                        ), 
                        BinaryOp(
                            "+", 
                            ArrayCell(
                                Id("a"), 
                                [ArrayCell(
                                    Id("b"), 
                                    [
                                        IntLiteral(2),IntLiteral(3)
                                    ]
                                )]
                            ), 
                            IntLiteral(4)
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_index_op_inside_index_op(self):
        input = """
        Function: main
            Body:
                a[3 + foo(2)][i[1][23 + i] + 10] = 20;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        ArrayCell(
                            Id("a"), 
                            [
                                BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)])), 
                                BinaryOp("+",ArrayCell(Id("i"), [IntLiteral(1), BinaryOp("+", IntLiteral(23), Id("i"))]), IntLiteral(10))
                            ]
                        ), 
                    IntLiteral(20))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_func_call_with_many_arguments(self):
        input = """
        Function: main
            Body:
                a = foo(a, b, c[10 * i]);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        CallExpr(
                            Id("foo"), 
                            [Id("a"), Id("b"), ArrayCell(Id("c"), [BinaryOp("*", IntLiteral(10), Id("i"))])
                            ]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_call_stmt(self):
        input = """
        Function: main
            Body:
                foo(2 * x + 3);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        CallStmt(
                            Id("foo"), 
                            [BinaryOp("+",BinaryOp("*", IntLiteral(2), Id("x")), IntLiteral(3))]
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    def test_call_stmt_with_two_params(self):
        input = """
        Function: foo
            Body:
                foo (2 + x, 4. \.y);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("foo"), [], 
                (
                    [], 
                    [CallStmt(
                        Id("foo"), 
                        [
                            BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\.", FloatLiteral(4.0), Id("y"))
                        ]
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

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
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [If(
                        [
                            (BinaryOp("==", Id("i"), IntLiteral(0)), [], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))])
                        ], 
                        ([], [
                            If(
                                [
                                    (BinaryOp("==", Id("i"), Id("j")), [], [Assign(Id("i"), BinaryOp("+", Id("j"), IntLiteral(1)))])
                                ], 
                                ([], [])
                            )
                        ]) 
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))         

    def test_if_inside_else_if_stmt(self):
        input = """
        Function: main
            Body:
                If i Then Var: j;
                ElseIf j Then
                    If i == 1 Then Var: i; EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [If(
                        [
                            (Id("i"), [VarDecl(Id("j"), [], None)], []), 
                            (
                                Id("j"), [], 
                                [If(
                                    [
                                        (BinaryOp("==", Id("i"), IntLiteral(1)), [VarDecl(Id("i"), [], None)], [])
                                    ], 
                                    ([], [])
                                )]
                            )
                        ], 
                        ([], [])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_simple_for_stmt(self):
        input = """
        Function: main
            Body:
                For (a = 0, a < 10, a + 1) Do
                    b = a;
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [For(
                        Id("a"), 
                        IntLiteral(0), 
                        BinaryOp("<", Id("a"), IntLiteral(10)), 
                        BinaryOp("+", Id("a"), IntLiteral(1)), 
                        (
                            [], 
                            [Assign(Id("b"), Id("a"))]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_for_stmt(self):
        input = """
        Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(2);
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [] , 
                (
                    [], 
                    [For(
                        Id("i"), 
                        IntLiteral(0), 
                        BinaryOp("<",Id("i"), IntLiteral(10)), 
                        IntLiteral(2), 
                        (
                            [], 
                            [CallStmt(Id("writeln"),[IntLiteral(2)])]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_simple_while_stmt(self):
        input = """
        Function: main
            Body:
                While (i < 0) Do i = i - 1; EndWhile.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [While(
                        BinaryOp("<", Id("i"), IntLiteral(0)), 
                        (
                            [], 
                            [Assign(Id("i"), BinaryOp("-", Id("i"),IntLiteral(1)))]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_while_stmt_with_empty_stmt_lst(self):
        input = """
        Function: main
            Body:
                While i - 2 Do EndWhile.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [While(
                        BinaryOp("-", Id("i"), IntLiteral(2)), 
                        ([],[])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

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
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Dowhile(
                        (
                            [], 
                            [
                                Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(2))), 
                                If(
                                    [
                                        (BinaryOp("==", Id("i"), IntLiteral(0)), [], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))])
                                    ], 
                                    ([],[])
                                ),
                            ] 
                        ), 
                        BinaryOp("==", Id("j"), Id("i"))
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_simple_break_stmt(self):
        input = """
        Function: main
            Body: 
                Break;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Break()]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_break_stmt_with_var_decl_stmt(self):
        input = """
        Function: main
            Body:
                Var: a;
                Break;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [VarDecl(Id("a"), [], None)], 
                    [Break()]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

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
        expect = Program([
            FuncDecl(
                Id("foo"), 
                [
                    VarDecl(Id("a"), [], None), 
                    VarDecl(Id("b"), [], None), 
                    VarDecl(Id("a"), [IntLiteral(12)], None)
                ], 
                (
                    [
                        VarDecl(Id("i"), [], None), 
                        VarDecl(Id("j"), [], IntLiteral(0))
                    ], 
                    [
                        For(
                            Id("i"), 
                            Id("j"), 
                            BinaryOp("<", Id("i"), IntLiteral(100)), 
                            BinaryOp("+", Id("i"), IntLiteral(1)), 
                            (
                                [], 
                                [If(
                                    [
                                        (BinaryOp("<", Id("i"), IntLiteral(90)), [], [Break()])
                                    ], 
                                    ([], [])
                                )]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_simple_continue_stmt(self):
        input = """
        Function: main
            Body: 
                Continue;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), 
                [], 
                (
                    [], [Continue()]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

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
        expect = Program([
            FuncDecl(
                Id("foo"), 
                [
                    VarDecl(Id("a"), [], None), 
                    VarDecl(Id("b"), [], None), 
                    VarDecl(Id("a"), [IntLiteral(12)], None)
                ], 
                (
                    [
                        VarDecl(Id("i"), [], None), 
                        VarDecl(Id("j"), [], IntLiteral(0))
                    ], 
                    [While(
                        BinaryOp(">", Id("i"), IntLiteral(10)), 
                        (
                            [], 
                            [
                                Assign(
                                    Id("i"), 
                                    BinaryOp(
                                        "+", 
                                        BinaryOp("*.", Id("i"), Id("i")), 
                                        BinaryOp("\.", IntLiteral(1), IntLiteral(12))
                                    )
                                ), 
                                If(
                                    [
                                        (
                                            BinaryOp("==", Id("i"), IntLiteral(0)), 
                                            [], 
                                            [Assign(Id("i"), BinaryOp("*.", Id("i"), FloatLiteral(12.5))), Continue()]
                                        ), 
                                    ], 
                                    ([],[])
                                )
                            ]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_simple_return_stmt(self):
        input = """
        Function: main
            Body:
                Return;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], [Return(None)]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_return_stmt_with_expr(self):
        input = """
        Function: main
            Body:
                Return i == 1;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                ([], [Return(BinaryOp("==", Id("i"), IntLiteral(1)))])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

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
        expect = Program([
            FuncDecl(
                Id("main"), 
                [
                    VarDecl(Id("a"), [], None), 
                    VarDecl(Id("b"), [], None), 
                    VarDecl(Id("a"), [IntLiteral(10), IntLiteral(12), IntLiteral(13), IntLiteral(14), IntLiteral(15)], None)
                ], 
                (
                    [
                        VarDecl(Id("a"), [], ArrayLiteral([IntLiteral(12), IntLiteral(14), IntLiteral(15)]))
                    ], 
                    [
                        Assign(
                            CallExpr(Id("m"),[IntLiteral(13)]), 
                            ArrayLiteral(
                                [
                                    IntLiteral(12), 
                                    ArrayLiteral(
                                        [
                                            IntLiteral(12), 
                                            IntLiteral(14), 
                                            IntLiteral(15)
                                        ]
                                    )
                                ]
                            )
                        ), 
                        Return(None)
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_cmt_inside_array_lit(self):
        input = """
        Function: main
            Body:
                Var: a = { ** This is comment ** 1 };
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [VarDecl(Id("a"), [], ArrayLiteral([IntLiteral(1)]))], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    
    def test_empty_stmt(self):
       input = """"""
       expect = Program([])
       self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_empty_program_with_cmt(self):
        input = """ ** This is comment** """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_idx_expr_precedence(self):
        input = """
        Function: main
            Body:
                a = a[i[n + 1] - ae[10] && 100] \. 12.2; 
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Assign(
                            Id("a"), 
                            BinaryOp(
                                "\.", 
                                ArrayCell(
                                    Id("a"), 
                                    [BinaryOp(
                                        "&&", 
                                        BinaryOp(
                                            "-", 
                                            ArrayCell(Id("i"), [BinaryOp("+", Id("n"), IntLiteral(1))]), 
                                            ArrayCell(Id("ae"), [IntLiteral(10)])
                                        ), 
                                        IntLiteral(100)
                                    )]
                                ), 
                                FloatLiteral(12.2)
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_type_coersion_func(self):
        input = """
        Function: main
            Body: 
                If bool_of_string (" True" ) Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [If(
                        [
                            (
                                CallExpr(
                                    Id("bool_of_string"), 
                                    [StringLiteral(" True")]
                                ), 
                                [], 
                                [
                                    Assign(
                                        Id("a"), 
                                        CallExpr(
                                            Id("int_of_string"), 
                                            [CallExpr(Id("read"), [])]
                                        )
                                    ), 
                                    Assign(
                                        Id("b"), 
                                        BinaryOp(
                                            "+.", 
                                            CallExpr(
                                                Id("float_of_int"), 
                                                [Id("a")]
                                            ), 
                                            FloatLiteral(2.0)
                                        )
                                    )
                                ]
                            )
                        ], 
                        ([], [])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_many_variable_stmt(self):
        input = """
        Function: main
            Body:
                Var: a, b = 10, c[20] = {1, {2, 3, {4, 5, {6, 7}}}}, f = 23.4;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [
                        VarDecl(Id("a"), [], None), 
                        VarDecl(Id("b"), [], IntLiteral(10)), 
                        VarDecl(
                            Id("c"), 
                            [IntLiteral(20)], 
                            ArrayLiteral(
                                [
                                    IntLiteral(1), 
                                    ArrayLiteral(
                                        [
                                            IntLiteral(2), 
                                            IntLiteral(3), 
                                            ArrayLiteral(
                                                [
                                                    IntLiteral(4), IntLiteral(5), ArrayLiteral(
                                                        [
                                                            IntLiteral(6), 
                                                            IntLiteral(7)
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            )
                        ), 
                        VarDecl(Id("f"), [], FloatLiteral(23.4))
                    ], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_break_stmt_inside_func_decl(self):
        input = """ 
        Function: main
            Body:
                Break;
            EndBody.

        Function: foo
            Body:
                Break;
                If foo(2) Then Break; ElseIf foo() Then Break; EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Break()]
                )
            ), 
            FuncDecl(
                Id("foo"), [], 
                (
                    [], 
                    [
                        Break(), 
                        If(
                            [
                                (CallExpr(Id("foo"), [IntLiteral(2)]), [], [Break()]), 
                                (CallExpr(Id("foo"), []), [], [Break()])
                            ], 
                            ([], [])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_many_break_in_stmt_lst(self):
        input = """
        Function: main
            Body:
                Break;Break;Break;Break;Break;Break;Break;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Break(), 
                        Break(), 
                        Break(), 
                        Break(), 
                        Break(), 
                        Break(), 
                        Break()
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_continue_stmt_in_function_decl(self):
        input = """
        Function: main
            Body:
                Continue;Continue;Continue;Continue;Continue;Continue;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Continue(), 
                        Continue(), 
                        Continue(), 
                        Continue(), 
                        Continue(), 
                        Continue()
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_return_with_simple_expr(self):
        input = """
        Function: main
            Body:
                Return 2 + 3;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Return(
                            BinaryOp("+", IntLiteral(2), IntLiteral(3))
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_return_stmt_with_complex_expression(self):
        input = """
        Function: main
            Body:
                Return 2[i + 1] || 3[i - 1] * (23 \. a + ((a - c) *. 1));
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Return(
                            BinaryOp(
                                "||", 
                                ArrayCell(IntLiteral(2), [BinaryOp("+", Id("i"), IntLiteral(1))]), 
                                BinaryOp(
                                    "*", 
                                    ArrayCell(IntLiteral(3), [BinaryOp("-", Id("i"), IntLiteral(1))]), 
                                    BinaryOp(
                                        "+", 
                                        BinaryOp("\.", IntLiteral(23), Id("a")), 
                                        BinaryOp(
                                            "*.", 
                                            BinaryOp("-", Id("a"), Id("c")), IntLiteral(1)
                                        )
                                    )
                                )
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_boolean_literal(self):
        input = """
        Function: main
            Body:
                Var: a = True;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [VarDecl(Id("a"), [], BooleanLiteral(True))], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_simple_unary_op(self):
        input = """
        Function: main
            Body:
                a = -2 + - (12 + a);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        BinaryOp(
                            "+", 
                            UnaryOp("-", IntLiteral(2)), 
                            UnaryOp(
                                "-", 
                                BinaryOp("+", IntLiteral(12), Id("a"))
                            )
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_empty_stmt_lst_in_for(self):
        input = """
        Function: main
            Body:
                For (i = -1, i, i) Do EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [For(
                        Id("i"), 
                        UnaryOp("-", IntLiteral(1)), 
                        Id("i"), 
                        Id("i"), 
                        ([], [])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_string_lit_with_escaped_char(self):
        input = """
        Function: main
            Body:
                a = "Hi I am \\n Tuan";
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        StringLiteral("Hi I am \\n Tuan")
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_empty_param_call_stmt(self):
        input = """
        Function: main
            Body:
                foo();
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [CallStmt(
                        Id("foo"), []
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_func_call_inside_call_stmt(self):
        input = """
        Function: main
            Body:
                read(foo(), foo1(1 && a[2]));
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [CallStmt(
                        Id("read"), 
                        [
                            CallExpr(Id("foo"), []), 
                            CallExpr(Id("foo1"), [BinaryOp("&&", IntLiteral(1),ArrayCell(Id("a"), [IntLiteral(2)]))])
                        ]
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_empty_stmt_lst_in_do_while(self):
        input = """
        Function: main
            Body:
                Do While -1 EndDo.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Dowhile(
                        ([], []), 
                        UnaryOp("-", IntLiteral(1))
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_nested_many_if_stmt(self):
        input = """
        Function: main
            Body:
                If i Then
                    If j Then
                        Var: f;
                    Else
                        Var: m = {"1", "\\n"};
                    EndIf.
                ElseIf m Then 
                    If n Then n = m;
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [If(
                        [
                            (
                                Id("i"), [], 
                                [If(
                                    [
                                        (Id("j"), [VarDecl(Id("f"), [], None)], [])
                                    ], 
                                    ([VarDecl(Id("m"), [], ArrayLiteral([StringLiteral("1"), StringLiteral("\\n")]))], [])
                                )]
                            ), 
                            (
                                Id("m"), [], 
                                [If(
                                    [
                                        (Id("n"), [], [Assign(Id("n"), Id("m"))])
                                    ], 
                                    ([], [])
                                )]
                            )
                        ], 
                        ([], [])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_hexadecimal_intlit(self):
        input = """
        Function: main
            Body:
                Var: a = 0X1ACF;
                a = 0X1ABF;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [
                        VarDecl(
                            Id("a"), [], IntLiteral(6863)
                        )
                    ], 
                    [Assign(
                        Id("a"), IntLiteral(6847)
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_octal_intlit(self):
        input = """
        Function: main
            Body:
                Var: a = 0o15;
                a = 0O1576;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [VarDecl(
                        Id("a"), [], IntLiteral(13)
                    )], 
                    [Assign(
                        Id("a"), IntLiteral(894))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_simple_use_float_lit(self):
        input = """
        Function: main
            Body:
                Var: x = 12.0e-3;
                y = 12.e5 *. 12000.;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [
                        VarDecl(
                            Id("x"), [], FloatLiteral(0.012)
                        )
                    ], 
                    [
                        Assign(
                            Id("y"),  
                            BinaryOp(
                                "*.", 
                                FloatLiteral(1200000.0), 
                                FloatLiteral(12000.0)
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_multiple_lits_inside_array_lit(self):
        input = """
        Function: main
            Body:
                Var: a = {0XABF, 0o1, True, False, "Hi", "Hello\\n\\t", {{{1}}}};
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [
                        VarDecl(
                            Id("a"), [], 
                            ArrayLiteral([
                                IntLiteral(2751), 
                                IntLiteral(1), 
                                BooleanLiteral(True), 
                                BooleanLiteral(False), 
                                StringLiteral("Hi"), 
                                StringLiteral("Hello\\n\\t"), 
                                ArrayLiteral([
                                    ArrayLiteral([
                                        ArrayLiteral([
                                            IntLiteral(1)
                                        ])
                                    ])
                                ])
                            ])
                        )
                    ], 
                    []
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_idx_expression_with_hexadecimal(self):
        input = """
        Function: main
            Body:
                a[12e-3 + 0x111] = 10;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Assign(
                            ArrayCell(
                                Id("a"), 
                                [BinaryOp("+", FloatLiteral(0.012), IntLiteral(273))]
                            ), 
                            IntLiteral(10)
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_multiple_idx_ops(self):
        input = """
        Function: main
            Body: 
                a = a[12[12.[0o127]]];
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        ArrayCell(
                            Id("a"), 
                            [
                                ArrayCell(
                                    IntLiteral(12), 
                                    [
                                        ArrayCell(
                                            FloatLiteral(12.0), 
                                            [IntLiteral(87)]
                                        )
                                    ]
                                )
                            ]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_assign_stmt_with_array_lit(self):
        input = """
        Function: main
            Body:
                arr[10] = {1, {0, "12e-3"}};
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Assign(
                            ArrayCell(
                                Id("arr"), 
                                [IntLiteral(10)]
                            ), 
                            ArrayLiteral([
                                IntLiteral(1), 
                                ArrayLiteral([
                                    IntLiteral(0), 
                                    StringLiteral("12e-3")
                                ])
                            ])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_precedence_of_func_call(self):
        input = """
        Function: main 
            Body:
                a = func_call(10) + 12.3 \. 0.;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [
                        Assign(
                            Id("a"), 
                            BinaryOp(
                                "+", 
                                CallExpr(
                                    Id("func_call"), [IntLiteral(10)]
                                ), 
                                BinaryOp("\.", FloatLiteral(12.3), FloatLiteral(0.0))
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_precedence_of_eq_logical_op(self):
        input = """
        Function: main
            Body:
                a = a =/= b && abc;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        BinaryOp(
                            "=/=", 
                            Id("a"), 
                            BinaryOp("&&", Id("b"), Id("abc"))
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_precedence_logical_plus_op(self):
        input = """
        Function: main
            Body:
                a = a <=. b - 1. || a;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"), [], 
                (
                    [], 
                    [Assign(
                        Id("a"), 
                        BinaryOp(
                            "<=.", 
                            Id("a"), 
                            BinaryOp(
                                "||", 
                                BinaryOp("-", Id("b"), FloatLiteral(1.0)), 
                                Id("a")
                            )
                        )
                    )]
                )
            )
        ])  
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_plus_mul_op_precedence(self):
        input = """
        Function: main
            Body:
                a = a + a * 12;
            EndBody.
        """

    
    
    


    



    

    
    

    
    
