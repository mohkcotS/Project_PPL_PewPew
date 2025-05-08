# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\6\7 \n\7\r\7\16\7!\3\7\3\7\2\2\b\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\3\2\4\3\2c|\5\2\13\f\17\17\"\"")
        buf.write("\2&\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\24\3\2\2\2\7\30")
        buf.write("\3\2\2\2\t\32\3\2\2\2\13\34\3\2\2\2\r\37\3\2\2\2\17\20")
        buf.write("\7f\2\2\20\21\7g\2\2\21\22\7h\2\2\22\4\3\2\2\2\23\25\t")
        buf.write("\2\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\6\3\2\2\2\30\31\7*\2\2\31\b\3\2\2\2\32\33")
        buf.write("\7+\2\2\33\n\3\2\2\2\34\35\7<\2\2\35\f\3\2\2\2\36 \t\3")
        buf.write("\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"")
        buf.write("#\3\2\2\2#$\b\7\2\2$\16\3\2\2\2\5\2\26!\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    ABC = 2
    BRACKET_OP = 3
    BRACKET_CLO = 4
    COLON = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "ABC", "BRACKET_OP", "BRACKET_CLO", "COLON", "WS" ]

    ruleNames = [ "DEF", "ABC", "BRACKET_OP", "BRACKET_CLO", "COLON", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


