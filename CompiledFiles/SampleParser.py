# Generated from Sample.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\22\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\5\3\r\n\3")
        buf.write("\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\20\2\6\3\2\2\2\4\b\3")
        buf.write("\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2\b\t\7\3\2\2\t\n\7\4\2\2")
        buf.write("\n\f\7\5\2\2\13\r\7\4\2\2\f\13\3\2\2\2\f\r\3\2\2\2\r\16")
        buf.write("\3\2\2\2\16\17\7\6\2\2\17\20\7\7\2\2\20\5\3\2\2\2\3\f")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "<INVALID>", "'('", "')'", "':'" ]

    symbolicNames = [ "<INVALID>", "DEF", "ABC", "BRACKET_OP", "BRACKET_CLO", 
                      "COLON", "WS" ]

    RULE_program = 0
    RULE_sentence = 1

    ruleNames =  [ "program", "sentence" ]

    EOF = Token.EOF
    DEF=1
    ABC=2
    BRACKET_OP=3
    BRACKET_CLO=4
    COLON=5
    WS=6

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
            return self.getTypedRuleContext(SampleParser.SentenceContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_program




    def program(self):

        localctx = SampleParser.ProgramContext(self, self._ctx, self.state)
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

        def DEF(self):
            return self.getToken(SampleParser.DEF, 0)

        def ABC(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.ABC)
            else:
                return self.getToken(SampleParser.ABC, i)

        def BRACKET_OP(self):
            return self.getToken(SampleParser.BRACKET_OP, 0)

        def BRACKET_CLO(self):
            return self.getToken(SampleParser.BRACKET_CLO, 0)

        def COLON(self):
            return self.getToken(SampleParser.COLON, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_sentence




    def sentence(self):

        localctx = SampleParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(SampleParser.DEF)
            self.state = 7
            self.match(SampleParser.ABC)
            self.state = 8
            self.match(SampleParser.BRACKET_OP)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.ABC:
                self.state = 9
                self.match(SampleParser.ABC)


            self.state = 12
            self.match(SampleParser.BRACKET_CLO)
            self.state = 13
            self.match(SampleParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





