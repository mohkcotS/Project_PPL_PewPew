# Generated from q1.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\32\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\6\5\25\n\5\r\5\16\5\26\3\5\3\5")
        buf.write("\2\2\6\3\3\5\4\7\5\t\6\3\2\4\3\2c|\5\2\13\f\17\17\"\"")
        buf.write("\2\32\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\3\13\3\2\2\2\5\17\3\2\2\2\7\21\3\2\2\2\t\24\3\2\2\2\13")
        buf.write("\f\7C\2\2\f\r\7t\2\2\r\16\7g\2\2\16\4\3\2\2\2\17\20\t")
        buf.write("\2\2\2\20\6\3\2\2\2\21\22\7A\2\2\22\b\3\2\2\2\23\25\t")
        buf.write("\3\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\31\b\5\2\2\31\n\3\2\2\2\4\2")
        buf.write("\26\3\b\2\2")
        return buf.getvalue()


class q1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARE = 1
    ID = 2
    Q_Mask = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Are'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "ARE", "ID", "Q_Mask", "WS" ]

    ruleNames = [ "ARE", "ID", "Q_Mask", "WS" ]

    grammarFileName = "q1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


