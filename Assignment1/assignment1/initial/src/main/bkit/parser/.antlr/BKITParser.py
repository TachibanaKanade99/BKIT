# Generated from /media/tuanminh/DATA/Tuan_Minh/HK201/PPL/BKIT/Assignment1/assignment1/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\u01df\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4~\n\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u0084\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0093\n\b\3\t\3\t\5\t\u0097\n\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00a6\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00b0\n\16\3\17\3\17\3\17\3\17\5\17\u00b6\n\17\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00bc\n\20\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00ce\n\24\3\25\3\25\5\25\u00d2\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00de\n\27")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u00e4\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u0104\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\7\33\u010c\n\33\f\33\16\33\u010f\13")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0117\n\34\f\34")
        buf.write("\16\34\u011a\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u0122\n\35\f\35\16\35\u0125\13\35\3\36\3\36\3\36\5\36")
        buf.write("\u012a\n\36\3\37\3\37\3\37\5\37\u012f\n\37\3 \3 \3 \3")
        buf.write(" \3 \7 \u0136\n \f \16 \u0139\13 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u0144\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u0151\n\"\3#\3#\3#\3#\5#\u0157\n#\3$\3")
        buf.write("$\3$\3$\5$\u015d\n$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\5&\u016b\n&\3\'\3\'\5\'\u016f\n\'\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3)\3)\3)\3)\5)\u017f\n)\3*\3*\3*\3*\5")
        buf.write("*\u0185\n*\3+\3+\3+\3+\3+\3,\3,\3,\5,\u018f\n,\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01be\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01c5\n\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\5\65\u01cd\n\65\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\39\59\u01dd")
        buf.write("\n9\39\2\6\64\668>:\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("p\2\f\3\2%&\3\2\'(\3\2)*\3\2,-\3\2./\3\2#$\3\2\31\34\3")
        buf.write("\2\35!\3\2\33\34\3\2>A\2\u01d5\2r\3\2\2\2\4u\3\2\2\2\6")
        buf.write("}\3\2\2\2\b\u0083\3\2\2\2\n\u0085\3\2\2\2\f\u008a\3\2")
        buf.write("\2\2\16\u0092\3\2\2\2\20\u0096\3\2\2\2\22\u009b\3\2\2")
        buf.write("\2\24\u009e\3\2\2\2\26\u00a5\3\2\2\2\30\u00a7\3\2\2\2")
        buf.write("\32\u00af\3\2\2\2\34\u00b5\3\2\2\2\36\u00b7\3\2\2\2 \u00bf")
        buf.write("\3\2\2\2\"\u00c1\3\2\2\2$\u00c5\3\2\2\2&\u00cd\3\2\2\2")
        buf.write("(\u00d1\3\2\2\2*\u00d3\3\2\2\2,\u00dd\3\2\2\2.\u00e3\3")
        buf.write("\2\2\2\60\u00e5\3\2\2\2\62\u0103\3\2\2\2\64\u0105\3\2")
        buf.write("\2\2\66\u0110\3\2\2\28\u011b\3\2\2\2:\u0129\3\2\2\2<\u012e")
        buf.write("\3\2\2\2>\u0130\3\2\2\2@\u0143\3\2\2\2B\u0150\3\2\2\2")
        buf.write("D\u0156\3\2\2\2F\u015c\3\2\2\2H\u015e\3\2\2\2J\u016a\3")
        buf.write("\2\2\2L\u016e\3\2\2\2N\u0173\3\2\2\2P\u017e\3\2\2\2R\u0184")
        buf.write("\3\2\2\2T\u0186\3\2\2\2V\u018e\3\2\2\2X\u0190\3\2\2\2")
        buf.write("Z\u019f\3\2\2\2\\\u01a6\3\2\2\2^\u01ad\3\2\2\2`\u01b0")
        buf.write("\3\2\2\2b\u01b3\3\2\2\2d\u01bd\3\2\2\2f\u01c4\3\2\2\2")
        buf.write("h\u01cc\3\2\2\2j\u01ce\3\2\2\2l\u01d0\3\2\2\2n\u01d4\3")
        buf.write("\2\2\2p\u01dc\3\2\2\2rs\5\4\3\2st\7\2\2\3t\3\3\2\2\2u")
        buf.write("v\5\6\4\2vw\5\32\16\2wx\5\60\31\2x\5\3\2\2\2yz\5\n\6\2")
        buf.write("z{\5\b\5\2{~\3\2\2\2|~\3\2\2\2}y\3\2\2\2}|\3\2\2\2~\7")
        buf.write("\3\2\2\2\177\u0080\5\n\6\2\u0080\u0081\5\b\5\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0084\3\2\2\2\u0083\177\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\t\3\2\2\2\u0085\u0086\7\24\2\2\u0086\u0087")
        buf.write("\7\67\2\2\u0087\u0088\5\f\7\2\u0088\u0089\7:\2\2\u0089")
        buf.write("\13\3\2\2\2\u008a\u008b\5\20\t\2\u008b\u008c\5\16\b\2")
        buf.write("\u008c\r\3\2\2\2\u008d\u008e\79\2\2\u008e\u008f\5\20\t")
        buf.write("\2\u008f\u0090\5\16\b\2\u0090\u0093\3\2\2\2\u0091\u0093")
        buf.write("\3\2\2\2\u0092\u008d\3\2\2\2\u0092\u0091\3\2\2\2\u0093")
        buf.write("\17\3\2\2\2\u0094\u0097\7;\2\2\u0095\u0097\5\22\n\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\7\60\2\2\u0099\u009a\5j\66\2\u009a\21\3\2")
        buf.write("\2\2\u009b\u009c\7;\2\2\u009c\u009d\5\24\13\2\u009d\23")
        buf.write("\3\2\2\2\u009e\u009f\5\30\r\2\u009f\u00a0\5\26\f\2\u00a0")
        buf.write("\25\3\2\2\2\u00a1\u00a2\5\30\r\2\u00a2\u00a3\5\26\f\2")
        buf.write("\u00a3\u00a6\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a1\3")
        buf.write("\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\27\3\2\2\2\u00a7\u00a8")
        buf.write("\7\65\2\2\u00a8\u00a9\7>\2\2\u00a9\u00aa\7\66\2\2\u00aa")
        buf.write("\31\3\2\2\2\u00ab\u00ac\5\36\20\2\u00ac\u00ad\5\34\17")
        buf.write("\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ab")
        buf.write("\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\33\3\2\2\2\u00b1\u00b2")
        buf.write("\5\36\20\2\u00b2\u00b3\5\34\17\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\35\3\2\2\2\u00b7\u00b8\7\17\2\2\u00b8\u00b9\7\67")
        buf.write("\2\2\u00b9\u00bb\5 \21\2\u00ba\u00bc\5\"\22\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\5*\26\2\u00be\37\3\2\2\2\u00bf\u00c0\7;\2\2\u00c0")
        buf.write("!\3\2\2\2\u00c1\u00c2\7\21\2\2\u00c2\u00c3\7\67\2\2\u00c3")
        buf.write("\u00c4\5$\23\2\u00c4#\3\2\2\2\u00c5\u00c6\5(\25\2\u00c6")
        buf.write("\u00c7\5&\24\2\u00c7%\3\2\2\2\u00c8\u00c9\79\2\2\u00c9")
        buf.write("\u00ca\5(\25\2\u00ca\u00cb\5&\24\2\u00cb\u00ce\3\2\2\2")
        buf.write("\u00cc\u00ce\3\2\2\2\u00cd\u00c8\3\2\2\2\u00cd\u00cc\3")
        buf.write("\2\2\2\u00ce\'\3\2\2\2\u00cf\u00d2\7;\2\2\u00d0\u00d2")
        buf.write("\5\22\n\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write(")\3\2\2\2\u00d3\u00d4\7\4\2\2\u00d4\u00d5\7\67\2\2\u00d5")
        buf.write("\u00d6\5,\27\2\u00d6\u00d7\7\n\2\2\u00d7\u00d8\78\2\2")
        buf.write("\u00d8+\3\2\2\2\u00d9\u00da\5J&\2\u00da\u00db\5.\30\2")
        buf.write("\u00db\u00de\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d9\3")
        buf.write("\2\2\2\u00dd\u00dc\3\2\2\2\u00de-\3\2\2\2\u00df\u00e0")
        buf.write("\5J&\2\u00e0\u00e1\5.\30\2\u00e1\u00e4\3\2\2\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00df\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("/\3\2\2\2\u00e5\u00e6\7\17\2\2\u00e6\u00e7\7\67\2\2\u00e7")
        buf.write("\u00e8\7\3\2\2\u00e8\u00e9\5*\26\2\u00e9\61\3\2\2\2\u00ea")
        buf.write("\u00eb\5\64\33\2\u00eb\u00ec\t\2\2\2\u00ec\u00ed\5\64")
        buf.write("\33\2\u00ed\u0104\3\2\2\2\u00ee\u00ef\5\64\33\2\u00ef")
        buf.write("\u00f0\t\3\2\2\u00f0\u00f1\5\64\33\2\u00f1\u0104\3\2\2")
        buf.write("\2\u00f2\u00f3\5\64\33\2\u00f3\u00f4\t\4\2\2\u00f4\u00f5")
        buf.write("\5\64\33\2\u00f5\u0104\3\2\2\2\u00f6\u00f7\5\64\33\2\u00f7")
        buf.write("\u00f8\7+\2\2\u00f8\u00f9\5\64\33\2\u00f9\u0104\3\2\2")
        buf.write("\2\u00fa\u00fb\5\64\33\2\u00fb\u00fc\t\5\2\2\u00fc\u00fd")
        buf.write("\5\64\33\2\u00fd\u0104\3\2\2\2\u00fe\u00ff\5\64\33\2\u00ff")
        buf.write("\u0100\t\6\2\2\u0100\u0101\5\64\33\2\u0101\u0104\3\2\2")
        buf.write("\2\u0102\u0104\5\64\33\2\u0103\u00ea\3\2\2\2\u0103\u00ee")
        buf.write("\3\2\2\2\u0103\u00f2\3\2\2\2\u0103\u00f6\3\2\2\2\u0103")
        buf.write("\u00fa\3\2\2\2\u0103\u00fe\3\2\2\2\u0103\u0102\3\2\2\2")
        buf.write("\u0104\63\3\2\2\2\u0105\u0106\b\33\1\2\u0106\u0107\5\66")
        buf.write("\34\2\u0107\u010d\3\2\2\2\u0108\u0109\f\4\2\2\u0109\u010a")
        buf.write("\t\7\2\2\u010a\u010c\5\66\34\2\u010b\u0108\3\2\2\2\u010c")
        buf.write("\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010e\65\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\b\34")
        buf.write("\1\2\u0111\u0112\58\35\2\u0112\u0118\3\2\2\2\u0113\u0114")
        buf.write("\f\4\2\2\u0114\u0115\t\b\2\2\u0115\u0117\58\35\2\u0116")
        buf.write("\u0113\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\67\3\2\2\2\u011a\u0118\3\2")
        buf.write("\2\2\u011b\u011c\b\35\1\2\u011c\u011d\5:\36\2\u011d\u0123")
        buf.write("\3\2\2\2\u011e\u011f\f\4\2\2\u011f\u0120\t\t\2\2\u0120")
        buf.write("\u0122\5:\36\2\u0121\u011e\3\2\2\2\u0122\u0125\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u01249\3\2\2")
        buf.write("\2\u0125\u0123\3\2\2\2\u0126\u0127\7\"\2\2\u0127\u012a")
        buf.write("\5:\36\2\u0128\u012a\5<\37\2\u0129\u0126\3\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a;\3\2\2\2\u012b\u012c\t\n\2\2\u012c")
        buf.write("\u012f\5<\37\2\u012d\u012f\5> \2\u012e\u012b\3\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f=\3\2\2\2\u0130\u0131\b \1\2\u0131")
        buf.write("\u0132\5B\"\2\u0132\u0137\3\2\2\2\u0133\u0134\f\4\2\2")
        buf.write("\u0134\u0136\5@!\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2")
        buf.write("\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138?\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\7\65\2\2\u013b")
        buf.write("\u013c\5> \2\u013c\u013d\7\66\2\2\u013d\u0144\3\2\2\2")
        buf.write("\u013e\u013f\7\65\2\2\u013f\u0140\5> \2\u0140\u0141\7")
        buf.write("\66\2\2\u0141\u0142\5@!\2\u0142\u0144\3\2\2\2\u0143\u013a")
        buf.write("\3\2\2\2\u0143\u013e\3\2\2\2\u0144A\3\2\2\2\u0145\u0146")
        buf.write("\7;\2\2\u0146\u0147\7\61\2\2\u0147\u0148\5D#\2\u0148\u0149")
        buf.write("\7\62\2\2\u0149\u0151\3\2\2\2\u014a\u0151\5j\66\2\u014b")
        buf.write("\u0151\7;\2\2\u014c\u014d\7\61\2\2\u014d\u014e\5\62\32")
        buf.write("\2\u014e\u014f\7\62\2\2\u014f\u0151\3\2\2\2\u0150\u0145")
        buf.write("\3\2\2\2\u0150\u014a\3\2\2\2\u0150\u014b\3\2\2\2\u0150")
        buf.write("\u014c\3\2\2\2\u0151C\3\2\2\2\u0152\u0153\5H%\2\u0153")
        buf.write("\u0154\5F$\2\u0154\u0157\3\2\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0152\3\2\2\2\u0156\u0155\3\2\2\2\u0157E\3\2\2\2\u0158")
        buf.write("\u0159\5H%\2\u0159\u015a\5F$\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u015d\3\2\2\2\u015c\u0158\3\2\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015dG\3\2\2\2\u015e\u015f\13\2\2\2\u015fI\3\2\2\2\u0160")
        buf.write("\u016b\5\n\6\2\u0161\u016b\5L\'\2\u0162\u016b\5N(\2\u0163")
        buf.write("\u016b\5X-\2\u0164\u016b\5Z.\2\u0165\u016b\5\\/\2\u0166")
        buf.write("\u016b\5^\60\2\u0167\u016b\5`\61\2\u0168\u016b\5b\62\2")
        buf.write("\u0169\u016b\5h\65\2\u016a\u0160\3\2\2\2\u016a\u0161\3")
        buf.write("\2\2\2\u016a\u0162\3\2\2\2\u016a\u0163\3\2\2\2\u016a\u0164")
        buf.write("\3\2\2\2\u016a\u0165\3\2\2\2\u016a\u0166\3\2\2\2\u016a")
        buf.write("\u0167\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2")
        buf.write("\u016bK\3\2\2\2\u016c\u016f\7;\2\2\u016d\u016f\5\22\n")
        buf.write("\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0171\7\60\2\2\u0171\u0172\5\62\32\2\u0172")
        buf.write("M\3\2\2\2\u0173\u0174\7\20\2\2\u0174\u0175\5\62\32\2\u0175")
        buf.write("\u0176\7\23\2\2\u0176\u0177\5,\27\2\u0177\u0178\5P)\2")
        buf.write("\u0178\u0179\5V,\2\u0179O\3\2\2\2\u017a\u017b\5T+\2\u017b")
        buf.write("\u017c\5R*\2\u017c\u017f\3\2\2\2\u017d\u017f\3\2\2\2\u017e")
        buf.write("\u017a\3\2\2\2\u017e\u017d\3\2\2\2\u017fQ\3\2\2\2\u0180")
        buf.write("\u0181\5T+\2\u0181\u0182\5R*\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0185\3\2\2\2\u0184\u0180\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185S\3\2\2\2\u0186\u0187\7\t\2\2\u0187\u0188\5\62\32")
        buf.write("\2\u0188\u0189\7\23\2\2\u0189\u018a\5,\27\2\u018aU\3\2")
        buf.write("\2\2\u018b\u018c\7\b\2\2\u018c\u018f\5,\27\2\u018d\u018f")
        buf.write("\3\2\2\2\u018e\u018b\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("W\3\2\2\2\u0190\u0191\7\16\2\2\u0191\u0192\7\61\2\2\u0192")
        buf.write("\u0193\7;\2\2\u0193\u0194\7\60\2\2\u0194\u0195\5\62\32")
        buf.write("\2\u0195\u0196\79\2\2\u0196\u0197\5\62\32\2\u0197\u0198")
        buf.write("\79\2\2\u0198\u0199\5\62\32\2\u0199\u019a\7\62\2\2\u019a")
        buf.write("\u019b\7\7\2\2\u019b\u019c\5,\27\2\u019c\u019d\7\f\2\2")
        buf.write("\u019d\u019e\78\2\2\u019eY\3\2\2\2\u019f\u01a0\7\25\2")
        buf.write("\2\u01a0\u01a1\5\62\32\2\u01a1\u01a2\7\7\2\2\u01a2\u01a3")
        buf.write("\5,\27\2\u01a3\u01a4\7\r\2\2\u01a4\u01a5\78\2\2\u01a5")
        buf.write("[\3\2\2\2\u01a6\u01a7\7\7\2\2\u01a7\u01a8\5,\27\2\u01a8")
        buf.write("\u01a9\7\25\2\2\u01a9\u01aa\5\62\32\2\u01aa\u01ab\7\30")
        buf.write("\2\2\u01ab\u01ac\78\2\2\u01ac]\3\2\2\2\u01ad\u01ae\7\5")
        buf.write("\2\2\u01ae\u01af\7:\2\2\u01af_\3\2\2\2\u01b0\u01b1\7\6")
        buf.write("\2\2\u01b1\u01b2\7:\2\2\u01b2a\3\2\2\2\u01b3\u01b4\7;")
        buf.write("\2\2\u01b4\u01b5\7\61\2\2\u01b5\u01b6\5d\63\2\u01b6\u01b7")
        buf.write("\7\62\2\2\u01b7\u01b8\7:\2\2\u01b8c\3\2\2\2\u01b9\u01ba")
        buf.write("\5\62\32\2\u01ba\u01bb\5f\64\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01b9\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01bee\3\2\2\2\u01bf\u01c0\79\2\2\u01c0\u01c1\5\62\32")
        buf.write("\2\u01c1\u01c2\5f\64\2\u01c2\u01c5\3\2\2\2\u01c3\u01c5")
        buf.write("\3\2\2\2\u01c4\u01bf\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("g\3\2\2\2\u01c6\u01c7\7\22\2\2\u01c7\u01cd\7:\2\2\u01c8")
        buf.write("\u01c9\7\22\2\2\u01c9\u01ca\5\62\32\2\u01ca\u01cb\7:\2")
        buf.write("\2\u01cb\u01cd\3\2\2\2\u01cc\u01c6\3\2\2\2\u01cc\u01c8")
        buf.write("\3\2\2\2\u01cdi\3\2\2\2\u01ce\u01cf\t\13\2\2\u01cfk\3")
        buf.write("\2\2\2\u01d0\u01d1\7\63\2\2\u01d1\u01d2\5n8\2\u01d2\u01d3")
        buf.write("\7\64\2\2\u01d3m\3\2\2\2\u01d4\u01d5\5j\66\2\u01d5\u01d6")
        buf.write("\5p9\2\u01d6o\3\2\2\2\u01d7\u01d8\79\2\2\u01d8\u01d9\5")
        buf.write("j\66\2\u01d9\u01da\5p9\2\u01da\u01dd\3\2\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01d7\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("q\3\2\2\2\"}\u0083\u0092\u0096\u00a5\u00af\u00b5\u00bb")
        buf.write("\u00cd\u00d1\u00dd\u00e3\u0103\u010d\u0118\u0123\u0129")
        buf.write("\u012e\u0137\u0143\u0150\u0156\u015c\u016a\u016e\u017e")
        buf.write("\u0184\u018e\u01bd\u01c4\u01cc\u01dc")
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
                      "BOOL_LIT", "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
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
    RULE_expr = 24
    RULE_operand_1 = 25
    RULE_operand_2 = 26
    RULE_operand_3 = 27
    RULE_operand_4 = 28
    RULE_operand_5 = 29
    RULE_operand_6 = 30
    RULE_index_ops = 31
    RULE_operand_7 = 32
    RULE_argument_lst = 33
    RULE_many_arguments = 34
    RULE_argument = 35
    RULE_stmt = 36
    RULE_assign_stmt = 37
    RULE_if_stmt = 38
    RULE_elseif_stmt_lst = 39
    RULE_many_elseif_stmts = 40
    RULE_elseif_stmt = 41
    RULE_else_stmt = 42
    RULE_for_stmt = 43
    RULE_while_stmt = 44
    RULE_do_while_stmt = 45
    RULE_break_stmt = 46
    RULE_continue_stmt = 47
    RULE_call_stmt = 48
    RULE_expr_lst = 49
    RULE_many_exprs = 50
    RULE_return_stmt = 51
    RULE_lit = 52
    RULE_array_lit = 53
    RULE_lit_list = 54
    RULE_many_lits = 55

    ruleNames =  [ "program", "many_declars", "global_var_declar_lst", "many_var_decl", 
                   "var_decl", "var_lst", "many_var", "var", "composite_var", 
                   "dimension_lst", "many_dimension", "dimension", "func_declar_lst", 
                   "many_func_decl", "func_decl", "func_name", "func_param", 
                   "param_lst", "many_params", "param", "body", "stmt_lst", 
                   "many_stmts", "main_func", "expr", "operand_1", "operand_2", 
                   "operand_3", "operand_4", "operand_5", "operand_6", "index_ops", 
                   "operand_7", "argument_lst", "many_arguments", "argument", 
                   "stmt", "assign_stmt", "if_stmt", "elseif_stmt_lst", 
                   "many_elseif_stmts", "elseif_stmt", "else_stmt", "for_stmt", 
                   "while_stmt", "do_while_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "expr_lst", "many_exprs", "return_stmt", 
                   "lit", "array_lit", "lit_list", "many_lits" ]

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

        def many_declars(self):
            return self.getTypedRuleContext(BKITParser.Many_declarsContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.many_declars()
            self.state = 113
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




    def many_declars(self):

        localctx = BKITParser.Many_declarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.global_var_declar_lst()
            self.state = 116
            self.func_declar_lst()
            self.state = 117
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




    def global_var_declar_lst(self):

        localctx = BKITParser.Global_var_declar_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_global_var_declar_lst)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.var_decl()
                self.state = 120
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




    def many_var_decl(self):

        localctx = BKITParser.Many_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_many_var_decl)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.var_decl()
                self.state = 126
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


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BKITParser.VAR)
            self.state = 132
            self.match(BKITParser.COLON)
            self.state = 133
            self.var_lst()
            self.state = 134
            self.match(BKITParser.SEMI)
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




    def var_lst(self):

        localctx = BKITParser.Var_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.var()
            self.state = 137
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




    def many_var(self):

        localctx = BKITParser.Many_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_many_var)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(BKITParser.COMMA)
                self.state = 140
                self.var()
                self.state = 141
                self.many_var()
                pass
            elif token in [BKITParser.SEMI]:
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

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 147
                self.composite_var()
                pass


            self.state = 150
            self.match(BKITParser.ASSIGN)
            self.state = 151
            self.lit()
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




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_composite_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BKITParser.ID)
            self.state = 154
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




    def dimension_lst(self):

        localctx = BKITParser.Dimension_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dimension_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.dimension()
            self.state = 157
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




    def many_dimension(self):

        localctx = BKITParser.Many_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_many_dimension)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.dimension()
                self.state = 160
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




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BKITParser.LSB)
            self.state = 166
            self.match(BKITParser.INT_LIT)
            self.state = 167
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




    def func_declar_lst(self):

        localctx = BKITParser.Func_declar_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_declar_lst)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.func_decl()
                self.state = 170
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




    def many_func_decl(self):

        localctx = BKITParser.Many_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_many_func_decl)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.func_decl()
                self.state = 176
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




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKITParser.FUNCTION)
            self.state = 182
            self.match(BKITParser.COLON)
            self.state = 183
            self.func_name()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 184
                self.func_param()


            self.state = 187
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




    def func_name(self):

        localctx = BKITParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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




    def func_param(self):

        localctx = BKITParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKITParser.PARAMETER)
            self.state = 192
            self.match(BKITParser.COLON)
            self.state = 193
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




    def param_lst(self):

        localctx = BKITParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_lst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.param()
            self.state = 196
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




    def many_params(self):

        localctx = BKITParser.Many_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_many_params)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(BKITParser.COMMA)
                self.state = 199
                self.param()
                self.state = 200
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




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKITParser.BODY)
            self.state = 210
            self.match(BKITParser.COLON)
            self.state = 211
            self.stmt_lst()
            self.state = 212
            self.match(BKITParser.ENDBODY)
            self.state = 213
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




    def stmt_lst(self):

        localctx = BKITParser.Stmt_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_lst)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.stmt()
                self.state = 216
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




    def many_stmts(self):

        localctx = BKITParser.Many_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_many_stmts)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.stmt()
                self.state = 222
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




    def main_func(self):

        localctx = BKITParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_main_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(BKITParser.FUNCTION)
            self.state = 228
            self.match(BKITParser.COLON)
            self.state = 229
            self.match(BKITParser.T__0)
            self.state = 230
            self.body()
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




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.operand_1(0)
                self.state = 233
                _la = self._input.LA(1)
                if not(_la==BKITParser.EQ or _la==BKITParser.NOT_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.operand_1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.operand_1(0)
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==BKITParser.LESS or _la==BKITParser.GREATER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.operand_1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.operand_1(0)
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==BKITParser.LESS_EQ or _la==BKITParser.GREATER_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.operand_1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.operand_1(0)
                self.state = 245
                self.match(BKITParser.FLOAT_NOT_EQ)
                self.state = 246
                self.operand_1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.operand_1(0)
                self.state = 249
                _la = self._input.LA(1)
                if not(_la==BKITParser.FLOAT_LESS or _la==BKITParser.FLOAT_GREATER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.operand_1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.operand_1(0)
                self.state = 253
                _la = self._input.LA(1)
                if not(_la==BKITParser.FLOAT_LESS_EQ or _la==BKITParser.FLOAT_GREATER_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 254
                self.operand_1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
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



    def operand_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_operand_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.operand_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_1)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.operand_2(0) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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



    def operand_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_operand_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.operand_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_2)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.PLUS) | (1 << BKITParser.FLOAT_PLUS) | (1 << BKITParser.MINUS) | (1 << BKITParser.FLOAT_MINUS))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.operand_3(0) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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



    def operand_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_operand_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.operand_4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_3)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.FLOAT_MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.FLOAT_DIV) | (1 << BKITParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 286
                    self.operand_4() 
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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




    def operand_4(self):

        localctx = BKITParser.Operand_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_operand_4)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(BKITParser.NOT)
                self.state = 293
                self.operand_4()
                pass
            elif token in [BKITParser.MINUS, BKITParser.FLOAT_MINUS, BKITParser.LP, BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.operand_5()
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




    def operand_5(self):

        localctx = BKITParser.Operand_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operand_5)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS, BKITParser.FLOAT_MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==BKITParser.MINUS or _la==BKITParser.FLOAT_MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.operand_5()
                pass
            elif token in [BKITParser.LP, BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.operand_6(0)
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


    class Operand_6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_7(self):
            return self.getTypedRuleContext(BKITParser.Operand_7Context,0)


        def operand_6(self):
            return self.getTypedRuleContext(BKITParser.Operand_6Context,0)


        def index_ops(self):
            return self.getTypedRuleContext(BKITParser.Index_opsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand_6



    def operand_6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Operand_6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_operand_6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.operand_7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Operand_6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operand_6)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
                    self.index_ops() 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_opsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def operand_6(self):
            return self.getTypedRuleContext(BKITParser.Operand_6Context,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def index_ops(self):
            return self.getTypedRuleContext(BKITParser.Index_opsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_ops




    def index_ops(self):

        localctx = BKITParser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_ops)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(BKITParser.LSB)
                self.state = 313
                self.operand_6(0)
                self.state = 314
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(BKITParser.LSB)
                self.state = 317
                self.operand_6(0)
                self.state = 318
                self.match(BKITParser.RSB)
                self.state = 319
                self.index_ops()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_7Context(ParserRuleContext):

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

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand_7




    def operand_7(self):

        localctx = BKITParser.Operand_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand_7)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(BKITParser.ID)
                self.state = 324
                self.match(BKITParser.LP)
                self.state = 325
                self.argument_lst()
                self.state = 326
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 330
                self.match(BKITParser.LP)
                self.state = 331
                self.expr()
                self.state = 332
                self.match(BKITParser.RP)
                pass


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




    def argument_lst(self):

        localctx = BKITParser.Argument_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argument_lst)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.argument()
                self.state = 337
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




    def many_arguments(self):

        localctx = BKITParser.Many_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_many_arguments)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.argument()
                self.state = 343
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




    def argument(self):

        localctx = BKITParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.matchWildcard()
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

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 354
                self.while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 355
                self.do_while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 356
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 357
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 358
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 359
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 362
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 363
                self.composite_var()
                pass


            self.state = 366
            self.match(BKITParser.ASSIGN)
            self.state = 367
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def elseif_stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Elseif_stmt_lstContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(BKITParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BKITParser.IF)
            self.state = 370
            self.expr()
            self.state = 371
            self.match(BKITParser.THEN)
            self.state = 372
            self.stmt_lst()
            self.state = 373
            self.elseif_stmt_lst()
            self.state = 374
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmt_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(BKITParser.Elseif_stmtContext,0)


        def many_elseif_stmts(self):
            return self.getTypedRuleContext(BKITParser.Many_elseif_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt_lst




    def elseif_stmt_lst(self):

        localctx = BKITParser.Elseif_stmt_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elseif_stmt_lst)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.elseif_stmt()
                self.state = 377
                self.many_elseif_stmts()
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


    class Many_elseif_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(BKITParser.Elseif_stmtContext,0)


        def many_elseif_stmts(self):
            return self.getTypedRuleContext(BKITParser.Many_elseif_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_elseif_stmts




    def many_elseif_stmts(self):

        localctx = BKITParser.Many_elseif_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_many_elseif_stmts)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.elseif_stmt()
                self.state = 383
                self.many_elseif_stmts()
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


    class Elseif_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(BKITParser.ELSEIF)
            self.state = 389
            self.expr()
            self.state = 390
            self.match(BKITParser.THEN)
            self.state = 391
            self.stmt_lst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_stmt




    def else_stmt(self):

        localctx = BKITParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_else_stmt)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(BKITParser.ELSE)
                self.state = 394
                self.stmt_lst()
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


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(BKITParser.FOR)
            self.state = 399
            self.match(BKITParser.LP)
            self.state = 400
            self.match(BKITParser.ID)
            self.state = 401
            self.match(BKITParser.ASSIGN)
            self.state = 402
            self.expr()
            self.state = 403
            self.match(BKITParser.COMMA)
            self.state = 404
            self.expr()
            self.state = 405
            self.match(BKITParser.COMMA)
            self.state = 406
            self.expr()
            self.state = 407
            self.match(BKITParser.RP)
            self.state = 408
            self.match(BKITParser.DO)
            self.state = 409
            self.stmt_lst()
            self.state = 410
            self.match(BKITParser.ENDFOR)
            self.state = 411
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(BKITParser.WHILE)
            self.state = 414
            self.expr()
            self.state = 415
            self.match(BKITParser.DO)
            self.state = 416
            self.stmt_lst()
            self.state = 417
            self.match(BKITParser.ENDWHILE)
            self.state = 418
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_lst(self):
            return self.getTypedRuleContext(BKITParser.Stmt_lstContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BKITParser.DO)
            self.state = 421
            self.stmt_lst()
            self.state = 422
            self.match(BKITParser.WHILE)
            self.state = 423
            self.expr()
            self.state = 424
            self.match(BKITParser.ENDDO)
            self.state = 425
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(BKITParser.BREAK)
            self.state = 428
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(BKITParser.CONTINUE)
            self.state = 431
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(BKITParser.Expr_lstContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(BKITParser.ID)
            self.state = 434
            self.match(BKITParser.LP)
            self.state = 435
            self.expr_lst()
            self.state = 436
            self.match(BKITParser.RP)
            self.state = 437
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def many_exprs(self):
            return self.getTypedRuleContext(BKITParser.Many_exprsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr_lst




    def expr_lst(self):

        localctx = BKITParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr_lst)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.MINUS, BKITParser.FLOAT_MINUS, BKITParser.NOT, BKITParser.LP, BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.expr()
                self.state = 440
                self.many_exprs()
                pass
            elif token in [BKITParser.RP]:
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


    class Many_exprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def many_exprs(self):
            return self.getTypedRuleContext(BKITParser.Many_exprsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_exprs




    def many_exprs(self):

        localctx = BKITParser.Many_exprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_many_exprs)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.match(BKITParser.COMMA)
                self.state = 446
                self.expr()
                self.state = 447
                self.many_exprs()
                pass
            elif token in [BKITParser.RP]:
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


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_return_stmt)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(BKITParser.RETURN)
                self.state = 453
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.match(BKITParser.RETURN)
                self.state = 455
                self.expr()
                self.state = 456
                self.match(BKITParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_lit




    def lit(self):

        localctx = BKITParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(BKITParser.LB)
            self.state = 463
            self.lit_list()
            self.state = 464
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

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def many_lits(self):
            return self.getTypedRuleContext(BKITParser.Many_litsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lit_list




    def lit_list(self):

        localctx = BKITParser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lit_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.lit()
            self.state = 467
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

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def many_lits(self):
            return self.getTypedRuleContext(BKITParser.Many_litsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_lits




    def many_lits(self):

        localctx = BKITParser.Many_litsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_many_lits)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(BKITParser.COMMA)
                self.state = 470
                self.lit()
                self.state = 471
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
        self._predicates[25] = self.operand_1_sempred
        self._predicates[26] = self.operand_2_sempred
        self._predicates[27] = self.operand_3_sempred
        self._predicates[30] = self.operand_6_sempred
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
         




