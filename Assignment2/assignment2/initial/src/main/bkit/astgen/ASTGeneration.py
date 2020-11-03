from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    # program: many_declars EOF;
    def visitProgram(self, ctx):
        return ctx.many_declars().accept(self)

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
            print(variable[0], " ", variable[1], " ", variable[2])
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
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_lit():
            return BooleanLiteral(ctx.bool_lit().accept(self))
        else:
            return ArrayLiteral(ctx.array_lit().accept(self))

    # bool_lit: TRUE | FALSE;
    def visitBool_lit(self, ctx):
        if ctx.TRUE():
            return ctx.TRUE().getText()
        else:
            return ctx.FALSE().getText()

    # array_lit: LB lit_list RB;
    def visitArray_lit(self, ctx):
        return ctx.lit_list().accept(self)

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
        return []

    

