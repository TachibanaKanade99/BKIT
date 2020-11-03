from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    # program: many_declars EOF;
    def visitProgram(self, ctx):
        return ctx.many_declars().accept(self)

    # many_declars: global_var_declar_lst func_declar_lst;
    

    

