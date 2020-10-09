# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\7")
        buf.write(":\u0170\n:\f:\16:\u0173\13:\3:\5:\u0176\n:\3;\3;\3;\6")
        buf.write(";\u017b\n;\r;\16;\u017c\3<\3<\3<\6<\u0182\n<\r<\16<\u0183")
        buf.write("\3=\3=\3=\5=\u0189\n=\3>\3>\7>\u018d\n>\f>\16>\u0190\13")
        buf.write(">\3?\3?\5?\u0194\n?\3?\6?\u0197\n?\r?\16?\u0198\3@\3@")
        buf.write("\5@\u019d\n@\3@\3@\3@\3@\3@\5@\u01a4\n@\5@\u01a6\n@\3")
        buf.write("A\3A\5A\u01aa\nA\3B\3B\7B\u01ae\nB\fB\16B\u01b1\13B\3")
        buf.write("B\3B\3C\3C\7C\u01b7\nC\fC\16C\u01ba\13C\3D\3D\3D\3D\7")
        buf.write("D\u01c0\nD\fD\16D\u01c3\13D\3D\3D\3D\3D\3D\3E\6E\u01cb")
        buf.write("\nE\rE\16E\u01cc\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3\u01c1")
        buf.write("\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write("\2s\2u\2w\2y:{\2}\2\177;\u0081<\u0083=\u0085>\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\3\2\16\3\2\62;\3\2\63;\4")
        buf.write("\2ZZzz\4\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\4\2--//\6\2\n")
        buf.write("\f\16\17\60\60AA\3\2c|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\2\u01e2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2y\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0093\3\2\2\2\5\u0098\3\2\2\2\7\u009e\3\2\2")
        buf.write("\2\t\u00a7\3\2\2\2\13\u00aa\3\2\2\2\r\u00af\3\2\2\2\17")
        buf.write("\u00b6\3\2\2\2\21\u00be\3\2\2\2\23\u00c4\3\2\2\2\25\u00cb")
        buf.write("\3\2\2\2\27\u00d4\3\2\2\2\31\u00d8\3\2\2\2\33\u00e1\3")
        buf.write("\2\2\2\35\u00e4\3\2\2\2\37\u00ee\3\2\2\2!\u00f5\3\2\2")
        buf.write("\2#\u00fa\3\2\2\2%\u00fe\3\2\2\2\'\u0104\3\2\2\2)\u0109")
        buf.write("\3\2\2\2+\u010f\3\2\2\2-\u0115\3\2\2\2/\u0117\3\2\2\2")
        buf.write("\61\u011a\3\2\2\2\63\u011c\3\2\2\2\65\u011f\3\2\2\2\67")
        buf.write("\u0121\3\2\2\29\u0124\3\2\2\2;\u0126\3\2\2\2=\u0129\3")
        buf.write("\2\2\2?\u012b\3\2\2\2A\u012d\3\2\2\2C\u0130\3\2\2\2E\u0133")
        buf.write("\3\2\2\2G\u0136\3\2\2\2I\u0139\3\2\2\2K\u013b\3\2\2\2")
        buf.write("M\u013d\3\2\2\2O\u0140\3\2\2\2Q\u0143\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u014a\3\2\2\2W\u014d\3\2\2\2Y\u0151\3\2\2\2[\u0155")
        buf.write("\3\2\2\2]\u0157\3\2\2\2_\u0159\3\2\2\2a\u015b\3\2\2\2")
        buf.write("c\u015d\3\2\2\2e\u015f\3\2\2\2g\u0161\3\2\2\2i\u0163\3")
        buf.write("\2\2\2k\u0165\3\2\2\2m\u0167\3\2\2\2o\u0169\3\2\2\2q\u016b")
        buf.write("\3\2\2\2s\u0175\3\2\2\2u\u0177\3\2\2\2w\u017e\3\2\2\2")
        buf.write("y\u0188\3\2\2\2{\u018a\3\2\2\2}\u0191\3\2\2\2\177\u01a5")
        buf.write("\3\2\2\2\u0081\u01a9\3\2\2\2\u0083\u01ab\3\2\2\2\u0085")
        buf.write("\u01b4\3\2\2\2\u0087\u01bb\3\2\2\2\u0089\u01ca\3\2\2\2")
        buf.write("\u008b\u01d0\3\2\2\2\u008d\u01d2\3\2\2\2\u008f\u01d4\3")
        buf.write("\2\2\2\u0091\u01d6\3\2\2\2\u0093\u0094\7D\2\2\u0094\u0095")
        buf.write("\7q\2\2\u0095\u0096\7f\2\2\u0096\u0097\7{\2\2\u0097\4")
        buf.write("\3\2\2\2\u0098\u0099\7D\2\2\u0099\u009a\7t\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7m\2\2\u009d\6")
        buf.write("\3\2\2\2\u009e\u009f\7E\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7g\2\2\u00a6\b")
        buf.write("\3\2\2\2\u00a7\u00a8\7F\2\2\u00a8\u00a9\7q\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7G\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00ae\7g\2\2\u00ae\f\3\2\2\2\u00af\u00b0")
        buf.write("\7G\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7K\2\2\u00b4\u00b5\7h\2\2\u00b5\16")
        buf.write("\3\2\2\2\u00b6\u00b7\7G\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7f\2\2\u00b9\u00ba\7D\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7f\2\2\u00bc\u00bd\7{\2\2\u00bd\20\3\2\2\2\u00be\u00bf")
        buf.write("\7G\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2")
        buf.write("\7K\2\2\u00c2\u00c3\7h\2\2\u00c3\22\3\2\2\2\u00c4\u00c5")
        buf.write("\7G\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8")
        buf.write("\7H\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7t\2\2\u00ca\24")
        buf.write("\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7f\2\2\u00ce\u00cf\7Y\2\2\u00cf\u00d0\7j\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7g\2\2\u00d3\26")
        buf.write("\3\2\2\2\u00d4\u00d5\7H\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da")
        buf.write("\7w\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7K\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7R\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7o\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7t\2\2\u00ed\36\3\2\2\2\u00ee\u00ef")
        buf.write("\7T\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7w\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7p\2\2\u00f4 \3")
        buf.write("\2\2\2\u00f5\u00f6\7V\2\2\u00f6\u00f7\7j\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7p\2\2\u00f9\"\3\2\2\2\u00fa\u00fb")
        buf.write("\7X\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7t\2\2\u00fd$\3")
        buf.write("\2\2\2\u00fe\u00ff\7Y\2\2\u00ff\u0100\7j\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7n\2\2\u0102\u0103\7g\2\2\u0103&\3")
        buf.write("\2\2\2\u0104\u0105\7V\2\2\u0105\u0106\7t\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7g\2\2\u0108(\3\2\2\2\u0109\u010a")
        buf.write("\7H\2\2\u010a\u010b\7c\2\2\u010b\u010c\7n\2\2\u010c\u010d")
        buf.write("\7u\2\2\u010d\u010e\7g\2\2\u010e*\3\2\2\2\u010f\u0110")
        buf.write("\7G\2\2\u0110\u0111\7p\2\2\u0111\u0112\7f\2\2\u0112\u0113")
        buf.write("\7F\2\2\u0113\u0114\7q\2\2\u0114,\3\2\2\2\u0115\u0116")
        buf.write("\7-\2\2\u0116.\3\2\2\2\u0117\u0118\7-\2\2\u0118\u0119")
        buf.write("\7\60\2\2\u0119\60\3\2\2\2\u011a\u011b\7/\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u011d\7/\2\2\u011d\u011e\7\60\2\2\u011e")
        buf.write("\64\3\2\2\2\u011f\u0120\7,\2\2\u0120\66\3\2\2\2\u0121")
        buf.write("\u0122\7,\2\2\u0122\u0123\7\60\2\2\u01238\3\2\2\2\u0124")
        buf.write("\u0125\7^\2\2\u0125:\3\2\2\2\u0126\u0127\7^\2\2\u0127")
        buf.write("\u0128\7\60\2\2\u0128<\3\2\2\2\u0129\u012a\7\'\2\2\u012a")
        buf.write(">\3\2\2\2\u012b\u012c\7#\2\2\u012c@\3\2\2\2\u012d\u012e")
        buf.write("\7(\2\2\u012e\u012f\7(\2\2\u012fB\3\2\2\2\u0130\u0131")
        buf.write("\7~\2\2\u0131\u0132\7~\2\2\u0132D\3\2\2\2\u0133\u0134")
        buf.write("\7?\2\2\u0134\u0135\7?\2\2\u0135F\3\2\2\2\u0136\u0137")
        buf.write("\7#\2\2\u0137\u0138\7?\2\2\u0138H\3\2\2\2\u0139\u013a")
        buf.write("\7>\2\2\u013aJ\3\2\2\2\u013b\u013c\7@\2\2\u013cL\3\2\2")
        buf.write("\2\u013d\u013e\7>\2\2\u013e\u013f\7?\2\2\u013fN\3\2\2")
        buf.write("\2\u0140\u0141\7@\2\2\u0141\u0142\7?\2\2\u0142P\3\2\2")
        buf.write("\2\u0143\u0144\7?\2\2\u0144\u0145\7\61\2\2\u0145\u0146")
        buf.write("\7?\2\2\u0146R\3\2\2\2\u0147\u0148\7>\2\2\u0148\u0149")
        buf.write("\7\60\2\2\u0149T\3\2\2\2\u014a\u014b\7@\2\2\u014b\u014c")
        buf.write("\7\60\2\2\u014cV\3\2\2\2\u014d\u014e\7>\2\2\u014e\u014f")
        buf.write("\7?\2\2\u014f\u0150\7\60\2\2\u0150X\3\2\2\2\u0151\u0152")
        buf.write("\7@\2\2\u0152\u0153\7?\2\2\u0153\u0154\7\60\2\2\u0154")
        buf.write("Z\3\2\2\2\u0155\u0156\7?\2\2\u0156\\\3\2\2\2\u0157\u0158")
        buf.write("\7*\2\2\u0158^\3\2\2\2\u0159\u015a\7+\2\2\u015a`\3\2\2")
        buf.write("\2\u015b\u015c\7}\2\2\u015cb\3\2\2\2\u015d\u015e\7\177")
        buf.write("\2\2\u015ed\3\2\2\2\u015f\u0160\7]\2\2\u0160f\3\2\2\2")
        buf.write("\u0161\u0162\7_\2\2\u0162h\3\2\2\2\u0163\u0164\7<\2\2")
        buf.write("\u0164j\3\2\2\2\u0165\u0166\7\60\2\2\u0166l\3\2\2\2\u0167")
        buf.write("\u0168\7.\2\2\u0168n\3\2\2\2\u0169\u016a\7=\2\2\u016a")
        buf.write("p\3\2\2\2\u016b\u016c\t\2\2\2\u016cr\3\2\2\2\u016d\u0171")
        buf.write("\t\3\2\2\u016e\u0170\5q9\2\u016f\u016e\3\2\2\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0176\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176\7\62\2")
        buf.write("\2\u0175\u016d\3\2\2\2\u0175\u0174\3\2\2\2\u0176t\3\2")
        buf.write("\2\2\u0177\u0178\7\62\2\2\u0178\u017a\t\4\2\2\u0179\u017b")
        buf.write("\t\5\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dv\3\2\2\2\u017e")
        buf.write("\u017f\7\62\2\2\u017f\u0181\t\6\2\2\u0180\u0182\t\7\2")
        buf.write("\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184x\3\2\2\2\u0185\u0189")
        buf.write("\5s:\2\u0186\u0189\5u;\2\u0187\u0189\5w<\2\u0188\u0185")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("z\3\2\2\2\u018a\u018e\7\60\2\2\u018b\u018d\5q9\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f|\3\2\2\2\u0190\u018e\3\2\2")
        buf.write("\2\u0191\u0193\t\b\2\2\u0192\u0194\t\t\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195")
        buf.write("\u0197\5q9\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199~\3\2\2\2\u019a")
        buf.write("\u019c\5s:\2\u019b\u019d\5{>\2\u019c\u019b\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\5}?\2\u019f")
        buf.write("\u01a6\3\2\2\2\u01a0\u01a1\5s:\2\u01a1\u01a3\5{>\2\u01a2")
        buf.write("\u01a4\5}?\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a6\3\2\2\2\u01a5\u019a\3\2\2\2\u01a5\u01a0\3\2\2\2")
        buf.write("\u01a6\u0080\3\2\2\2\u01a7\u01aa\5\'\24\2\u01a8\u01aa")
        buf.write("\5)\25\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa")
        buf.write("\u0082\3\2\2\2\u01ab\u01af\7$\2\2\u01ac\u01ae\t\n\2\2")
        buf.write("\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b2\u01b3\7$\2\2\u01b3\u0084\3\2\2\2\u01b4")
        buf.write("\u01b8\t\13\2\2\u01b5\u01b7\t\f\2\2\u01b6\u01b5\3\2\2")
        buf.write("\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u0086\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\7,\2\2\u01bc\u01bd\7,\2\2\u01bd\u01c1\3\2\2\2\u01be")
        buf.write("\u01c0\13\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2")
        buf.write("\2\u01c1\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7,\2\2\u01c5")
        buf.write("\u01c6\7,\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\bD\2\2\u01c8")
        buf.write("\u0088\3\2\2\2\u01c9\u01cb\t\r\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\bE\2\2\u01cf\u008a")
        buf.write("\3\2\2\2\u01d0\u01d1\13\2\2\2\u01d1\u008c\3\2\2\2\u01d2")
        buf.write("\u01d3\13\2\2\2\u01d3\u008e\3\2\2\2\u01d4\u01d5\13\2\2")
        buf.write("\2\u01d5\u0090\3\2\2\2\u01d6\u01d7\13\2\2\2\u01d7\u0092")
        buf.write("\3\2\2\2\23\2\u0171\u0175\u017c\u0183\u0188\u018e\u0193")
        buf.write("\u0198\u019c\u01a3\u01a5\u01a9\u01af\u01b8\u01c1\u01cc")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BODY = 1
    BREAK = 2
    CONTINUE = 3
    DO = 4
    ELSE = 5
    ELSEIF = 6
    ENDBODY = 7
    ENDIF = 8
    ENDFOR = 9
    ENDWHILE = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    PARAMETER = 14
    RETURN = 15
    THEN = 16
    VAR = 17
    WHILE = 18
    TRUE = 19
    FALSE = 20
    ENDDO = 21
    PLUS = 22
    FLOAT_PLUS = 23
    MINUS = 24
    FLOAT_MINUS = 25
    MUL = 26
    FLOAT_MUL = 27
    DIV = 28
    FLOAT_DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    EQ = 34
    NOT_EQ = 35
    LESS = 36
    GREATER = 37
    LESS_EQ = 38
    GREATER_EQ = 39
    FLOAT_NOT_EQ = 40
    FLOAT_LESS = 41
    FLOAT_GREATER = 42
    FLOAT_LESS_EQ = 43
    FLOAT_GREATER_EQ = 44
    ASSIGN = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    COLON = 52
    DOT = 53
    COMMA = 54
    SEMI = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    BOOL_LIT = 58
    STRING_LIT = 59
    ID = 60
    COMMENT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'='", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "PLUS", "FLOAT_PLUS", "MINUS", "FLOAT_MINUS", "MUL", "FLOAT_MUL", 
            "DIV", "FLOAT_DIV", "MOD", "NOT", "AND", "OR", "EQ", "NOT_EQ", 
            "LESS", "GREATER", "LESS_EQ", "GREATER_EQ", "FLOAT_NOT_EQ", 
            "FLOAT_LESS", "FLOAT_GREATER", "FLOAT_LESS_EQ", "FLOAT_GREATER_EQ", 
            "ASSIGN", "LP", "RP", "LB", "RB", "LSB", "RSB", "COLON", "DOT", 
            "COMMA", "SEMI", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
            "ID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "PLUS", "FLOAT_PLUS", "MINUS", "FLOAT_MINUS", 
                  "MUL", "FLOAT_MUL", "DIV", "FLOAT_DIV", "MOD", "NOT", 
                  "AND", "OR", "EQ", "NOT_EQ", "LESS", "GREATER", "LESS_EQ", 
                  "GREATER_EQ", "FLOAT_NOT_EQ", "FLOAT_LESS", "FLOAT_GREATER", 
                  "FLOAT_LESS_EQ", "FLOAT_GREATER_EQ", "ASSIGN", "LP", "RP", 
                  "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", 
                  "DIGIT", "INT", "HEXA_DEC", "OCTAL", "INT_LIT", "DECIMAL_PART", 
                  "EXPONENT_PART", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
                  "ID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


