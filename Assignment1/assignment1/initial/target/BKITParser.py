# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\36\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("\34\n\5\3\5\2\2\6\2\4\6\b\2\2\2\32\2\n\3\2\2\2\4\20\3")
        buf.write("\2\2\2\6\24\3\2\2\2\b\33\3\2\2\2\n\13\7\23\2\2\13\f\7")
        buf.write("\66\2\2\f\r\7:\2\2\r\16\79\2\2\16\17\7\2\2\3\17\3\3\2")
        buf.write("\2\2\20\21\7\62\2\2\21\22\5\6\4\2\22\23\7\63\2\2\23\5")
        buf.write("\3\2\2\2\24\25\7A\2\2\25\26\5\b\5\2\26\7\3\2\2\2\27\30")
        buf.write("\78\2\2\30\31\7A\2\2\31\34\5\b\5\2\32\34\3\2\2\2\33\27")
        buf.write("\3\2\2\2\33\32\3\2\2\2\34\t\3\2\2\2\3\33")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'='", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "':'", "'.'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS", 
                      "FLOAT_PLUS", "MINUS", "FLOAT_MINUS", "MUL", "FLOAT_MUL", 
                      "DIV", "FLOAT_DIV", "MOD", "NOT", "AND", "OR", "EQ", 
                      "NOT_EQ", "LESS", "GREATER", "LESS_EQ", "GREATER_EQ", 
                      "FLOAT_NOT_EQ", "FLOAT_LESS", "FLOAT_GREATER", "FLOAT_LESS_EQ", 
                      "FLOAT_GREATER_EQ", "ASSIGN", "LP", "RP", "LB", "RB", 
                      "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "ID", 
                      "COMMENT", "WS", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
                      "STRING_LIT", "LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_array_lit = 1
    RULE_lit_list = 2
    RULE_many_lits = 3

    ruleNames =  [ "program", "array_lit", "lit_list", "many_lits" ]

    EOF = Token.EOF
    BODY=1
    BREAK=2
    CONTINUE=3
    DO=4
    ELSE=5
    ELSEIF=6
    ENDBODY=7
    ENDIF=8
    ENDFOR=9
    ENDWHILE=10
    FOR=11
    FUNCTION=12
    IF=13
    PARAMETER=14
    RETURN=15
    THEN=16
    VAR=17
    WHILE=18
    TRUE=19
    FALSE=20
    ENDDO=21
    PLUS=22
    FLOAT_PLUS=23
    MINUS=24
    FLOAT_MINUS=25
    MUL=26
    FLOAT_MUL=27
    DIV=28
    FLOAT_DIV=29
    MOD=30
    NOT=31
    AND=32
    OR=33
    EQ=34
    NOT_EQ=35
    LESS=36
    GREATER=37
    LESS_EQ=38
    GREATER_EQ=39
    FLOAT_NOT_EQ=40
    FLOAT_LESS=41
    FLOAT_GREATER=42
    FLOAT_LESS_EQ=43
    FLOAT_GREATER_EQ=44
    ASSIGN=45
    LP=46
    RP=47
    LB=48
    RB=49
    LSB=50
    RSB=51
    COLON=52
    DOT=53
    COMMA=54
    SEMI=55
    ID=56
    COMMENT=57
    WS=58
    INT_LIT=59
    FLOAT_LIT=60
    BOOL_LIT=61
    STRING_LIT=62
    LIT=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    UNTERMINATED_COMMENT=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(BKITParser.VAR)
            self.state = 9
            self.match(BKITParser.COLON)
            self.state = 10
            self.match(BKITParser.ID)
            self.state = 11
            self.match(BKITParser.SEMI)
            self.state = 12
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def lit_list(self):
            return self.getTypedRuleContext(BKITParser.Lit_listContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(BKITParser.LB)
            self.state = 15
            self.lit_list()
            self.state = 16
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT(self):
            return self.getToken(BKITParser.LIT, 0)

        def many_lits(self):
            return self.getTypedRuleContext(BKITParser.Many_litsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lit_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list" ):
                return visitor.visitLit_list(self)
            else:
                return visitor.visitChildren(self)




    def lit_list(self):

        localctx = BKITParser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lit_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(BKITParser.LIT)
            self.state = 19
            self.many_lits()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_litsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def LIT(self):
            return self.getToken(BKITParser.LIT, 0)

        def many_lits(self):
            return self.getTypedRuleContext(BKITParser.Many_litsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_lits

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_lits" ):
                return visitor.visitMany_lits(self)
            else:
                return visitor.visitChildren(self)




    def many_lits(self):

        localctx = BKITParser.Many_litsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_many_lits)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(BKITParser.COMMA)
                self.state = 22
                self.match(BKITParser.LIT)
                self.state = 23
                self.many_lits()
                pass
            elif token in [BKITParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





