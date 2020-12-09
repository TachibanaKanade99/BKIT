# ID: 1752595

"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

# Operand:
class Operand():
    def __init__(self, opName=None, opType=None, opKind=None, param_lst=None):
        self.opName = opName
        self.opType = opType
        self.opKind = opKind
        self.param_lst = param_lst # use for function only:


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType())),
            Symbol("float_to_int",MType([IntType()],FloatType())),
            Symbol("int_of_string",MType([StringType()],IntType())),
            Symbol("string_of_int",MType([IntType()],StringType())),
            Symbol("float_of_string",MType([StringType()],FloatType())),
            Symbol("string_of_float",MType([FloatType()],StringType())),
            Symbol("bool_of_string",MType([StringType()],BoolType())),
            Symbol("string_of_bool",MType([BoolType()],StringType())),
            Symbol("read",MType([],StringType())),
            Symbol("printLn",MType([],VoidType())),
            Symbol("print",MType([StringType()],VoidType())),
            Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, param):
        decl_lst = [[]]

        for x in ast.decl:
            decl = x.accept(self, decl_lst)
            decl_lst[0].append(decl)

        # Check if it exists function main:
        isMain = list(filter(lambda x: x.opKind == "function" and x.opName == "main", decl_lst[0]))
        if len(isMain) == 0:
            raise NoEntryPoint()        

        # check only:
        for y in decl_lst[0]:
            print(y.opName, " ", y.opType)

    def visitVarDecl(self, ast, param):
        decl_lst = param
        var_name = ast.variable.accept(self, decl_lst+["vardecl"])
        # var_dimension = ast.varDimen.accept(self, decl_lst)

        # Check redeclared variable:
        for decl in decl_lst[0]:
            if var_name == decl.opName:

                if param[-1] is not None:
                    if param[-1] == 'param':
                        raise Redeclared(Parameter(), var_name)
                
                raise Redeclared(Variable(), var_name)
        
        # Infer type for variable:
        if ast.varInit is not None:
            var_value = ast.varInit.accept(self, decl_lst)
            var_type = var_value.opType
        else:
            var_type = None

        return Operand(var_name, var_type, "variable", None)

    def visitFuncDecl(self, ast, param):
        decl_lst = param
        func_name = ast.name.accept(self, decl_lst+["funcdecl"])
        func_type = None
        param_lst = []

        # Check redeclared function
        for decl in decl_lst[0]:
            if func_name == decl.opName:
                raise Redeclared(Function(), func_name)

        # Add function name to global scope:
        # Use new list:
        new_decl_lst = decl_lst.copy()
        new_decl_lst[0].append(Operand(func_name, func_type, "function", param_lst))

        # visit param:
        if len(ast.param) > 0:
            for x in ast.param:
                param_decl = x.accept(self, [param_lst, "param"])
                param_lst.append(param_decl)

        # visit body[0]:
        # copy a new_lst
        local_lst = param_lst.copy()

        for y in ast.body[0]:
            decl = y.accept(self, [local_lst])
            local_lst.append(decl)

        # visit body[1]:
        new_decl_lst = [local_lst] + new_decl_lst

        for z in ast.body[1]:
            # check if stmt is Return:
            if isinstance(z, Return):
                stmt = z.accept(self, new_decl_lst+[func_type])
            else:
                stmt = z.accept(self, new_decl_lst)

        return Operand(func_name, func_type, "function", param_lst)

    def visitBinaryOp(self, ast, param):
        decl_lst = param
        op = ast.op
        left_expr = ast.left.accept(self, decl_lst)
        right_expr = ast.right.accept(self, decl_lst)

        if left_expr.opType is None and right_expr.opType is not None:
            left_expr.opType = right_expr.opType
        if left_expr.opType is not None and right_expr.opType is None:
            right_expr.opType = left_expr.opType

        if op == '+' or op == '-' or op == '*' or op == '\\' or op == '%':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = int
                right_expr.opType = int
            if left_expr.opType is not int or right_expr.opType is not int:
                raise TypeMismatchInExpression(ast)
            return Operand(None, int, "bin_op", None)

        if op == '+.' or op == '-.' or op == '*.' or op == '\.':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = float
                right_expr.opType = float
            if left_expr.opType is not float or right_expr.opType is not float:
                raise TypeMismatchInExpression(ast)    
            return Operand(None, float, "bin_op", None)

        if op == '!' or op == '&&' or op == '||':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = bool
                right_expr.opType = bool
            if left_expr.opType is not bool or right_expr.opType is not bool:
                raise TypeMismatchInExpression(ast)
            return Operand(None, bool, "bin_op", None)

        if op == '==' or op == '!=' or op == '>' or op == '<' or op == '>=' or op == '<=':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = int
                right_expr.opType = int
            if left_expr.opType is not int or right_expr.opType is not int:
                raise TypeMismatchInExpression(ast)
            return Operand(None, bool, "bin_op", None)

        if op == '=/=' or op == '<.' or op == '>.' or op == '<=.' or op == '>=.':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = float
                right_expr.opType = float
            if left_expr.opType is not float or right_expr.opType is not float:
                raise TypeMismatchInExpression(ast)
            return Operand(None, float, "bin_op", None)

    def visitUnaryOp(self, ast, param):
        decl_lst = param
        op = ast.op
        expr = ast.body.accept(self, decl_lst)

        if op == '-':
            if expr.opType is None:
                expr.opType = int
            if expr.opType is not int:
                raise TypeMismatchInExpression(ast)
            return Operand(None, int, "un_op", None)

        if op == '-.':
            if expr.opType is None:
                expr.opType = float
            if expr.opType is not float:
                raise TypeMismatchInExpression(ast)
            return Operand(None, float, "un_op", None)

        if op == '!':
            if expr.opType is None:
                expr.opType = bool
            if expr.opType is not bool:
                raise TypeMismatchInExpression(ast)
            return Operand(None, bool, "un_op", None)

    def visitArrayCell(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        decl_lst = param
        func = ast.method.accept(self, decl_lst+["func_call"])
        func.opKind = "func_call"

        # visit arguments in func_call:
        arg_lst = []
        for x in ast.param:
            arg = x.accept(self, decl_lst)
            arg_lst.append(arg)

        if len(arg_lst) > 0:
            func.opType = arg_lst[0].opType

        # check number of argument:
        if len(func.param_lst) != len(arg_lst):
            raise TypeMismatchInExpression(ast)

        # check type of arguments:
        for i in range(len(arg_lst)):
            if arg_lst[i].opType is None and func.param_lst[i].opType is not None:
                arg_lst[i].opType = func.param_lst[i].opType
            else:
                if func.param_lst[i].opType is None:
                    func.param_lst[i].opType = arg_lst[i].opType
                else:
                    if arg_lst[i].opType != func.param_lst[i].opType:
                        arg_lst[i].opType = None

        return Operand(None, func.opType, "func_call", arg_lst)

    def visitCallStmt(self, ast, param):
        decl_lst = param
        func = ast.method.accept(self, decl_lst+["func_call"])
        func.opKind = "call_stmt"

        # check if type of function is inferred:
        if func.opType is not None:
            raise TypeCannotBeInferred(ast)
        else:
            func.opType = None

        # visit arguments in call stmt:
        arg_lst = []
        for x in ast.param:
            arg = x.accept(self, decl_lst)
            arg_lst.append(arg)
        
        # Test only:
        for arg in arg_lst:
            print(arg.opName)

        # check number of arguments:
        if len(func.param_lst) != len(arg_lst):
            raise TypeMismatchInStatement(ast)
            
        # check type of arguments:
        for i in range(len(arg_lst)):
            if arg_lst[i].opType is None:
                if func.param_lst[i].opType is None:
                    raise TypeCannotBeInferred(ast)
                else:
                    arg_lst[i].opType = func.param_lst[i].opType
            else:
                if func.param_lst[i].opType is None:
                    func.param_lst[i].opType = arg_lst[i].opType
                else:
                    if arg_lst[i].opType != func.param_lst[i].opType:
                        raise TypeCannotBeInferred(ast)
        

    def visitAssign(self, ast, param):
        decl_lst = param
        lhs = ast.lhs.accept(self, decl_lst)
        rhs = ast.rhs.accept(self, decl_lst)

        # Check type of lhs and rhs:
        if lhs.opType is None and rhs.opType is None:
            raise TypeCannotBeInferred(ast)
        elif lhs.opType is None and rhs.opType is not None:
            lhs.opType = rhs.opType
        elif lhs.opType is not None and rhs.opType is None:
            rhs.opType = lhs.opType
        elif lhs.opType != rhs.opType:
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, param):
        decl_lst = param
        ifthen_stmt_lst = ast.ifthenStmt
        else_stmt_lst = ast.elseStmt

        # visit if and elseif stmts:
        for ifthen_stmt in ifthen_stmt_lst:
            # visit expression:
            expr = ifthen_stmt[0].accept(self, decl_lst)

            if expr.opType != bool:
                if expr.opType is None:
                    expr.opType = bool
                else:
                    raise TypeMismatchInStatement(ast)

            # visit var_decls:
            local_lst = []
            for x in ifthen_stmt[1]:
                decl = x.accept(self, [local_lst])
                local_lst.append(decl)
            
            # visit stmts:
            new_decl_lst = decl_lst.copy()
            new_decl_lst = [local_lst] + new_decl_lst

            for y in ifthen_stmt[2]:
                stmt = y.accept(self, new_decl_lst)

    def visitFor(self, ast, param):
        decl_lst = param
        index = ast.idx1.accept(self, decl_lst)
        expr_1 = ast.expr1.accept(self, decl_lst)
        expr_2 = ast.expr2.accept(self, decl_lst)
        expr_3 = ast.expr3.accept(self, decl_lst)
        var_decl_lst = ast.loop[0]
        stmt_lst = ast.loop[1]

        # infer type for index if its type is None:
        if index.opType is None:
            index.opType = int

        # check type of index:        
        if index.opType != int:
            raise TypeMismatchInStatement(ast)
        
        # check type of expression 1:
        if expr_1.opType != int:
            raise TypeMismatchInStatement(ast)
            print("Hello World!")
        
        # check type of expression 2:
        if expr_2.opType != bool:
            raise TypeMismatchInStatement(ast)

        # check type of expression 3:
        if expr_3.opType != int:
            raise TypeMismatchInStatement(ast)

        # visit var_decls:
        local_lst = []
        for x in var_decl_lst:
            decl = x.accept(self, [local_lst])
            local_lst.append(decl)

        # visit stmts:
        new_decl_lst = decl_lst.copy()
        new_decl_lst = [local_lst] + new_decl_lst
        for y in stmt_lst:
            stmt = y.accept(self, new_decl_lst)
    
    def visitDowhile(self, ast, param):
        decl_lst = param
        var_decl_lst = ast.sl[0]
        stmt_lst = ast.sl[1]
        expr = ast.exp.accept(self, decl_lst)

        # visit var_decl_lst
        local_lst = []
        for x in var_decl_lst:
            decl = x.accept(self, [local_lst])
            local_lst.append(decl)

        # visit stmt_lst:
        new_decl_lst = decl_lst.copy()
        new_decl_lst = [local_lst] + new_decl_lst
        for y in stmt_lst:
            stmt = y.accept(self, new_decl_lst)

        # check type of expr:
        if expr.opType != bool:
            if expr.opType is None:
                expr.opType = bool
            else:
                raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, param):
        decl_lst = param
        expr = ast.exp.accept(self, decl_lst)
        var_decl_lst = ast.sl[0]
        stmt_lst = ast.sl[1]

        # check type of expr:
        if expr.opType != bool:
            if expr.opType is None:
                expr.opType = bool
            else:
                raise TypeMismatchInStatement(ast)

        # visit var_decl_lst
        local_lst = []
        for x in var_decl_lst:
            decl = x.accept(self, [local_lst])
            local_lst.append(decl)

        # visit stmt_lst:
        new_decl_lst = decl_lst.copy()
        new_decl_lst = [local_lst] + new_decl_lst
        for y in stmt_lst:
            stmt = y.accept(self, new_decl_lst)

    def visitReturn(self, ast, param):
        decl_lst = param[:-1]
        func_type = param[-1]
        expr = ast.expr.accept(self, decl_lst)

        if func_type is None:
            if expr is not None:
                raise TypeMismatchInStatement(ast)
        else:
            if expr.opType != func_type:
                raise TypeMismatchInStatement(ast)

    def visitId(self, ast, param):
        decl_lst = param
        flatten_decl_lst = []
        isFunc = None

        # Use for decl:
        if decl_lst[-1] == "vardecl" or decl_lst[-1] == "funcdecl":
            return ast.name

        # Check if id is function name:
        if decl_lst[-1] == "func_call":
            isFunc = decl_lst.pop()
        
        for sublst in decl_lst:
            for x in sublst:
                flatten_decl_lst.append(x)

        for decl in flatten_decl_lst:
            if ast.name == decl.opName:
                return decl

        if isFunc == "func_call":
            raise Undeclared(Function(), ast.name)
        else:
            raise Undeclared(Identifier(), ast.name)

    # Literal:
    def visitIntLiteral(self, ast, param):
        return Operand(None, int, "literal", None)
    
    def visitFloatLiteral(self, ast, param):
        return Operand(None, float, "literal", None)
    
    def visitBooleanLiteral(self, ast, param):
        return Operand(None, bool, "literal", None)
    
    def visitStringLiteral(self, ast, param):
        return Operand(None, str, "literal", None)

    def visitArrayLiteral(self, ast, param):
        decl_lst = param
        lit_lst = []
        for x in ast.value:
            lit = x.accept(self, decl_lst)
            lit_lst.append(lit)
        
        return Operand(None, "array_type", "literal", lit_lst)
    





        
