# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\7")
        buf.write("9\u0170\n9\f9\169\u0173\139\3:\3:\3:\3:\7:\u0179\n:\f")
        buf.write(":\16:\u017c\13:\3:\3:\3:\3:\3:\3;\6;\u0184\n;\r;\16;\u0185")
        buf.write("\3;\3;\3<\3<\3=\3=\7=\u018e\n=\f=\16=\u0191\13=\3=\5=")
        buf.write("\u0194\n=\3>\3>\3>\6>\u0199\n>\r>\16>\u019a\3?\3?\3?\6")
        buf.write("?\u01a0\n?\r?\16?\u01a1\3@\3@\3@\5@\u01a7\n@\3A\3A\7A")
        buf.write("\u01ab\nA\fA\16A\u01ae\13A\3B\3B\5B\u01b2\nB\3B\6B\u01b5")
        buf.write("\nB\rB\16B\u01b6\3C\3C\5C\u01bb\nC\3C\3C\3C\3C\3C\5C\u01c2")
        buf.write("\nC\5C\u01c4\nC\3D\3D\3D\3E\3E\3E\3F\3F\3F\3F\7F\u01d0")
        buf.write("\nF\fF\16F\u01d3\13F\3F\3F\3F\3G\3G\3H\3H\3H\3H\7H\u01de")
        buf.write("\nH\fH\16H\u01e1\13H\3H\3H\3I\3I\3I\3I\7I\u01e9\nI\fI")
        buf.write("\16I\u01ec\13I\3I\3I\3I\3I\5I\u01f2\nI\3I\3I\3J\3J\3J")
        buf.write("\3J\7J\u01fa\nJ\fJ\16J\u01fd\13J\4\u017a\u01fb\2K\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("\2y\2{\2}\2\177=\u0081\2\u0083\2\u0085>\u0087\2\u0089")
        buf.write("\2\u008b?\u008d@\u008fA\u0091B\u0093C\3\2\20\3\2c|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\62;\3\2\63;\4\2ZZz")
        buf.write("z\4\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\4\2--//\t\2))^^dd")
        buf.write("hhppttvv\7\2\n\f\16\17$$))^^\3\2$$\2\u020f\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009a\3\2\2\2\7\u00a0")
        buf.write("\3\2\2\2\t\u00a9\3\2\2\2\13\u00ac\3\2\2\2\r\u00b1\3\2")
        buf.write("\2\2\17\u00b8\3\2\2\2\21\u00c0\3\2\2\2\23\u00c6\3\2\2")
        buf.write("\2\25\u00cd\3\2\2\2\27\u00d6\3\2\2\2\31\u00da\3\2\2\2")
        buf.write("\33\u00e3\3\2\2\2\35\u00e6\3\2\2\2\37\u00f0\3\2\2\2!\u00f7")
        buf.write("\3\2\2\2#\u00fc\3\2\2\2%\u0100\3\2\2\2\'\u0106\3\2\2\2")
        buf.write(")\u010b\3\2\2\2+\u0111\3\2\2\2-\u0117\3\2\2\2/\u0119\3")
        buf.write("\2\2\2\61\u011c\3\2\2\2\63\u011e\3\2\2\2\65\u0121\3\2")
        buf.write("\2\2\67\u0123\3\2\2\29\u0126\3\2\2\2;\u0128\3\2\2\2=\u012b")
        buf.write("\3\2\2\2?\u012d\3\2\2\2A\u012f\3\2\2\2C\u0132\3\2\2\2")
        buf.write("E\u0135\3\2\2\2G\u0138\3\2\2\2I\u013b\3\2\2\2K\u013d\3")
        buf.write("\2\2\2M\u013f\3\2\2\2O\u0142\3\2\2\2Q\u0145\3\2\2\2S\u0149")
        buf.write("\3\2\2\2U\u014c\3\2\2\2W\u014f\3\2\2\2Y\u0153\3\2\2\2")
        buf.write("[\u0157\3\2\2\2]\u0159\3\2\2\2_\u015b\3\2\2\2a\u015d\3")
        buf.write("\2\2\2c\u015f\3\2\2\2e\u0161\3\2\2\2g\u0163\3\2\2\2i\u0165")
        buf.write("\3\2\2\2k\u0167\3\2\2\2m\u0169\3\2\2\2o\u016b\3\2\2\2")
        buf.write("q\u016d\3\2\2\2s\u0174\3\2\2\2u\u0183\3\2\2\2w\u0189\3")
        buf.write("\2\2\2y\u0193\3\2\2\2{\u0195\3\2\2\2}\u019c\3\2\2\2\177")
        buf.write("\u01a6\3\2\2\2\u0081\u01a8\3\2\2\2\u0083\u01af\3\2\2\2")
        buf.write("\u0085\u01c3\3\2\2\2\u0087\u01c5\3\2\2\2\u0089\u01c8\3")
        buf.write("\2\2\2\u008b\u01cb\3\2\2\2\u008d\u01d7\3\2\2\2\u008f\u01d9")
        buf.write("\3\2\2\2\u0091\u01e4\3\2\2\2\u0093\u01f5\3\2\2\2\u0095")
        buf.write("\u0096\7D\2\2\u0096\u0097\7q\2\2\u0097\u0098\7f\2\2\u0098")
        buf.write("\u0099\7{\2\2\u0099\4\3\2\2\2\u009a\u009b\7D\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7m\2\2\u009f\6\3\2\2\2\u00a0\u00a1\7E\2\2\u00a1")
        buf.write("\u00a2\7q\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7v\2\2\u00a4")
        buf.write("\u00a5\7k\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7w\2\2\u00a7")
        buf.write("\u00a8\7g\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7F\2\2\u00aa")
        buf.write("\u00ab\7q\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7G\2\2\u00ad")
        buf.write("\u00ae\7n\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\f\3\2\2\2\u00b1\u00b2\7G\2\2\u00b2\u00b3\7n\2\2\u00b3")
        buf.write("\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7K\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\16\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9")
        buf.write("\u00ba\7p\2\2\u00ba\u00bb\7f\2\2\u00bb\u00bc\7D\2\2\u00bc")
        buf.write("\u00bd\7q\2\2\u00bd\u00be\7f\2\2\u00be\u00bf\7{\2\2\u00bf")
        buf.write("\20\3\2\2\2\u00c0\u00c1\7G\2\2\u00c1\u00c2\7p\2\2\u00c2")
        buf.write("\u00c3\7f\2\2\u00c3\u00c4\7K\2\2\u00c4\u00c5\7h\2\2\u00c5")
        buf.write("\22\3\2\2\2\u00c6\u00c7\7G\2\2\u00c7\u00c8\7p\2\2\u00c8")
        buf.write("\u00c9\7f\2\2\u00c9\u00ca\7H\2\2\u00ca\u00cb\7q\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\24\3\2\2\2\u00cd\u00ce\7G\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7f\2\2\u00d0\u00d1\7Y\2\2\u00d1")
        buf.write("\u00d2\7j\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7n\2\2\u00d4")
        buf.write("\u00d5\7g\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7H\2\2\u00d7")
        buf.write("\u00d8\7q\2\2\u00d8\u00d9\7t\2\2\u00d9\30\3\2\2\2\u00da")
        buf.write("\u00db\7H\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\u00de\7e\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0")
        buf.write("\u00e1\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\32\3\2\2\2\u00e3")
        buf.write("\u00e4\7K\2\2\u00e4\u00e5\7h\2\2\u00e5\34\3\2\2\2\u00e6")
        buf.write("\u00e7\7R\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("\u00ea\7c\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7g\2\2\u00ec")
        buf.write("\u00ed\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7t\2\2\u00ef")
        buf.write("\36\3\2\2\2\u00f0\u00f1\7T\2\2\u00f1\u00f2\7g\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7t\2\2\u00f5")
        buf.write("\u00f6\7p\2\2\u00f6 \3\2\2\2\u00f7\u00f8\7V\2\2\u00f8")
        buf.write("\u00f9\7j\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb")
        buf.write("\"\3\2\2\2\u00fc\u00fd\7X\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff$\3\2\2\2\u0100\u0101\7Y\2\2\u0101")
        buf.write("\u0102\7j\2\2\u0102\u0103\7k\2\2\u0103\u0104\7n\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105&\3\2\2\2\u0106\u0107\7V\2\2\u0107")
        buf.write("\u0108\7t\2\2\u0108\u0109\7w\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("(\3\2\2\2\u010b\u010c\7H\2\2\u010c\u010d\7c\2\2\u010d")
        buf.write("\u010e\7n\2\2\u010e\u010f\7u\2\2\u010f\u0110\7g\2\2\u0110")
        buf.write("*\3\2\2\2\u0111\u0112\7G\2\2\u0112\u0113\7p\2\2\u0113")
        buf.write("\u0114\7f\2\2\u0114\u0115\7F\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write(",\3\2\2\2\u0117\u0118\7-\2\2\u0118.\3\2\2\2\u0119\u011a")
        buf.write("\7-\2\2\u011a\u011b\7\60\2\2\u011b\60\3\2\2\2\u011c\u011d")
        buf.write("\7/\2\2\u011d\62\3\2\2\2\u011e\u011f\7/\2\2\u011f\u0120")
        buf.write("\7\60\2\2\u0120\64\3\2\2\2\u0121\u0122\7,\2\2\u0122\66")
        buf.write("\3\2\2\2\u0123\u0124\7,\2\2\u0124\u0125\7\60\2\2\u0125")
        buf.write("8\3\2\2\2\u0126\u0127\7^\2\2\u0127:\3\2\2\2\u0128\u0129")
        buf.write("\7^\2\2\u0129\u012a\7\60\2\2\u012a<\3\2\2\2\u012b\u012c")
        buf.write("\7\'\2\2\u012c>\3\2\2\2\u012d\u012e\7#\2\2\u012e@\3\2")
        buf.write("\2\2\u012f\u0130\7(\2\2\u0130\u0131\7(\2\2\u0131B\3\2")
        buf.write("\2\2\u0132\u0133\7~\2\2\u0133\u0134\7~\2\2\u0134D\3\2")
        buf.write("\2\2\u0135\u0136\7?\2\2\u0136\u0137\7?\2\2\u0137F\3\2")
        buf.write("\2\2\u0138\u0139\7#\2\2\u0139\u013a\7?\2\2\u013aH\3\2")
        buf.write("\2\2\u013b\u013c\7>\2\2\u013cJ\3\2\2\2\u013d\u013e\7@")
        buf.write("\2\2\u013eL\3\2\2\2\u013f\u0140\7>\2\2\u0140\u0141\7?")
        buf.write("\2\2\u0141N\3\2\2\2\u0142\u0143\7@\2\2\u0143\u0144\7?")
        buf.write("\2\2\u0144P\3\2\2\2\u0145\u0146\7?\2\2\u0146\u0147\7\61")
        buf.write("\2\2\u0147\u0148\7?\2\2\u0148R\3\2\2\2\u0149\u014a\7>")
        buf.write("\2\2\u014a\u014b\7\60\2\2\u014bT\3\2\2\2\u014c\u014d\7")
        buf.write("@\2\2\u014d\u014e\7\60\2\2\u014eV\3\2\2\2\u014f\u0150")
        buf.write("\7>\2\2\u0150\u0151\7?\2\2\u0151\u0152\7\60\2\2\u0152")
        buf.write("X\3\2\2\2\u0153\u0154\7@\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\u0156\7\60\2\2\u0156Z\3\2\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("\\\3\2\2\2\u0159\u015a\7*\2\2\u015a^\3\2\2\2\u015b\u015c")
        buf.write("\7+\2\2\u015c`\3\2\2\2\u015d\u015e\7}\2\2\u015eb\3\2\2")
        buf.write("\2\u015f\u0160\7\177\2\2\u0160d\3\2\2\2\u0161\u0162\7")
        buf.write("]\2\2\u0162f\3\2\2\2\u0163\u0164\7_\2\2\u0164h\3\2\2\2")
        buf.write("\u0165\u0166\7<\2\2\u0166j\3\2\2\2\u0167\u0168\7\60\2")
        buf.write("\2\u0168l\3\2\2\2\u0169\u016a\7.\2\2\u016an\3\2\2\2\u016b")
        buf.write("\u016c\7=\2\2\u016cp\3\2\2\2\u016d\u0171\t\2\2\2\u016e")
        buf.write("\u0170\t\3\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172r\3\2\2")
        buf.write("\2\u0173\u0171\3\2\2\2\u0174\u0175\7,\2\2\u0175\u0176")
        buf.write("\7,\2\2\u0176\u017a\3\2\2\2\u0177\u0179\13\2\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017d\u017e\7,\2\2\u017e\u017f\7,\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\b:\2\2\u0181t\3\2\2\2\u0182\u0184")
        buf.write("\t\4\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0188\b;\2\2\u0188v\3\2\2\2\u0189\u018a\t\5\2\2")
        buf.write("\u018ax\3\2\2\2\u018b\u018f\t\6\2\2\u018c\u018e\5w<\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190\u0194\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0194\7\62\2\2\u0193\u018b\3\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194z\3\2\2\2\u0195\u0196\7\62\2\2\u0196")
        buf.write("\u0198\t\7\2\2\u0197\u0199\t\b\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b|\3\2\2\2\u019c\u019d\7\62\2\2\u019d\u019f")
        buf.write("\t\t\2\2\u019e\u01a0\t\n\2\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2~\3\2\2\2\u01a3\u01a7\5y=\2\u01a4\u01a7\5{>\2\u01a5")
        buf.write("\u01a7\5}?\2\u01a6\u01a3\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u0080\3\2\2\2\u01a8\u01ac\7\60\2")
        buf.write("\2\u01a9\u01ab\5w<\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u0082")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1\t\13\2\2\u01b0")
        buf.write("\u01b2\t\f\2\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2\u01b4\3\2\2\2\u01b3\u01b5\5w<\2\u01b4\u01b3\3\2")
        buf.write("\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u0084\3\2\2\2\u01b8\u01ba\5y=\2\u01b9\u01bb")
        buf.write("\5\u0081A\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01bd\5\u0083B\2\u01bd\u01c4\3\2")
        buf.write("\2\2\u01be\u01bf\5y=\2\u01bf\u01c1\5\u0081A\2\u01c0\u01c2")
        buf.write("\5\u0083B\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01b8\3\2\2\2\u01c3\u01be\3\2\2\2")
        buf.write("\u01c4\u0086\3\2\2\2\u01c5\u01c6\7)\2\2\u01c6\u01c7\7")
        buf.write("$\2\2\u01c7\u0088\3\2\2\2\u01c8\u01c9\7^\2\2\u01c9\u01ca")
        buf.write("\t\r\2\2\u01ca\u008a\3\2\2\2\u01cb\u01d1\7$\2\2\u01cc")
        buf.write("\u01d0\n\16\2\2\u01cd\u01d0\5\u0089E\2\u01ce\u01d0\5\u0087")
        buf.write("D\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2")
        buf.write("\u01d4\u01d5\7$\2\2\u01d5\u01d6\bF\3\2\u01d6\u008c\3\2")
        buf.write("\2\2\u01d7\u01d8\13\2\2\2\u01d8\u008e\3\2\2\2\u01d9\u01df")
        buf.write("\7$\2\2\u01da\u01de\n\16\2\2\u01db\u01de\5\u0089E\2\u01dc")
        buf.write("\u01de\5\u0087D\2\u01dd\u01da\3\2\2\2\u01dd\u01db\3\2")
        buf.write("\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e2\u01e3\bH\4\2\u01e3\u0090\3\2\2\2")
        buf.write("\u01e4\u01ea\7$\2\2\u01e5\u01e9\n\16\2\2\u01e6\u01e9\5")
        buf.write("\u0089E\2\u01e7\u01e9\5\u0087D\2\u01e8\u01e5\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01f1\3")
        buf.write("\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7^\2\2\u01ee\u01f2")
        buf.write("\n\r\2\2\u01ef\u01f0\7)\2\2\u01f0\u01f2\n\17\2\2\u01f1")
        buf.write("\u01ed\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f4\bI\5\2\u01f4\u0092\3\2\2\2\u01f5\u01f6\7")
        buf.write(",\2\2\u01f6\u01f7\7,\2\2\u01f7\u01fb\3\2\2\2\u01f8\u01fa")
        buf.write("\13\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u0094\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\31\2\u0171\u017a\u0185\u018f\u0193")
        buf.write("\u019a\u01a1\u01a6\u01ac\u01b1\u01b6\u01ba\u01c1\u01c3")
        buf.write("\u01cf\u01d1\u01dd\u01df\u01e8\u01ea\u01f1\u01fb\6\b\2")
        buf.write("\2\3F\2\3H\3\3I\4")
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
    ID = 56
    COMMENT = 57
    WS = 58
    INT_LIT = 59
    FLOAT_LIT = 60
    STRING_LIT = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65

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
            "COMMA", "SEMI", "ID", "COMMENT", "WS", "INT_LIT", "FLOAT_LIT", 
            "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
                  "ID", "COMMENT", "WS", "DIGIT", "INT", "HEXA_DEC", "OCTAL", 
                  "INT_LIT", "DECIMAL_PART", "EXPONENT_PART", "FLOAT_LIT", 
                  "ESCAPE_QUOTE", "ESCAPE_CHAR", "STRING_LIT", "ERROR_CHAR", 
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[68] = self.STRING_LIT_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     


