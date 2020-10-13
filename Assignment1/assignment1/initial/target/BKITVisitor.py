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