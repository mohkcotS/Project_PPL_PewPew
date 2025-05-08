# Generated from q3.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\16\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\2")
        buf.write("\2\4\2\4\2\2\2\13\2\6\3\2\2\2\4\b\3\2\2\2\6\7\5\4\3\2")
        buf.write("\7\3\3\2\2\2\b\t\7\3\2\2\t\n\7\4\2\2\n\13\7\5\2\2\13\f")
        buf.write("\7\6\2\2\f\5\3\2\2\2\2")
        return buf.getvalue()


class q3Parser ( Parser ):

    grammarFileName = "q3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'?'" ]

    symbolicNames = [ "<INVALID>", "CAN_COULD_SHOULD_WOULD", "SUBJECT", 
                      "VERB", "Q_Mask", "WS" ]

    RULE_program = 0
    RULE_sentence = 1

    ruleNames =  [ "program", "sentence" ]

    EOF = Token.EOF
    CAN_COULD_SHOULD_WOULD=1
    SUBJECT=2
    VERB=3
    Q_Mask=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(q3Parser.SentenceContext,0)


        def getRuleIndex(self):
            return q3Parser.RULE_program




    def program(self):

        localctx = q3Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.sentence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAN_COULD_SHOULD_WOULD(self):
            return self.getToken(q3Parser.CAN_COULD_SHOULD_WOULD, 0)

        def SUBJECT(self):
            return self.getToken(q3Parser.SUBJECT, 0)

        def VERB(self):
            return self.getToken(q3Parser.VERB, 0)

        def Q_Mask(self):
            return self.getToken(q3Parser.Q_Mask, 0)

        def getRuleIndex(self):
            return q3Parser.RULE_sentence




    def sentence(self):

        localctx = q3Parser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(q3Parser.CAN_COULD_SHOULD_WOULD)
            self.state = 7
            self.match(q3Parser.SUBJECT)
            self.state = 8
            self.match(q3Parser.VERB)
            self.state = 9
            self.match(q3Parser.Q_Mask)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





