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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u014b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4`\n\4\3\5\3\5\3\5\3\5\5\5f\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\bt\n")
        buf.write("\b\3\t\3\t\5\tx\n\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\5\f\u0087\n\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u0091\n\16\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u0097\n\17\3\20\3\20\3\20\3\20\5\20\u009d\n\20\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00af\n\24\3\25\3\25\5")
        buf.write("\25\u00b3\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u00bf\n\27\3\30\3\30\3\30\3\30\5\30\u00c5")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u00d5\n\33\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u00db\n\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u00f8")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0100\n\37\f")
        buf.write("\37\16\37\u0103\13\37\3 \3 \3 \3 \3 \3 \7 \u010b\n \f")
        buf.write(" \16 \u010e\13 \3!\3!\3!\3!\3!\3!\7!\u0116\n!\f!\16!\u0119")
        buf.write("\13!\3\"\3\"\3\"\5\"\u011e\n\"\3#\3#\3#\5#\u0123\n#\3")
        buf.write("$\3$\3$\3$\3$\7$\u012a\n$\f$\16$\u012d\13$\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\5&\u013a\n&\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\5*\u0149\n*\3*\2\6<>@F+\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPR\2\13\3\2%&\3\2\'(\3\2)*\3\2,-\3\2./\3\2")
        buf.write("#$\3\2\31\34\3\2\35!\3\2\33\34\2\u013d\2T\3\2\2\2\4W\3")
        buf.write("\2\2\2\6_\3\2\2\2\be\3\2\2\2\ng\3\2\2\2\fk\3\2\2\2\16")
        buf.write("s\3\2\2\2\20w\3\2\2\2\22|\3\2\2\2\24\177\3\2\2\2\26\u0086")
        buf.write("\3\2\2\2\30\u0088\3\2\2\2\32\u0090\3\2\2\2\34\u0096\3")
        buf.write("\2\2\2\36\u0098\3\2\2\2 \u00a0\3\2\2\2\"\u00a2\3\2\2\2")
        buf.write("$\u00a6\3\2\2\2&\u00ae\3\2\2\2(\u00b2\3\2\2\2*\u00b4\3")
        buf.write("\2\2\2,\u00be\3\2\2\2.\u00c4\3\2\2\2\60\u00c6\3\2\2\2")
        buf.write("\62\u00cb\3\2\2\2\64\u00d4\3\2\2\2\66\u00da\3\2\2\28\u00dc")
        buf.write("\3\2\2\2:\u00f7\3\2\2\2<\u00f9\3\2\2\2>\u0104\3\2\2\2")
        buf.write("@\u010f\3\2\2\2B\u011d\3\2\2\2D\u0122\3\2\2\2F\u0124\3")
        buf.write("\2\2\2H\u012e\3\2\2\2J\u0139\3\2\2\2L\u013b\3\2\2\2N\u013d")
        buf.write("\3\2\2\2P\u0141\3\2\2\2R\u0148\3\2\2\2TU\5\4\3\2UV\7\2")
        buf.write("\2\3V\3\3\2\2\2WX\5\6\4\2XY\5\32\16\2YZ\5\60\31\2Z\5\3")
        buf.write("\2\2\2[\\\5\n\6\2\\]\5\b\5\2]`\3\2\2\2^`\3\2\2\2_[\3\2")
        buf.write("\2\2_^\3\2\2\2`\7\3\2\2\2ab\5\n\6\2bc\5\b\5\2cf\3\2\2")
        buf.write("\2df\3\2\2\2ea\3\2\2\2ed\3\2\2\2f\t\3\2\2\2gh\7\24\2\2")
        buf.write("hi\7\67\2\2ij\5\f\7\2j\13\3\2\2\2kl\5\20\t\2lm\5\16\b")
        buf.write("\2m\r\3\2\2\2no\79\2\2op\5\20\t\2pq\5\16\b\2qt\3\2\2\2")
        buf.write("rt\3\2\2\2sn\3\2\2\2sr\3\2\2\2t\17\3\2\2\2ux\7;\2\2vx")
        buf.write("\5\22\n\2wu\3\2\2\2wv\3\2\2\2xy\3\2\2\2yz\7\60\2\2z{\7")
        buf.write("B\2\2{\21\3\2\2\2|}\7;\2\2}~\5\24\13\2~\23\3\2\2\2\177")
        buf.write("\u0080\5\30\r\2\u0080\u0081\5\26\f\2\u0081\25\3\2\2\2")
        buf.write("\u0082\u0083\5\30\r\2\u0083\u0084\5\26\f\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0082\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\27\3\2\2\2\u0088\u0089\7\65\2\2\u0089")
        buf.write("\u008a\7>\2\2\u008a\u008b\7\66\2\2\u008b\31\3\2\2\2\u008c")
        buf.write("\u008d\5\36\20\2\u008d\u008e\5\34\17\2\u008e\u0091\3\2")
        buf.write("\2\2\u008f\u0091\3\2\2\2\u0090\u008c\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\33\3\2\2\2\u0092\u0093\5\36\20\2\u0093")
        buf.write("\u0094\5\34\17\2\u0094\u0097\3\2\2\2\u0095\u0097\3\2\2")
        buf.write("\2\u0096\u0092\3\2\2\2\u0096\u0095\3\2\2\2\u0097\35\3")
        buf.write("\2\2\2\u0098\u0099\7\17\2\2\u0099\u009a\7\67\2\2\u009a")
        buf.write("\u009c\5 \21\2\u009b\u009d\5\"\22\2\u009c\u009b\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f")
        buf.write("\5*\26\2\u009f\37\3\2\2\2\u00a0\u00a1\7;\2\2\u00a1!\3")
        buf.write("\2\2\2\u00a2\u00a3\7\21\2\2\u00a3\u00a4\7\67\2\2\u00a4")
        buf.write("\u00a5\5$\23\2\u00a5#\3\2\2\2\u00a6\u00a7\5(\25\2\u00a7")
        buf.write("\u00a8\5&\24\2\u00a8%\3\2\2\2\u00a9\u00aa\79\2\2\u00aa")
        buf.write("\u00ab\5(\25\2\u00ab\u00ac\5&\24\2\u00ac\u00af\3\2\2\2")
        buf.write("\u00ad\u00af\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae\u00ad\3")
        buf.write("\2\2\2\u00af\'\3\2\2\2\u00b0\u00b3\7;\2\2\u00b1\u00b3")
        buf.write("\5\22\n\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write(")\3\2\2\2\u00b4\u00b5\7\4\2\2\u00b5\u00b6\7\67\2\2\u00b6")
        buf.write("\u00b7\5,\27\2\u00b7\u00b8\7\n\2\2\u00b8\u00b9\78\2\2")
        buf.write("\u00b9+\3\2\2\2\u00ba\u00bb\5L\'\2\u00bb\u00bc\5.\30\2")
        buf.write("\u00bc\u00bf\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00ba\3")
        buf.write("\2\2\2\u00be\u00bd\3\2\2\2\u00bf-\3\2\2\2\u00c0\u00c1")
        buf.write("\5L\'\2\u00c1\u00c2\5.\30\2\u00c2\u00c5\3\2\2\2\u00c3")
        buf.write("\u00c5\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5/\3\2\2\2\u00c6\u00c7\7\17\2\2\u00c7\u00c8\7\67")
        buf.write("\2\2\u00c8\u00c9\7\3\2\2\u00c9\u00ca\5*\26\2\u00ca\61")
        buf.write("\3\2\2\2\u00cb\u00cc\7;\2\2\u00cc\u00cd\7\61\2\2\u00cd")
        buf.write("\u00ce\5\64\33\2\u00ce\u00cf\7\62\2\2\u00cf\63\3\2\2\2")
        buf.write("\u00d0\u00d1\58\35\2\u00d1\u00d2\5\66\34\2\u00d2\u00d5")
        buf.write("\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\65\3\2\2\2\u00d6\u00d7\58\35\2\u00d7")
        buf.write("\u00d8\5\66\34\2\u00d8\u00db\3\2\2\2\u00d9\u00db\3\2\2")
        buf.write("\2\u00da\u00d6\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\67\3")
        buf.write("\2\2\2\u00dc\u00dd\13\2\2\2\u00dd9\3\2\2\2\u00de\u00df")
        buf.write("\5<\37\2\u00df\u00e0\t\2\2\2\u00e0\u00e1\5<\37\2\u00e1")
        buf.write("\u00f8\3\2\2\2\u00e2\u00e3\5<\37\2\u00e3\u00e4\t\3\2\2")
        buf.write("\u00e4\u00e5\5<\37\2\u00e5\u00f8\3\2\2\2\u00e6\u00e7\5")
        buf.write("<\37\2\u00e7\u00e8\t\4\2\2\u00e8\u00e9\5<\37\2\u00e9\u00f8")
        buf.write("\3\2\2\2\u00ea\u00eb\5<\37\2\u00eb\u00ec\7+\2\2\u00ec")
        buf.write("\u00ed\5<\37\2\u00ed\u00f8\3\2\2\2\u00ee\u00ef\5<\37\2")
        buf.write("\u00ef\u00f0\t\5\2\2\u00f0\u00f1\5<\37\2\u00f1\u00f8\3")
        buf.write("\2\2\2\u00f2\u00f3\5<\37\2\u00f3\u00f4\t\6\2\2\u00f4\u00f5")
        buf.write("\5<\37\2\u00f5\u00f8\3\2\2\2\u00f6\u00f8\5<\37\2\u00f7")
        buf.write("\u00de\3\2\2\2\u00f7\u00e2\3\2\2\2\u00f7\u00e6\3\2\2\2")
        buf.write("\u00f7\u00ea\3\2\2\2\u00f7\u00ee\3\2\2\2\u00f7\u00f2\3")
        buf.write("\2\2\2\u00f7\u00f6\3\2\2\2\u00f8;\3\2\2\2\u00f9\u00fa")
        buf.write("\b\37\1\2\u00fa\u00fb\5> \2\u00fb\u0101\3\2\2\2\u00fc")
        buf.write("\u00fd\f\4\2\2\u00fd\u00fe\t\7\2\2\u00fe\u0100\5> \2\u00ff")
        buf.write("\u00fc\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102=\3\2\2\2\u0103\u0101\3\2\2")
        buf.write("\2\u0104\u0105\b \1\2\u0105\u0106\5@!\2\u0106\u010c\3")
        buf.write("\2\2\2\u0107\u0108\f\4\2\2\u0108\u0109\t\b\2\2\u0109\u010b")
        buf.write("\5@!\2\u010a\u0107\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d?\3\2\2\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0110\b!\1\2\u0110\u0111\5B\"\2\u0111\u0117")
        buf.write("\3\2\2\2\u0112\u0113\f\4\2\2\u0113\u0114\t\t\2\2\u0114")
        buf.write("\u0116\5B\"\2\u0115\u0112\3\2\2\2\u0116\u0119\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118A\3\2\2")
        buf.write("\2\u0119\u0117\3\2\2\2\u011a\u011b\7\"\2\2\u011b\u011e")
        buf.write("\5B\"\2\u011c\u011e\5D#\2\u011d\u011a\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011eC\3\2\2\2\u011f\u0120\t\n\2\2\u0120\u0123")
        buf.write("\5D#\2\u0121\u0123\5F$\2\u0122\u011f\3\2\2\2\u0122\u0121")
        buf.write("\3\2\2\2\u0123E\3\2\2\2\u0124\u0125\b$\1\2\u0125\u0126")
        buf.write("\5H%\2\u0126\u012b\3\2\2\2\u0127\u0128\f\4\2\2\u0128\u012a")
        buf.write("\5J&\2\u0129\u0127\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012cG\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012fI\3\2\2\2\u0130\u0131")
        buf.write("\7\65\2\2\u0131\u0132\5F$\2\u0132\u0133\7\66\2\2\u0133")
        buf.write("\u013a\3\2\2\2\u0134\u0135\7\65\2\2\u0135\u0136\5F$\2")
        buf.write("\u0136\u0137\7\66\2\2\u0137\u0138\5J&\2\u0138\u013a\3")
        buf.write("\2\2\2\u0139\u0130\3\2\2\2\u0139\u0134\3\2\2\2\u013aK")
        buf.write("\3\2\2\2\u013b\u013c\13\2\2\2\u013cM\3\2\2\2\u013d\u013e")
        buf.write("\7\63\2\2\u013e\u013f\5P)\2\u013f\u0140\7\64\2\2\u0140")
        buf.write("O\3\2\2\2\u0141\u0142\7B\2\2\u0142\u0143\5R*\2\u0143Q")
        buf.write("\3\2\2\2\u0144\u0145\79\2\2\u0145\u0146\7B\2\2\u0146\u0149")
        buf.write("\5R*\2\u0147\u0149\3\2\2\2\u0148\u0144\3\2\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149S\3\2\2\2\31_esw\u0086\u0090\u0096\u009c")
        buf.write("\u00ae\u00b2\u00be\u00c4\u00d4\u00da\u00f7\u0101\u010c")
        buf.write("\u0117\u011d\u0122\u012b\u0139\u0148")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", 
                     "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "PLUS", "FLOAT_PLUS", "MINUS", "FLOAT_MINUS", 
                      "MUL", "FLOAT_MUL", "DIV", "FLOAT_DIV", "MOD", "NOT", 
                      "AND", "OR", "EQ", "NOT_EQ", "LESS", "GREATER", "LESS_EQ", 
                      "GREATER_EQ", "FLOAT_NOT_EQ", "FLOAT_LESS", "FLOAT_GREATER", 
                      "FLOAT_LESS_EQ", "FLOAT_GREATER_EQ", "ASSIGN", "LP", 
                      "RP", "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", 
                      "SEMI", "ID", "COMMENT", "WS", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STRING_LIT", "LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_many_declars = 1
    RULE_global_var_declar_lst = 2
    RULE_many_var_decl = 3
    RULE_var_decl = 4
    RULE_var_lst = 5
    RULE_many_var = 6
    RULE_var = 7
    RULE_composite_var = 8
    RULE_dimension_lst = 9
    RULE_many_dimension = 10
    RULE_dimension = 11
    RULE_func_declar_lst = 12
    RULE_many_func_decl = 13
    RULE_func_decl = 14
    RULE_func_name = 15
    RULE_func_param = 16
    RULE_param_lst = 17
    RULE_many_params = 18
    RULE_param = 19
    RULE_body = 20
    RULE_stmt_lst = 21
    RULE_many_stmts = 22
    RULE_main_func = 23
    RULE_func_call = 24
    RULE_argument_lst = 25
    RULE_many_arguments = 26
    RULE_argument = 27
    RULE_expr = 28
    RULE_operand_1 = 29
    RULE_operand_2 = 30
    RULE_operand_3 = 31
    RULE_operand_4 = 32
    RULE_operand_5 = 33
    RULE_operand_6 = 34
    RULE_operand_7 = 35
    RULE_index_op = 36
    RULE_stmt = 37
    RULE_array_lit = 38
    RULE_lit_list = 39
    RULE_many_lits = 40

    ruleNames =  [ "program", "many_declars", "global_var_declar_lst", "many_var_decl", 
                   "var_decl", "var_lst", "many_var", "var", "composite_var", 
                   "dimension_lst", "many_dimension", "dimension", "func_declar_lst", 
                   "many_func_decl", "func_decl", "func_name", "func_param", 
                   "param_lst", "many_params", "param", "body", "stmt_lst", 
                   "many_stmts", "main_func", "func_call", "argument_lst", 
                   "many_arguments", "argument", "expr", "operand_1", "operand_2", 
                   "operand_3", "operand_4", "operand_5", "operand_6", "operand_7", 
                   "index_op", "stmt", "array_lit", "lit_list", "many_lits" ]

    EOF = Token.EOF
    T__0=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    PLUS=23
    FLOAT_PLUS=24
    MINUS=25
    FLOAT_MINUS=26
    MUL=27
    FLOAT_MUL=28
    DIV=29
    FLOAT_DIV=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQ=35
    NOT_EQ=36
    LESS=37
    GREATER=38
    LESS_EQ=39
    GREATER_EQ=40
    FLOAT_NOT_EQ=41
    FLOAT_LESS=42
    FLOAT_GREATER=43
    FLOAT_LESS_EQ=44
    FLOAT_GREATER_EQ=45
    ASSIGN=46
    LP=47
    RP=48
    LB=49
    RB=50
    LSB=51
    RSB=52
    COLON=53
    DOT=54
    COMMA=55
    SEMI=56
    ID=57
    COMMENT=58
    WS=59
    INT_LIT=60
    FLOAT_LIT=61
    BOOL_LIT=62
    STRING_LIT=63
    LIT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    UNTERMINATED_COMMENT=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_declars(self):
            return self.getTypedRuleContext(BKITParser.Many_declarsContext,0)


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
            self.state = 82
            self.many_declars()
            self.state = 83
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declarsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def global_var_declar_lst(self):
            return self.getTypedRuleContext(BKITParser.Global_var_declar_lstContext,0)


        def func_declar_lst(self):
            return self.getTypedRuleContext(BKITParser.Func_declar_lstContext,0)


        def main_func(self):
            return self.getTypedRuleContext(BKITParser.Main_funcContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_declars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_declars" ):
                return visitor.visitMany_declars(self)
            else:
                return visitor.visitChildren(self)




    def many_declars(self):

        localctx = BKITParser.Many_declarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.global_var_declar_lst()
            self.state = 86
            self.func_declar_lst()
            self.state = 87
            self.main_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_var_declar_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def many_var_decl(self):
            return self.getTypedRuleContext(BKITParser.Many_var_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_global_var_declar_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_var_declar_lst" ):
                return visitor.visitGlobal_var_declar_lst(self)
            else:
                return visitor.visitChildren(self)




    def global_var_declar_lst(self):

        localctx = BKITParser.Global_var_declar_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_global_var_declar_lst)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.var_decl()
                self.state = 90
                self.many_var_decl()
                pass
            elif token in [BKITParser.FUNCTION]:
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


    class Many_var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def many_var_decl(self):
            return self.getTypedRuleContext(BKITParser.Many_var_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_var_decl" ):
                return visitor.visitMany_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def many_var_decl(self):

        localctx = BKITParser.Many_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_many_var_decl)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.var_decl()
                self.state = 96
                self.many_var_decl()
                pass
            elif token in [BKITParser.FUNCTION]:
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


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_lst(self):
            return self.getTypedRuleContext(BKITParser.Var_lstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKITParser.VAR)
            self.state = 102
            self.match(BKITParser.COLON)
            self.state = 103
            self.var_lst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def many_var(self):
            return self.getTypedRuleContext(BKITParser.Many_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_lst" ):
                return visitor.visitVar_lst(self)
            else:
                return visitor.visitChildren(self)




    def var_lst(self):

        localctx = BKITParser.Var_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.var()
            self.state = 106
            self.many_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def many_var(self):
            return self.getTypedRuleContext(BKITParser.Many_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_var" ):
                return visitor.visitMany_var(self)
            else:
                return visitor.visitChildren(self)




    def many_var(self):

        localctx = BKITParser.Many_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_many_var)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(BKITParser.COMMA)
                self.state = 109
                self.var()
                self.state = 110
                self.many_var()
                pass
            elif token in [BKITParser.FUNCTION, BKITParser.VAR]:
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


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def LIT(self):
            return self.getToken(BKITParser.LIT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 116
                self.composite_var()
                pass


            self.state = 119
            self.match(BKITParser.ASSIGN)
            self.state = 120
            self.match(BKITParser.LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension_lst(self):
            return self.getTypedRuleContext(BKITParser.Dimension_lstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_var" ):
                return visitor.visitComposite_var(self)
            else:
                return visitor.visitChildren(self)




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_composite_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(BKITParser.ID)
            self.state = 123
            self.dimension_lst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def many_dimension(self):
            return self.getTypedRuleContext(BKITParser.Many_dimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimension_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_lst" ):
                return visitor.visitDimension_lst(self)
            else:
                return visitor.visitChildren(self)




    def dimension_lst(self):

        localctx = BKITParser.Dimension_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dimension_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.dimension()
            self.state = 126
            self.many_dimension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_dimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def many_dimension(self):
            return self.getTypedRuleContext(BKITParser.Many_dimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_dimension" ):
                return visitor.visitMany_dimension(self)
            else:
                return visitor.visitChildren(self)




    def many_dimension(self):

        localctx = BKITParser.Many_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_many_dimension)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.dimension()
                self.state = 129
                self.many_dimension()
                pass
            elif token in [BKITParser.BODY, BKITParser.ASSIGN, BKITParser.COMMA]:
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


    class DimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKITParser.LSB)
            self.state = 135
            self.match(BKITParser.INT_LIT)
            self.state = 136
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declar_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def many_func_decl(self):
            return self.getTypedRuleContext(BKITParser.Many_func_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declar_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declar_lst" ):
                return visitor.visitFunc_declar_lst(self)
            else:
                return visitor.visitChildren(self)




    def func_declar_lst(self):

        localctx = BKITParser.Func_declar_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_declar_lst)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.func_decl()
                self.state = 139
                self.many_func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def many_func_decl(self):
            return self.getTypedRuleContext(BKITParser.Many_func_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_func_decl" ):
                return visitor.visitMany_func_decl(self)
            else:
                return visitor.visitChildren(self)




    def many_func_decl(self):

        localctx = BKITParser.Many_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_many_func_decl)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.func_decl()
                self.state = 145
                self.many_func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def func_name(self):
            return self.getTypedRuleContext(BKITParser.Func_nameContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def func_param(self):
            return self.getTypedRuleContext(BKITParser.Func_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(BKITParser.FUNCTION)
            self.state = 151
            self.match(BKITParser.COLON)
            self.state = 152
            self.func_name()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 153
                self.func_param()


            self.state = 156
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_name" ):
                return visitor.visitFunc_name(self)
            else:
                return visitor.visitChildren(self)




    def func_name(self):

        localctx = BKITParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param_lst(self):
            return self.getTypedRuleContext(BKITParser.Param_lstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param" ):
                return visitor.visitFunc_param(self)
            else:
                return visitor.visitChildren(self)




    def func_param(self):

        localctx = BKITParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BKITParser.PARAMETER)
            self.state = 161
            self.match(BKITParser.COLON)
            self.state = 162
            self.param_lst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def many_params(self):
            return self.getTypedRuleContext(BKITParser.Many_paramsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = BKITParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.param()
            self.state = 165
            self.many_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def many_params(self):
            return self.getTypedRuleContext(BKITParser.Many_paramsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_params" ):
                return visitor.visitMany_params(self)
            else:
                return visitor.visitChildren(self)




    def many_params(self):

        localctx = BKITParser.Many_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_many_params)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(BKITParser.COMMA)
                self.state = 168
                self.param()
                self.state = 169
                self.many_params()
                pass
            elif token in [BKITParser.BODY]:
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


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.composite_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(BKITParser.BODY)
            self.state = 179
            self.match(BKITParser.COLON)
            self.state = 180
            self.stmt_lst()
            self.state = 181
            self.match(BKITParser.ENDBODY)
            self.state = 182
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKITParser.StmtContext,0)


        def many_stmts(self):
            return self.getTypedRuleContext(BKITParser.Many_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_lst" ):
                return visitor.visitStmt_lst(self)
            else:
                return visitor.visitChildren(self)




    def stmt_lst(self):

        localctx = BKITParser.Stmt_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_lst)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.stmt()
                self.state = 185
                self.many_stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKITParser.StmtContext,0)


        def many_stmts(self):
            return self.getTypedRuleContext(BKITParser.Many_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_stmts" ):
                return visitor.visitMany_stmts(self)
            else:
                return visitor.visitChildren(self)




    def many_stmts(self):

        localctx = BKITParser.Many_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_many_stmts)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.stmt()
                self.state = 191
                self.many_stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_main_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




    def main_func(self):

        localctx = BKITParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_main_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BKITParser.FUNCTION)
            self.state = 197
            self.match(BKITParser.COLON)
            self.state = 198
            self.match(BKITParser.T__0)
            self.state = 199
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def argument_lst(self):
            return self.getTypedRuleContext(BKITParser.Argument_lstContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(BKITParser.ID)
            self.state = 202
            self.match(BKITParser.LP)
            self.state = 203
            self.argument_lst()
            self.state = 204
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(BKITParser.ArgumentContext,0)


        def many_arguments(self):
            return self.getTypedRuleContext(BKITParser.Many_argumentsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_argument_lst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_lst" ):
                return visitor.visitArgument_lst(self)
            else:
                return visitor.visitChildren(self)




    def argument_lst(self):

        localctx = BKITParser.Argument_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_argument_lst)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.argument()
                self.state = 207
                self.many_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(BKITParser.ArgumentContext,0)


        def many_arguments(self):
            return self.getTypedRuleContext(BKITParser.Many_argumentsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_arguments" ):
                return visitor.visitMany_arguments(self)
            else:
                return visitor.visitChildren(self)




    def many_arguments(self):

        localctx = BKITParser.Many_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_many_arguments)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.argument()
                self.state = 213
                self.many_arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = BKITParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Operand_1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Operand_1Context,i)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(BKITParser.NOT_EQ, 0)

        def LESS(self):
            return self.getToken(BKITParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKITParser.GREATER, 0)

        def LESS_EQ(self):
            return self.getToken(BKITParser.LESS_EQ, 0)

        def GREATER_EQ(self):
            return self.getToken(BKITParser.GREATER_EQ, 0)

        def FLOAT_NOT_EQ(self):
            return self.getToken(BKITParser.FLOAT_NOT_EQ, 0)

        def FLOAT_LESS(self):
            return self.getToken(BKITParser.FLOAT_LESS, 0)

        def FLOAT_GREATER(self):
            return self.getToken(BKITParser.FLOAT_GREATER, 0)

        def FLOAT_LESS_EQ(self):
            return self.getToken(BKITParser.FLOAT_LESS_EQ, 0)

        def FLOAT_GREATER_EQ(self):
            return self.getToken(BKITParser.FLOAT_GREATER_EQ, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.operand_1(0)
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==BKITParser.EQ or _la==BKITParser.NOT_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.operand_1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.operand_1(0)
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==BKITParser.LESS or _la==BKITParser.GREATER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.operand_1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.operand_1(0)
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==BKITParser.LESS_EQ or _la==BKITParser.GREATER_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.operand_1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.operand_1(0)
                self.state = 233
                self.match(BKITParser.FLOAT_NOT_EQ)
                self.state = 234
                self.operand_1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.operand_1(0)
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==BKITParser.FLOAT_LESS or _la==BKITParser.FLOAT_GREATER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.operand_1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.operand_1(0)
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==BKITParser.FLOAT_LESS_EQ or _la==BKITParser.FLOAT_GREATER_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.operand_1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 244
                self.operand_1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_2(self):
            return self.getTypedRuleContext(BKITParser.Operand_2Context,0)


        def operand_1(self):
            return self.getTypedRuleContext(BKITParser.Operand_1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_1" ):
                return visitor.visitOperand_1(self)
            else:
                return visitor.visitChildren(self)



    def operand_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_operand_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.operand_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_1)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.operand_2(0) 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_3(self):
            return self.getTypedRuleContext(BKITParser.Operand_3Context,0)


        def operand_2(self):
            return self.getTypedRuleContext(BKITParser.Operand_2Context,0)


        def PLUS(self):
            return self.getToken(BKITParser.PLUS, 0)

        def FLOAT_PLUS(self):
            return self.getToken(BKITParser.FLOAT_PLUS, 0)

        def MINUS(self):
            return self.getToken(BKITParser.MINUS, 0)

        def FLOAT_MINUS(self):
            return self.getToken(BKITParser.FLOAT_MINUS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_2" ):
                return visitor.visitOperand_2(self)
            else:
                return visitor.visitChildren(self)



    def operand_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_operand_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.operand_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_2)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.PLUS) | (1 << BKITParser.FLOAT_PLUS) | (1 << BKITParser.MINUS) | (1 << BKITParser.FLOAT_MINUS))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.operand_3(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand_3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_4(self):
            return self.getTypedRuleContext(BKITParser.Operand_4Context,0)


        def operand_3(self):
            return self.getTypedRuleContext(BKITParser.Operand_3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def FLOAT_MUL(self):
            return self.getToken(BKITParser.FLOAT_MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKITParser.FLOAT_DIV, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_3" ):
                return visitor.visitOperand_3(self)
            else:
                return visitor.visitChildren(self)



    def operand_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_operand_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.operand_4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_3)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.FLOAT_MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.FLOAT_DIV) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.operand_4() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand_4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def operand_4(self):
            return self.getTypedRuleContext(BKITParser.Operand_4Context,0)


        def operand_5(self):
            return self.getTypedRuleContext(BKITParser.Operand_5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_4" ):
                return visitor.visitOperand_4(self)
            else:
                return visitor.visitChildren(self)




    def operand_4(self):

        localctx = BKITParser.Operand_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand_4)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(BKITParser.NOT)
                self.state = 281
                self.operand_4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.operand_5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_5(self):
            return self.getTypedRuleContext(BKITParser.Operand_5Context,0)


        def MINUS(self):
            return self.getToken(BKITParser.MINUS, 0)

        def FLOAT_MINUS(self):
            return self.getToken(BKITParser.FLOAT_MINUS, 0)

        def operand_6(self):
            return self.getTypedRuleContext(BKITParser.Operand_6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_5" ):
                return visitor.visitOperand_5(self)
            else:
                return visitor.visitChildren(self)




    def operand_5(self):

        localctx = BKITParser.Operand_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operand_5)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==BKITParser.MINUS or _la==BKITParser.FLOAT_MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 286
                self.operand_5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.operand_6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_7(self):
            return self.getTypedRuleContext(BKITParser.Operand_7Context,0)


        def operand_6(self):
            return self.getTypedRuleContext(BKITParser.Operand_6Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_6" ):
                return visitor.visitOperand_6(self)
            else:
                return visitor.visitChildren(self)



    def operand_6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_operand_6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.operand_7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_6)
                    self.state = 293
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 294
                    self.index_op() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operand_7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_operand_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_7" ):
                return visitor.visitOperand_7(self)
            else:
                return visitor.visitChildren(self)




    def operand_7(self):

        localctx = BKITParser.Operand_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_operand_7)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def operand_6(self):
            return self.getTypedRuleContext(BKITParser.Operand_6Context,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_index_op)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(BKITParser.LSB)
                self.state = 303
                self.operand_6(0)
                self.state = 304
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(BKITParser.LSB)
                self.state = 307
                self.operand_6(0)
                self.state = 308
                self.match(BKITParser.RSB)
                self.state = 309
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.matchWildcard()
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
        self.enterRule(localctx, 76, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKITParser.LB)
            self.state = 316
            self.lit_list()
            self.state = 317
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
        self.enterRule(localctx, 78, self.RULE_lit_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKITParser.LIT)
            self.state = 320
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
        self.enterRule(localctx, 80, self.RULE_many_lits)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(BKITParser.COMMA)
                self.state = 323
                self.match(BKITParser.LIT)
                self.state = 324
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.operand_1_sempred
        self._predicates[30] = self.operand_2_sempred
        self._predicates[31] = self.operand_3_sempred
        self._predicates[34] = self.operand_6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operand_1_sempred(self, localctx:Operand_1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def operand_2_sempred(self, localctx:Operand_2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def operand_3_sempred(self, localctx:Operand_3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def operand_6_sempred(self, localctx:Operand_6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




