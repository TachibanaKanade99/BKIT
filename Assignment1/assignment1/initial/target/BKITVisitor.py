# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_declars.
    def visitMany_declars(self, ctx:BKITParser.Many_declarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#global_var_declar_lst.
    def visitGlobal_var_declar_lst(self, ctx:BKITParser.Global_var_declar_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_var_decl.
    def visitMany_var_decl(self, ctx:BKITParser.Many_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_lst.
    def visitVar_lst(self, ctx:BKITParser.Var_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_var.
    def visitMany_var(self, ctx:BKITParser.Many_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_var.
    def visitComposite_var(self, ctx:BKITParser.Composite_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension_lst.
    def visitDimension_lst(self, ctx:BKITParser.Dimension_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_dimension.
    def visitMany_dimension(self, ctx:BKITParser.Many_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declar_lst.
    def visitFunc_declar_lst(self, ctx:BKITParser.Func_declar_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_func_decl.
    def visitMany_func_decl(self, ctx:BKITParser.Many_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_name.
    def visitFunc_name(self, ctx:BKITParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_param.
    def visitFunc_param(self, ctx:BKITParser.Func_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_lst.
    def visitParam_lst(self, ctx:BKITParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_params.
    def visitMany_params(self, ctx:BKITParser.Many_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_lst.
    def visitStmt_lst(self, ctx:BKITParser.Stmt_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_stmts.
    def visitMany_stmts(self, ctx:BKITParser.Many_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main_func.
    def visitMain_func(self, ctx:BKITParser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument_lst.
    def visitArgument_lst(self, ctx:BKITParser.Argument_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_arguments.
    def visitMany_arguments(self, ctx:BKITParser.Many_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument.
    def visitArgument(self, ctx:BKITParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_1.
    def visitOperand_1(self, ctx:BKITParser.Operand_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_2.
    def visitOperand_2(self, ctx:BKITParser.Operand_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_3.
    def visitOperand_3(self, ctx:BKITParser.Operand_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_4.
    def visitOperand_4(self, ctx:BKITParser.Operand_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_5.
    def visitOperand_5(self, ctx:BKITParser.Operand_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_6.
    def visitOperand_6(self, ctx:BKITParser.Operand_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand_7.
    def visitOperand_7(self, ctx:BKITParser.Operand_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lit_list.
    def visitLit_list(self, ctx:BKITParser.Lit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_lits.
    def visitMany_lits(self, ctx:BKITParser.Many_litsContext):
        return self.visitChildren(ctx)



del BKITParser