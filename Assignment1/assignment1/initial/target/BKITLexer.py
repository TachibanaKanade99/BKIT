# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0204\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\79\u0172\n9\f9\169\u0175\139\3:\3:\3:\3:\7:\u017b")
        buf.write("\n:\f:\16:\u017e\13:\3:\3:\3:\3:\3:\3;\6;\u0186\n;\r;")
        buf.write("\16;\u0187\3;\3;\3<\3<\3=\3=\7=\u0190\n=\f=\16=\u0193")
        buf.write("\13=\3=\5=\u0196\n=\3>\3>\3>\6>\u019b\n>\r>\16>\u019c")
        buf.write("\3?\3?\3?\6?\u01a2\n?\r?\16?\u01a3\3@\3@\3@\5@\u01a9\n")
        buf.write("@\3A\3A\7A\u01ad\nA\fA\16A\u01b0\13A\3B\3B\5B\u01b4\n")
        buf.write("B\3B\6B\u01b7\nB\rB\16B\u01b8\3C\3C\5C\u01bd\nC\3C\3C")
        buf.write("\3C\3C\3C\5C\u01c4\nC\5C\u01c6\nC\3D\3D\5D\u01ca\nD\3")
        buf.write("E\3E\3E\3F\3F\3F\3G\3G\3G\3G\7G\u01d6\nG\fG\16G\u01d9")
        buf.write("\13G\3G\3G\3G\3H\3H\3I\3I\3I\3I\7I\u01e4\nI\fI\16I\u01e7")
        buf.write("\13I\3I\3I\3J\3J\3J\3J\7J\u01ef\nJ\fJ\16J\u01f2\13J\3")
        buf.write("J\3J\3J\3J\5J\u01f8\nJ\3J\3J\3K\3K\3K\3K\7K\u0200\nK\f")
        buf.write("K\16K\u0203\13K\4\u017c\u0201\2L\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081")
        buf.write("\2\u0083\2\u0085>\u0087?\u0089\2\u008b\2\u008d@\u008f")
        buf.write("A\u0091B\u0093C\u0095D\3\2\20\3\2c|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\3\2\62;\3\2\63;\4\2ZZzz\4\2\62;CH\4\2")
        buf.write("QQqq\3\2\629\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\5\2$$)")
        buf.write(")^^\3\2$$\2\u0216\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u0097\3\2\2\2\5\u009c\3\2\2\2\7\u00a2\3\2\2")
        buf.write("\2\t\u00ab\3\2\2\2\13\u00ae\3\2\2\2\r\u00b3\3\2\2\2\17")
        buf.write("\u00ba\3\2\2\2\21\u00c2\3\2\2\2\23\u00c8\3\2\2\2\25\u00cf")
        buf.write("\3\2\2\2\27\u00d8\3\2\2\2\31\u00dc\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00e8\3\2\2\2\37\u00f2\3\2\2\2!\u00f9\3\2\2")
        buf.write("\2#\u00fe\3\2\2\2%\u0102\3\2\2\2\'\u0108\3\2\2\2)\u010d")
        buf.write("\3\2\2\2+\u0113\3\2\2\2-\u0119\3\2\2\2/\u011b\3\2\2\2")
        buf.write("\61\u011e\3\2\2\2\63\u0120\3\2\2\2\65\u0123\3\2\2\2\67")
        buf.write("\u0125\3\2\2\29\u0128\3\2\2\2;\u012a\3\2\2\2=\u012d\3")
        buf.write("\2\2\2?\u012f\3\2\2\2A\u0131\3\2\2\2C\u0134\3\2\2\2E\u0137")
        buf.write("\3\2\2\2G\u013a\3\2\2\2I\u013d\3\2\2\2K\u013f\3\2\2\2")
        buf.write("M\u0141\3\2\2\2O\u0144\3\2\2\2Q\u0147\3\2\2\2S\u014b\3")
        buf.write("\2\2\2U\u014e\3\2\2\2W\u0151\3\2\2\2Y\u0155\3\2\2\2[\u0159")
        buf.write("\3\2\2\2]\u015b\3\2\2\2_\u015d\3\2\2\2a\u015f\3\2\2\2")
        buf.write("c\u0161\3\2\2\2e\u0163\3\2\2\2g\u0165\3\2\2\2i\u0167\3")
        buf.write("\2\2\2k\u0169\3\2\2\2m\u016b\3\2\2\2o\u016d\3\2\2\2q\u016f")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u0185\3\2\2\2w\u018b\3\2\2\2")
        buf.write("y\u0195\3\2\2\2{\u0197\3\2\2\2}\u019e\3\2\2\2\177\u01a8")
        buf.write("\3\2\2\2\u0081\u01aa\3\2\2\2\u0083\u01b1\3\2\2\2\u0085")
        buf.write("\u01c5\3\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01cb\3\2\2\2")
        buf.write("\u008b\u01ce\3\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01dd\3")
        buf.write("\2\2\2\u0091\u01df\3\2\2\2\u0093\u01ea\3\2\2\2\u0095\u01fb")
        buf.write("\3\2\2\2\u0097\u0098\7D\2\2\u0098\u0099\7q\2\2\u0099\u009a")
        buf.write("\7f\2\2\u009a\u009b\7{\2\2\u009b\4\3\2\2\2\u009c\u009d")
        buf.write("\7D\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7m\2\2\u00a1\6\3\2\2\2\u00a2\u00a3")
        buf.write("\7E\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7g\2\2\u00aa\b\3\2\2\2\u00ab\u00ac")
        buf.write("\7F\2\2\u00ac\u00ad\7q\2\2\u00ad\n\3\2\2\2\u00ae\u00af")
        buf.write("\7G\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\f\3\2\2\2\u00b3\u00b4\7G\2\2\u00b4\u00b5")
        buf.write("\7n\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7K\2\2\u00b8\u00b9\7h\2\2\u00b9\16\3\2\2\2\u00ba\u00bb")
        buf.write("\7G\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7f\2\2\u00bd\u00be")
        buf.write("\7D\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1")
        buf.write("\7{\2\2\u00c1\20\3\2\2\2\u00c2\u00c3\7G\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7f\2\2\u00c5\u00c6\7K\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7\22\3\2\2\2\u00c8\u00c9\7G\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7H\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7t\2\2\u00ce\24\3\2\2\2\u00cf\u00d0")
        buf.write("\7G\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3")
        buf.write("\7Y\2\2\u00d3\u00d4\7j\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7n\2\2\u00d6\u00d7\7g\2\2\u00d7\26\3\2\2\2\u00d8\u00d9")
        buf.write("\7H\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7t\2\2\u00db\30")
        buf.write("\3\2\2\2\u00dc\u00dd\7H\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\32")
        buf.write("\3\2\2\2\u00e5\u00e6\7K\2\2\u00e6\u00e7\7h\2\2\u00e7\34")
        buf.write("\3\2\2\2\u00e8\u00e9\7R\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7o\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7p\2\2\u00f8 \3\2\2\2\u00f9\u00fa")
        buf.write("\7V\2\2\u00fa\u00fb\7j\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7X\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7t\2\2\u0101$\3\2\2\2\u0102\u0103")
        buf.write("\7Y\2\2\u0103\u0104\7j\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7n\2\2\u0106\u0107\7g\2\2\u0107&\3\2\2\2\u0108\u0109")
        buf.write("\7V\2\2\u0109\u010a\7t\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c(\3\2\2\2\u010d\u010e\7H\2\2\u010e\u010f")
        buf.write("\7c\2\2\u010f\u0110\7n\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112*\3\2\2\2\u0113\u0114\7G\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7f\2\2\u0116\u0117\7F\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118,\3\2\2\2\u0119\u011a\7-\2\2\u011a.\3\2\2")
        buf.write("\2\u011b\u011c\7-\2\2\u011c\u011d\7\60\2\2\u011d\60\3")
        buf.write("\2\2\2\u011e\u011f\7/\2\2\u011f\62\3\2\2\2\u0120\u0121")
        buf.write("\7/\2\2\u0121\u0122\7\60\2\2\u0122\64\3\2\2\2\u0123\u0124")
        buf.write("\7,\2\2\u0124\66\3\2\2\2\u0125\u0126\7,\2\2\u0126\u0127")
        buf.write("\7\60\2\2\u01278\3\2\2\2\u0128\u0129\7^\2\2\u0129:\3\2")
        buf.write("\2\2\u012a\u012b\7^\2\2\u012b\u012c\7\60\2\2\u012c<\3")
        buf.write("\2\2\2\u012d\u012e\7\'\2\2\u012e>\3\2\2\2\u012f\u0130")
        buf.write("\7#\2\2\u0130@\3\2\2\2\u0131\u0132\7(\2\2\u0132\u0133")
        buf.write("\7(\2\2\u0133B\3\2\2\2\u0134\u0135\7~\2\2\u0135\u0136")
        buf.write("\7~\2\2\u0136D\3\2\2\2\u0137\u0138\7?\2\2\u0138\u0139")
        buf.write("\7?\2\2\u0139F\3\2\2\2\u013a\u013b\7#\2\2\u013b\u013c")
        buf.write("\7?\2\2\u013cH\3\2\2\2\u013d\u013e\7>\2\2\u013eJ\3\2\2")
        buf.write("\2\u013f\u0140\7@\2\2\u0140L\3\2\2\2\u0141\u0142\7>\2")
        buf.write("\2\u0142\u0143\7?\2\2\u0143N\3\2\2\2\u0144\u0145\7@\2")
        buf.write("\2\u0145\u0146\7?\2\2\u0146P\3\2\2\2\u0147\u0148\7?\2")
        buf.write("\2\u0148\u0149\7\61\2\2\u0149\u014a\7?\2\2\u014aR\3\2")
        buf.write("\2\2\u014b\u014c\7>\2\2\u014c\u014d\7\60\2\2\u014dT\3")
        buf.write("\2\2\2\u014e\u014f\7@\2\2\u014f\u0150\7\60\2\2\u0150V")
        buf.write("\3\2\2\2\u0151\u0152\7>\2\2\u0152\u0153\7?\2\2\u0153\u0154")
        buf.write("\7\60\2\2\u0154X\3\2\2\2\u0155\u0156\7@\2\2\u0156\u0157")
        buf.write("\7?\2\2\u0157\u0158\7\60\2\2\u0158Z\3\2\2\2\u0159\u015a")
        buf.write("\7?\2\2\u015a\\\3\2\2\2\u015b\u015c\7*\2\2\u015c^\3\2")
        buf.write("\2\2\u015d\u015e\7+\2\2\u015e`\3\2\2\2\u015f\u0160\7}")
        buf.write("\2\2\u0160b\3\2\2\2\u0161\u0162\7\177\2\2\u0162d\3\2\2")
        buf.write("\2\u0163\u0164\7]\2\2\u0164f\3\2\2\2\u0165\u0166\7_\2")
        buf.write("\2\u0166h\3\2\2\2\u0167\u0168\7<\2\2\u0168j\3\2\2\2\u0169")
        buf.write("\u016a\7\60\2\2\u016al\3\2\2\2\u016b\u016c\7.\2\2\u016c")
        buf.write("n\3\2\2\2\u016d\u016e\7=\2\2\u016ep\3\2\2\2\u016f\u0173")
        buf.write("\t\2\2\2\u0170\u0172\t\3\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174r\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7,\2\2")
        buf.write("\u0177\u0178\7,\2\2\u0178\u017c\3\2\2\2\u0179\u017b\13")
        buf.write("\2\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0180\7,\2\2\u0180\u0181\7,\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0183\b:\2\2\u0183t\3\2\2\2\u0184")
        buf.write("\u0186\t\4\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u018a\b;\2\2\u018av\3\2\2\2\u018b\u018c\t")
        buf.write("\5\2\2\u018cx\3\2\2\2\u018d\u0191\t\6\2\2\u018e\u0190")
        buf.write("\5w<\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0196\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0194\u0196\7\62\2\2\u0195\u018d\3\2\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196z\3\2\2\2\u0197\u0198\7\62")
        buf.write("\2\2\u0198\u019a\t\7\2\2\u0199\u019b\t\b\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d|\3\2\2\2\u019e\u019f\7\62\2\2\u019f")
        buf.write("\u01a1\t\t\2\2\u01a0\u01a2\t\n\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4~\3\2\2\2\u01a5\u01a9\5y=\2\u01a6\u01a9\5")
        buf.write("{>\2\u01a7\u01a9\5}?\2\u01a8\u01a5\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9\u0080\3\2\2\2\u01aa")
        buf.write("\u01ae\7\60\2\2\u01ab\u01ad\5w<\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u0082\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3")
        buf.write("\t\13\2\2\u01b2\u01b4\t\f\2\2\u01b3\u01b2\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b7\5w<\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u0084\3\2\2\2\u01ba\u01bc\5")
        buf.write("y=\2\u01bb\u01bd\5\u0081A\2\u01bc\u01bb\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\5\u0083")
        buf.write("B\2\u01bf\u01c6\3\2\2\2\u01c0\u01c1\5y=\2\u01c1\u01c3")
        buf.write("\5\u0081A\2\u01c2\u01c4\5\u0083B\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01ba\3")
        buf.write("\2\2\2\u01c5\u01c0\3\2\2\2\u01c6\u0086\3\2\2\2\u01c7\u01ca")
        buf.write("\5\'\24\2\u01c8\u01ca\5)\25\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u0088\3\2\2\2\u01cb\u01cc\7)\2\2")
        buf.write("\u01cc\u01cd\7$\2\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\7")
        buf.write("^\2\2\u01cf\u01d0\t\r\2\2\u01d0\u008c\3\2\2\2\u01d1\u01d7")
        buf.write("\7$\2\2\u01d2\u01d6\n\16\2\2\u01d3\u01d6\5\u008bF\2\u01d4")
        buf.write("\u01d6\5\u0089E\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2")
        buf.write("\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01da\u01db\7$\2\2\u01db\u01dc\bG\3\2\u01dc")
        buf.write("\u008e\3\2\2\2\u01dd\u01de\13\2\2\2\u01de\u0090\3\2\2")
        buf.write("\2\u01df\u01e5\7$\2\2\u01e0\u01e4\n\16\2\2\u01e1\u01e4")
        buf.write("\5\u008bF\2\u01e2\u01e4\5\u0089E\2\u01e3\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7\3")
        buf.write("\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\bI\4\2\u01e9")
        buf.write("\u0092\3\2\2\2\u01ea\u01f0\7$\2\2\u01eb\u01ef\n\16\2\2")
        buf.write("\u01ec\u01ef\5\u008bF\2\u01ed\u01ef\5\u0089E\2\u01ee\u01eb")
        buf.write("\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef")
        buf.write("\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f7\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\7")
        buf.write("^\2\2\u01f4\u01f8\n\r\2\2\u01f5\u01f6\7)\2\2\u01f6\u01f8")
        buf.write("\n\17\2\2\u01f7\u01f3\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fa\bJ\5\2\u01fa\u0094\3\2\2\2")
        buf.write("\u01fb\u01fc\7,\2\2\u01fc\u01fd\7,\2\2\u01fd\u0201\3\2")
        buf.write("\2\2\u01fe\u0200\13\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0203")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0201\u01ff\3\2\2\2\u0202")
        buf.write("\u0096\3\2\2\2\u0203\u0201\3\2\2\2\32\2\u0173\u017c\u0187")
        buf.write("\u0191\u0195\u019c\u01a3\u01a8\u01ae\u01b3\u01b8\u01bc")
        buf.write("\u01c3\u01c5\u01c9\u01d5\u01d7\u01e3\u01e5\u01ee\u01f0")
        buf.write("\u01f7\u0201\6\b\2\2\3G\2\3I\3\3J\4")
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
    BOOL_LIT = 61
    STRING_LIT = 62
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
            "COMMA", "SEMI", "ID", "COMMENT", "WS", "INT_LIT", "FLOAT_LIT", 
            "BOOL_LIT", "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
                  "BOOL_LIT", "ESCAPE_QUOTE", "ESCAPE_CHAR", "STRING_LIT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            actions[69] = self.STRING_LIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
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
     


