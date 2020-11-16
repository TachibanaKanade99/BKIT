# ID:1752595

from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    # program: many_declars EOF;
    def visitProgram(self, ctx):
        return Program(ctx.many_declars().accept(self))

    # many_declars: global_var_declar_lst func_declar_lst;
    def visitMany_declars(self, ctx):
        return ctx.global_var_declar_lst().accept(self) + ctx.func_declar_lst().accept(self)

    # global_var_declar_lst: var_decl many_var_decl | ;
    def visitGlobal_var_declar_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return ctx.var_decl().accept(self) + ctx.many_var_decl().accept(self)
        else:
            return []

    # many_var_decl: var_decl many_var_decl | ;
    def visitMany_var_decl(self, ctx):
        if ctx.getChildCount() == 2:
            return  ctx.var_decl().accept(self) + ctx.many_var_decl().accept(self)
        else:
            return []

    # var_decl: VAR COLON var_lst SEMI;
    def visitVar_decl(self, ctx):
        decl_lst = []
        variable_lst = ctx.var_lst().accept(self)

        for variable in variable_lst:
            # variable[0] : ID
            # variable[1] : dimension
            # varialbe[2] : initial_value
            
            decl_lst.append(VarDecl(variable[0], variable[1], variable[2]))

        return decl_lst

    # var_lst: var many_var;
    def visitVar_lst(self, ctx):
        return [ctx.var().accept(self)] + ctx.many_var().accept(self)

    # many_var: COMMA var many_var | ;
    def visitMany_var(self, ctx):
        if ctx.getChildCount() == 3:
            return [ctx.var().accept(self)] + ctx.many_var().accept(self)
        else:
            return []

    # var: ( ID | composite_var ) initial_value;
    def visitVar(self, ctx):
        if ctx.ID():
            return [Id(ctx.ID().getText())] + [[]] + [ctx.initial_value().accept(self)]
        else:
            return ctx.composite_var().accept(self) + [ctx.initial_value().accept(self)]

    # initial_value: ASSIGN lit | ;
    def visitInitial_value(self, ctx):
        if ctx.getChildCount() == 2:
            return ctx.lit().accept(self)
        else:
            return None

    # lit: INT_LIT | FLOAT_LIT | STRING_LIT | bool_lit | array_lit;
    def visitLit(self, ctx):
        if ctx.INT_LIT():
            prefix = ctx.INT_LIT().getText()[0:2]

            if prefix == "0X" or prefix == "0x":
                return IntLiteral(int(ctx.INT_LIT().getText(), 16))
            elif prefix == "0o" or prefix == "0O":
                return IntLiteral(int(ctx.INT_LIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INT_LIT().getText()))
            # return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_lit():
            return BooleanLiteral(ctx.bool_lit().accept(self))
        else:
            return ctx.array_lit().accept(self)

    # bool_lit: TRUE | FALSE;
    def visitBool_lit(self, ctx):
        if ctx.TRUE():
            return ctx.TRUE().getText()
        else:
            return ctx.FALSE().getText()

    # array_lit: LB lit_list RB;
    def visitArray_lit(self, ctx):
        return ArrayLiteral(ctx.lit_list().accept(self))

    # lit_list: lit many_lits;
    def visitLit_list(self, ctx):
        return [ctx.lit().accept(self)] + ctx.many_lits().accept(self)

    # many_lits: COMMA lit many_lits | ;
    def visitMany_lits(self, ctx):
        if ctx.getChildCount() == 3:
            return [ctx.lit().accept(self)] + ctx.many_lits().accept(self)
        else:
            return []

    # composite_var: ID dimension_lst;
    def visitComposite_var(self, ctx):
        return [Id(ctx.ID().getText())] + [ctx.dimension_lst().accept(self)]

    # dimension_lst: dimension many_dimension;
    def visitDimension_lst(self, ctx):
        return [ctx.dimension().accept(self)] + ctx.many_dimension().accept(self)

    # many_dimension: dimension many_dimension | ;
    def visitMany_dimension(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.dimension().accept(self)] + ctx.many_dimension().accept(self)
        else:
            return []

    # dimension: LSB INT_LIT RSB;
    def visitDimension(self, ctx):
        return IntLiteral(int(ctx.INT_LIT().getText()))

    # func_declar_lst: func_decl many_func_decl | ;
    def visitFunc_declar_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.func_decl().accept(self)] + ctx.many_func_decl().accept(self)
        else:
            return []

    # many_func_decl: func_decl many_func_decl | ;
    def visitMany_func_decl(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.func_decl().accept(self)] + ctx.many_func_decl().accept(self)
        else:
            return []

    # func_decl: FUNCTION COLON func_name func_param? body;
    def visitFunc_decl(self, ctx):
        if ctx.func_param():
            return FuncDecl(ctx.func_name().accept(self), ctx.func_param().accept(self), ctx.body().accept(self))
        else:
            return FuncDecl(ctx.func_name().accept(self), [], ctx.body().accept(self))

    # func_name: ID;
    def visitFunc_name(self, ctx):
        return Id(ctx.ID().getText())

    # func_param: PARAMETER COLON param_lst;
    def visitFunc_param(self, ctx):
        decl_lst = []
        param_lst = ctx.param_lst().accept(self)

        for param in param_lst:
            # param[0]: ID
            # param[1]: dimension
            decl_lst.append(VarDecl(param[0], param[1], None))
        
        return decl_lst

    # param_lst: param many_params;
    def visitParam_lst(self, ctx):
        return [ctx.param().accept(self)] + ctx.many_params().accept(self)

    # many_params: COMMA param many_params | ;
    def visitMany_params(self, ctx):
        if ctx.getChildCount() == 3:
            return [ctx.param().accept(self)] + ctx.many_params().accept(self)
        else:
            return []

    # param: ID | composite_var;
    def visitParam(self, ctx):
        if ctx.ID():
            return [Id(ctx.ID().getText())] + [[]]
        else:
            return ctx.composite_var().accept(self)

    # body: BODY COLON stmt_lst ENDBODY DOT;
    def visitBody(self, ctx):
        return ctx.stmt_lst().accept(self)

    # stmt_lst: global_var_declar_lst other_stmt_lst;
    def visitStmt_lst(self, ctx):
        return (ctx.global_var_declar_lst().accept(self), ctx.other_stmt_lst().accept(self))

    # other_stmt_lst: stmt many_stmts | ;
    def visitOther_stmt_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.stmt().accept(self)] + ctx.many_stmts().accept(self)
        else:
            return []

    # many_stmts: stmt many_stmts | ;
    def visitMany_stmts(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.stmt().accept(self)] + ctx.many_stmts().accept(self)
        else:
            return []

    """
    expr: operand_1 (EQ | NOT_EQ) operand_1
    | operand_1 (LESS | GREATER) operand_1
    | operand_1 (LESS_EQ | GREATER_EQ) operand_1
    | operand_1 FLOAT_NOT_EQ operand_1
    | operand_1 (FLOAT_LESS | FLOAT_GREATER) operand_1
    | operand_1 (FLOAT_LESS_EQ | FLOAT_GREATER_EQ) operand_1
    | operand_1; 
    """
    def visitExpr(self, ctx):
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.NOT_EQ():
            return BinaryOp(ctx.NOT_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.LESS():
            return BinaryOp(ctx.LESS().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.GREATER():
            return BinaryOp(ctx.GREATER().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.LESS_EQ():
            return BinaryOp(ctx.LESS_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.GREATER_EQ():
            return BinaryOp(ctx.GREATER_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.FLOAT_NOT_EQ():
            return BinaryOp(ctx.FLOAT_NOT_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.FLOAT_LESS():
            return BinaryOp(ctx.FLOAT_LESS().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.FLOAT_GREATER():
            return BinaryOp(ctx.FLOAT_GREATER().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.FLOAT_LESS_EQ():
            return BinaryOp(ctx.FLOAT_LESS_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        elif ctx.FLOAT_GREATER_EQ():
            return BinaryOp(ctx.FLOAT_GREATER_EQ().getText(), ctx.operand_1(0).accept(self), ctx.operand_1(1).accept(self))
        else:
            return ctx.operand_1(0).accept(self)

    # operand_1: operand_1 (AND | OR) operand_2 | operand_2;
    def visitOperand_1(self, ctx):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), ctx.operand_1().accept(self), ctx.operand_2().accept(self))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), ctx.operand_1().accept(self), ctx.operand_2().accept(self))
        else:
            return ctx.operand_2().accept(self)

    # operand_2: operand_2 (PLUS | FLOAT_PLUS | MINUS | FLOAT_MINUS) operand_3 | operand_3;
    def visitOperand_2(self, ctx):
        if ctx.PLUS():
            return BinaryOp(ctx.PLUS().getText(), ctx.operand_2().accept(self), ctx.operand_3().accept(self))
        elif ctx.FLOAT_PLUS():
            return BinaryOp(ctx.FLOAT_PLUS().getText(), ctx.operand_2().accept(self), ctx.operand_3().accept(self))
        elif ctx.MINUS():
            return BinaryOp(ctx.MINUS().getText(), ctx.operand_2().accept(self), ctx.operand_3().accept(self))
        elif ctx.FLOAT_MINUS():
            return BinaryOp(ctx.FLOAT_MINUS().getText(), ctx.operand_2().accept(self), ctx.operand_3().accept(self))
        else:
            return ctx.operand_3().accept(self)

    # operand_3: operand_3 (MUL | FLOAT_MUL | DIV | FLOAT_DIV | MOD) operand_4 | operand_4;
    def visitOperand_3(self, ctx):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), ctx.operand_3().accept(self), ctx.operand_4().accept(self))
        elif ctx.FLOAT_MUL():
            return BinaryOp(ctx.FLOAT_MUL().getText(), ctx.operand_3().accept(self), ctx.operand_4().accept(self))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), ctx.operand_3().accept(self), ctx.operand_4().accept(self))
        elif ctx.FLOAT_DIV():
            return BinaryOp(ctx.FLOAT_DIV().getText(), ctx.operand_3().accept(self), ctx.operand_4().accept(self))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), ctx.operand_3().accept(self), ctx.operand_4().accept(self))
        else:
            return ctx.operand_4().accept(self)

    # operand_4: NOT operand_4 | operand_5;
    def visitOperand_4(self, ctx):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), ctx.operand_4().accept(self))
        else:
            return ctx.operand_5().accept(self)
    
    # operand_5: (MINUS | FLOAT_MINUS) operand_5 | index_expr;
    def visitOperand_5(self, ctx):
        if ctx.MINUS():
            return UnaryOp(ctx.MINUS().getText(), ctx.operand_5().accept(self))
        elif ctx.FLOAT_MINUS():
            return UnaryOp(ctx.FLOAT_MINUS().getText(), ctx.operand_5().accept(self))
        else:
            return ctx.index_expr().accept(self)

    # index_expr: index_expr index_ops | func_call;
    def visitIndex_expr(self, ctx):
        if ctx.getChildCount() == 2:
            return ArrayCell(ctx.index_expr().accept(self), ctx.index_ops().accept(self))
        else:
            return ctx.func_call().accept(self)

    # index_ops: LSB expr RSB index_ops | LSB expr RSB;
    def visitIndex_ops(self, ctx):
        if ctx.getChildCount() == 4:
            return [ctx.expr().accept(self)] + ctx.index_ops().accept(self)
        else:
            return [ctx.expr().accept(self)]

    # func_call: ID LP argument_lst RP | operand;
    def visitFunc_call(self, ctx):
        if ctx.getChildCount() == 4:
            return CallExpr(Id(ctx.ID().getText()), ctx.argument_lst().accept(self))
        else:
            return ctx.operand().accept(self)

    # operand: lit | ID | LP expr RP;
    def visitOperand(self, ctx):
        if ctx.lit():
            return ctx.lit().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expr():
            return ctx.expr().accept(self)

    # argument_lst: argument many_arguments | ;
    def visitArgument_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.argument().accept(self)] + ctx.many_arguments().accept(self)
        else:
            return []
    
    # many_arguments: COMMA argument many_arguments | ;
    def visitMany_arguments(self, ctx):
        if ctx.getChildCount() == 3:
            return [ctx.argument().accept(self)] + ctx.many_arguments().accept(self)
        else:
            return []

    # argument: expr;
    def visitArgument(self, ctx):
        return ctx.expr().accept(self)

    # stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;
    def visitStmt(self, ctx):
        if ctx.assign_stmt():
            return ctx.assign_stmt().accept(self)
        elif ctx.if_stmt():
            return ctx.if_stmt().accept(self)
        elif ctx.for_stmt():
            return ctx.for_stmt().accept(self)
        elif ctx.while_stmt():
            return ctx.while_stmt().accept(self)
        elif ctx.do_while_stmt():
            return ctx.do_while_stmt().accept(self)
        elif ctx.break_stmt():
            return ctx.break_stmt().accept(self)
        elif ctx.continue_stmt():
            return ctx.continue_stmt().accept(self)
        elif ctx.call_stmt():
            return ctx.call_stmt().accept(self)
        elif ctx.return_stmt():
            return ctx.return_stmt().accept(self)

    # assign_stmt: (ID | index_expr) ASSIGN expr SEMI;
    def visitAssign_stmt(self, ctx):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()), ctx.expr().accept(self))
        else:
            return Assign(ctx.index_expr().accept(self), ctx.expr().accept(self))

    # if_stmt: IF expr THEN stmt_lst elseif_stmt_lst else_stmt ENDIF DOT;
    def visitIf_stmt(self, ctx):
        ifthen_stmts = []
        stmts = ctx.stmt_lst().accept(self)
        vardecl_lst = stmts[0]
        stmt_lst = stmts[1]

        ifthen_stmts.append((ctx.expr().accept(self), vardecl_lst, stmt_lst))

        return If(ifthen_stmts + ctx.elseif_stmt_lst().accept(self), ctx.else_stmt().accept(self))

    # elseif_stmt_lst: elseif_stmt many_elseif_stmts | ;
    def visitElseif_stmt_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.elseif_stmt().accept(self)] + ctx.many_elseif_stmts().accept(self)
        else:
            return []

    # many_elseif_stmts: elseif_stmt many_elseif_stmts | ;
    def visitMany_elseif_stmts(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.elseif_stmt().accept(self)] + ctx.many_elseif_stmts().accept(self)
        else:
            return []

    # elseif_stmt: ELSEIF expr THEN stmt_lst;
    def visitElseif_stmt(self, ctx):
        stmts = ctx.stmt_lst().accept(self)
        vardecl_lst = stmts[0]
        stmt_lst = stmts[1]

        return (ctx.expr().accept(self), vardecl_lst, stmt_lst)

    # else_stmt: ELSE stmt_lst | ;
    def visitElse_stmt(self, ctx):
        if ctx.getChildCount() == 2:
            stmts = ctx.stmt_lst().accept(self)
            vardecl_lst = stmts[0]
            stmt_lst = stmts[1]

            return (vardecl_lst, stmt_lst)
        else:
            return ([], [])

    # for_stmt: FOR LP ID ASSIGN expr COMMA expr COMMA expr RP DO stmt_lst ENDFOR DOT;
    def visitFor_stmt(self, ctx):
        stmts = ctx.stmt_lst().accept(self)
        vardecl_lst = stmts[0]
        stmt_lst = stmts[1]

        return For(Id(ctx.ID().getText()), ctx.expr(0).accept(self), ctx.expr(1).accept(self), ctx.expr(2).accept(self), (vardecl_lst, stmt_lst))

    # while_stmt: WHILE expr DO stmt_lst ENDWHILE DOT;
    def visitWhile_stmt(self, ctx):
        stmts = ctx.stmt_lst().accept(self)
        vardecl_lst = stmts[0]
        stmt_lst = stmts[1]

        return While(ctx.expr().accept(self), (vardecl_lst, stmt_lst))

    # do_while_stmt: DO stmt_lst WHILE expr ENDDO DOT;
    def visitDo_while_stmt(self, ctx):
        stmts = ctx.stmt_lst().accept(self)
        vardecl_lst = stmts[0]
        stmt_lst = stmts[1]

        return Dowhile((vardecl_lst, stmt_lst), ctx.expr().accept(self))

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx):
        return Break()

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx):
        return Continue()

    # call_stmt: ID LP expr_lst RP SEMI;
    def visitCall_stmt(self, ctx):
        return CallStmt(Id(ctx.ID().getText()), ctx.expr_lst().accept(self))

    # expr_lst: expr many_exprs | ;
    def visitExpr_lst(self, ctx):
        if ctx.getChildCount() == 2:
            return [ctx.expr().accept(self)] + ctx.many_exprs().accept(self)
        else:
            return []

    # many_exprs: COMMA expr many_exprs | ;
    def visitMany_exprs(self, ctx):
        if ctx.getChildCount() == 3:
            return [ctx.expr().accept(self)] + ctx.many_exprs().accept(self)
        else:
            return []

    # return_stmt: RETURN SEMI | RETURN expr SEMI;
    def visitReturn_stmt(self, ctx):
        if ctx.getChildCount() == 2:
            return Return(None)
        else:
            return Return(ctx.expr().accept(self))
