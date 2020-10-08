# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\7\6+\n\6\f\6\16\6.\13\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\6\7\66\n\7\r\7\16\7\67\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3,\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\3\2\5\3\2c|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\2E\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\36\3\2")
        buf.write("\2\2\7 \3\2\2\2\t\"\3\2\2\2\13&\3\2\2\2\r\65\3\2\2\2\17")
        buf.write(";\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27\33\t")
        buf.write("\2\2\2\30\32\t\3\2\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\4\3\2\2\2\35\33\3\2\2\2\36\37")
        buf.write("\7=\2\2\37\6\3\2\2\2 !\7<\2\2!\b\3\2\2\2\"#\7X\2\2#$\7")
        buf.write("c\2\2$%\7t\2\2%\n\3\2\2\2&\'\7,\2\2\'(\7,\2\2(,\3\2\2")
        buf.write("\2)+\13\2\2\2*)\3\2\2\2+.\3\2\2\2,-\3\2\2\2,*\3\2\2\2")
        buf.write("-/\3\2\2\2.,\3\2\2\2/\60\7,\2\2\60\61\7,\2\2\61\62\3\2")
        buf.write("\2\2\62\63\b\6\2\2\63\f\3\2\2\2\64\66\t\4\2\2\65\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2")
        buf.write("\29:\b\7\2\2:\16\3\2\2\2;<\13\2\2\2<\20\3\2\2\2=>\13\2")
        buf.write("\2\2>\22\3\2\2\2?@\13\2\2\2@\24\3\2\2\2AB\13\2\2\2B\26")
        buf.write("\3\2\2\2\6\2\33,\67\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    COMMENT = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "COMMENT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


