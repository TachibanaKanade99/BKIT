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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\23\2\2\5\6\7\66\2\2\6\7\7:\2\2\7")
        buf.write("\b\79\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
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
                      "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

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
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

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
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





