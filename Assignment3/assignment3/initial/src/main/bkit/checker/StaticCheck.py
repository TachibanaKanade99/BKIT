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
        func_lst = []

        for x in ast.decl:
            decl = x.accept(self, decl_lst)
            decl_lst[0].append(decl)

            # Add function to func_lst:
            if decl.opKind == "function":
                func_lst.append(decl)

        # Check if it exists function main:
        isMain = list(filter(lambda x: x.opKind == "function" and x.opName == "main", decl_lst[0]))
        if len(isMain) == 0:
            raise NoEntryPoint()

        # revisit function body:
        for y in ast.decl:
            for func in func_lst:
                if isinstance(y, FuncDecl) and y.name.name == func.opName:
                        y.accept(self, decl_lst+["recheck"])
            
        # check only:
        # for z in decl_lst[0]:
        #     print(z.opName, " ", z.opType)

    def visitVarDecl(self, ast, param):
        decl_lst = param
        var_name = ast.variable.accept(self, decl_lst+["vardecl"])
        var_dimension_lst = ast.varDimen
        var_type = None
        var_kind = None

        # Check redeclared variable:
        for decl in decl_lst[0]:
            if var_name == decl.opName:
                if param[-1] is not None and param[-1] == 'param':
                    raise Redeclared(Parameter(), var_name)
                raise Redeclared(Variable(), var_name)
        
        # Infer type for variable:
        if ast.varInit is not None:
            var_value = ast.varInit.accept(self, decl_lst)
            
            # array type:
            if type(var_value.opType) == list:
                var_kind = "composite_variable"
                if len(var_dimension_lst) > 0:
                    var_type = [type(var_dimension_lst[0]), var_value.opType]
                else:
                    var_type = [None, var_value.opType]
            else:
                var_kind = "scalar_variable"
                var_type = var_value.opType

        # print(var_name, var_type)
        return Operand(var_name, var_type, var_kind, [])

    def visitFuncDecl(self, ast, param):
        decl_lst = param
        isVisit = None

        if decl_lst[-1] == "recheck":
            isVisit = decl_lst.pop()
        
        if isVisit is None:
            func_name = ast.name.accept(self, decl_lst+["funcdecl"])
            func_type = None

            # Check redeclared function
            for decl in decl_lst[0]:
                if func_name == decl.opName:
                    raise Redeclared(Function(), func_name)

            # visit param:
            param_lst = []
            if len(ast.param) > 0:
                for x in ast.param:
                    param_decl = x.accept(self, [param_lst, "param"])
                    param_lst.append(param_decl)
            
            return Operand(func_name, func_type, "function", param_lst)
        
        else:
            func = ast.name.accept(self, decl_lst+["func_call"])
            # Add function name to global scope:
            # Use new list:
            new_decl_lst = decl_lst.copy()
            # new_decl_lst[0].append(Operand(func_name, func_type, "function", param_lst))

            # visit body[0]:
            # copy a new_lst
            local_lst = func.param_lst.copy()

            for y in ast.body[0]:
                decl = y.accept(self, [local_lst])
                local_lst.append(decl)

            # visit body[1]:
            new_decl_lst = [local_lst] + new_decl_lst
            
            for z in ast.body[1]:
                # check if stmt is Return:
                # if isinstance(z, Return):
                #     stmt = z.accept(self, new_decl_lst+[func])
                # else:
                #     stmt = z.accept(self, new_decl_lst)
                stmt = z.accept(self, new_decl_lst+[[func]])

    def visitBinaryOp(self, ast, param):
        decl_lst = param
        op = ast.op
        left_expr = ast.left.accept(self, decl_lst)
        right_expr = ast.right.accept(self, decl_lst)
        param_lst = []
        # print(left_expr.opName, left_expr.opType)
        # print(right_expr.opName, right_expr.opType)

        # Get all param of left_expr:
        if len(left_expr.param_lst) > 0:
            for param in left_expr.param_lst:
                param_lst.append(param)
        # Get all param of right_expr:
        if len(right_expr.param_lst) > 0:
            for param in right_expr.param_lst:
                param_lst.append(param)

        # Operand name:
        operand_name = left_expr.opName + op + right_expr.opName

        # Test param_lst returned:
        # for param in param_lst:
        #     print(param.opName, param.opType)

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
            return Operand(operand_name, int, "bin_op", param_lst)

        if op == '+.' or op == '-.' or op == '*.' or op == '\.':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = float
                right_expr.opType = float
            if left_expr.opType is not float or right_expr.opType is not float:
                raise TypeMismatchInExpression(ast)    
            return Operand(operand_name, float, "bin_op", param_lst)

        if op == '!' or op == '&&' or op == '||':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = bool
                right_expr.opType = bool
            if left_expr.opType is not bool or right_expr.opType is not bool:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, bool, "bin_op", param_lst)

        if op == '==' or op == '!=' or op == '>' or op == '<' or op == '>=' or op == '<=':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = int
                right_expr.opType = int
            if left_expr.opType is not int or right_expr.opType is not int:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, bool, "bin_op", param_lst)

        if op == '=/=' or op == '<.' or op == '>.' or op == '<=.' or op == '>=.':
            if left_expr.opType is None and right_expr.opType is None:
                left_expr.opType = float
                right_expr.opType = float
            if left_expr.opType is not float or right_expr.opType is not float:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, bool, "bin_op", param_lst)

    def visitUnaryOp(self, ast, param):
        decl_lst = param
        op = ast.op
        expr = ast.body.accept(self, decl_lst)
        param_lst = []

        # Get all param of expr:
        if len(expr.param_lst) > 0:
            for param in expr.param_lst:
                param_lst.append(param)

        # Operand name:
        operand_name = op + expr.opName

        if op == '-':
            if expr.opType is None:
                expr.opType = int
            if expr.opType is not int:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, int, "un_op", param_lst)

        if op == '-.':
            if expr.opType is None:
                expr.opType = float
            if expr.opType is not float:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, float, "un_op", param_lst)

        if op == '!':
            if expr.opType is None:
                expr.opType = bool
            if expr.opType is not bool:
                raise TypeMismatchInExpression(ast)
            return Operand(operand_name, bool, "un_op", param_lst)

    def visitArrayCell(self, ast, param):
        decl_lst = param
        arr = ast.arr.accept(self, decl_lst)
        index_lst = []

        if arr.opType != "array_type":
            if arr.opType is None:
                arr.opType = "array_type"
            else:
                raise TypeMismatchInExpression(ast)

        # visit index_lst:
        for x in ast.idx:
            index = x.accept(self, decl_lst)
            index_lst.append(index)

        # check if each index has type is int:
        for index in index_lst:
            if index.opType != int:
                raise TypeMismatchInExpression(ast)

        return Operand(arr.opName, arr.opType, "array_cell", index_lst)

    
    def visitCallExpr(self, ast, param):
        decl_lst = param
        func = ast.method.accept(self, decl_lst+["func_call"])

        # visit arguments in func_call:
        arg_lst = []
        for x in ast.param:
            arg = x.accept(self, decl_lst)
            arg_lst.append(arg)      

        # check number of argument:
        if len(func.param_lst) != len(arg_lst):
            raise TypeMismatchInExpression(ast)

        # check type of arguments:
        for i in range(len(arg_lst)):
            if arg_lst[i].opType is None:
                if func.param_lst[i].opType is not None:
                    arg_lst[i].opType = func.param_lst[i].opType
            else:
                if func.param_lst[i].opType is None:
                    func.param_lst[i].opType = arg_lst[i].opType
                else:
                    if arg_lst[i].opType != func.param_lst[i].opType:
                        raise TypeMismatchInExpression(ast)
        
        func.param_lst = func.param_lst + arg_lst
        return func

    def visitCallStmt(self, ast, param):
        decl_lst = param
        func = ast.method.accept(self, decl_lst+["func_call"])
        func.opKind = "call_stmt"

        # check if type of function is inferred:
        if func.opType is not None:
            raise TypeMismatchInStatement(ast)
        else:
            func.opType = "void_type"

        # visit arguments in call stmt:
        arg_lst = []
        for x in ast.param:
            arg = x.accept(self, decl_lst)
            arg_lst.append(arg)
        
        # Test only:
        # for arg in arg_lst:
        #     print(arg.opName)

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
                        raise TypeMismatchInStatement(ast)

    def visitAssign(self, ast, param):
        decl_lst = param
        lhs = ast.lhs.accept(self, decl_lst)
        rhs = ast.rhs.accept(self, decl_lst)
        # print(lhs.opType, rhs.opType)

        # Check type of lhs and rhs:
        if lhs.opType is None and rhs.opType is None:
            raise TypeCannotBeInferred(ast)
        if lhs.opType is not None:
            if lhs.opType == "void_type":
                raise TypeMismatchInStatement(ast)
            if rhs.opType is None:
                rhs.opType = lhs.opType
        if lhs.opType is None and rhs.opType is not None:
            lhs.opType = rhs.opType

        if lhs.opType != rhs.opType:
            raise TypeMismatchInStatement(ast)
        else:
            # Check all type inferred in lhs:
            if len(lhs.param_lst) > 0:
                for param in lhs.param_lst:
                    if param.opType is None:
                        raise TypeCannotBeInferred(ast)

            # Check all type inferred in rhs:
            if len(rhs.param_lst) > 0:
                for param in rhs.param_lst:
                    if param.opType is None:
                        raise TypeCannotBeInferred(ast)

    def visitIf(self, ast, param):
        decl_lst = param
        ifthen_stmt_lst = ast.ifthenStmt
        else_stmt = ast.elseStmt

        # visit if and elseif stmts:
        for ifthen_stmt in ifthen_stmt_lst:
            # visit expression:
            expr = ifthen_stmt[0].accept(self, decl_lst)

            if expr.opType is None:
                expr.opType = bool

            if expr.opType != bool:
                raise TypeMismatchInStatement(ast)

            # visit var_decl_lst:
            local_lst = []
            for x in ifthen_stmt[1]:
                decl = x.accept(self, [local_lst])
                local_lst.append(decl)
            
            # visit stmt_lst:
            new_decl_lst = decl_lst.copy()
            new_decl_lst = [local_lst] + new_decl_lst

            for y in ifthen_stmt[2]:
                stmt = y.accept(self, new_decl_lst)
        
        # visit else stmt:

        # visit var_decl_lst:
        local_lst = []
        for x in else_stmt[0]:
            decl = x.accept(self, [local_lst])
            local_lst.append(decl)
        
        # visit stmt_lst:
        new_decl_lst = decl_lst.copy()
        new_decl_lst = [local_lst] + new_decl_lst
        for y in else_stmt[1]:
            stmt = y.accept(self, new_decl_lst)

    def visitFor(self, ast, param):
        decl_lst = param
        index = ast.idx1.accept(self, decl_lst)
        expr_1 = ast.expr1.accept(self, decl_lst)
        expr_2 = ast.expr2.accept(self, decl_lst)
        expr_3 = ast.expr3.accept(self, decl_lst)
        var_decl_lst = ast.loop[0]
        stmt_lst = ast.loop[1]

        # infer type for index, expr_1,2,3 if their type is None:
        if index.opType is None:
            index.opType = int
        if expr_1.opType is None:
            expr_1.opType = int
        if expr_2.opType is None:
            expr_2.opType = bool
        if expr_3.opType is None:
            expr_3.opType = int

        # check type of index:        
        if index.opType != int:
            raise TypeMismatchInStatement(ast)
        
        # check type of expression 1:
        if expr_1.opType != int:
            raise TypeMismatchInStatement(ast)
        
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
        if expr.opType is None:
            expr.opType = bool

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
        if expr.opType is None:
            expr.opType = bool

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
        func = param[-1][0]
        expr = ast.expr.accept(self, decl_lst)

        if func.opType is not None:
            if func.opType == "void_type" and expr is not None:
                raise TypeMismatchInStatement(ast)
            if expr.opType != func.opType:
                raise TypeMismatchInStatement(ast)
        else:
            if expr.opType is None:
                raise TypeCannotBeInferred(ast)
            else:
                func.opType = expr.opType
        
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
        return Operand(str(ast.value), int, "literal", [])
    
    def visitFloatLiteral(self, ast, param):
        return Operand(str(ast.value), float, "literal", [])
    
    def visitBooleanLiteral(self, ast, param):
        return Operand(str(ast.value), bool, "literal", [])
    
    def visitStringLiteral(self, ast, param):
        return Operand(str(ast.value), str, "literal", [])

    def visitArrayLiteral(self, ast, param):
        decl_lst = param
        index_type = None
        elem_type = None
        lit_lst = []
        
        for x in ast.value:
            lit = x.accept(self, decl_lst)
            lit_lst.append(lit)
        elem_type = lit_lst[0].opType

        return Operand(None, [index_type, elem_type], "literal", [])
    





        
