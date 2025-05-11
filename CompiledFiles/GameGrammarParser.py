# Generated from GameGrammar.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2(\2\20\3\2\2\2")
        buf.write("\4\30\3\2\2\2\6\32\3\2\2\2\b\35\3\2\2\2\n \3\2\2\2\f$")
        buf.write("\3\2\2\2\16\'\3\2\2\2\20\21\5\4\3\2\21\22\7\2\2\3\22\3")
        buf.write("\3\2\2\2\23\31\5\6\4\2\24\31\5\b\5\2\25\31\5\n\6\2\26")
        buf.write("\31\5\f\7\2\27\31\5\16\b\2\30\23\3\2\2\2\30\24\3\2\2\2")
        buf.write("\30\25\3\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2")
        buf.write("\2\32\33\7\3\2\2\33\34\7\7\2\2\34\7\3\2\2\2\35\36\7\4")
        buf.write("\2\2\36\37\7\t\2\2\37\t\3\2\2\2 !\7\4\2\2!\"\7\b\2\2\"")
        buf.write("#\7\7\2\2#\13\3\2\2\2$%\7\5\2\2%&\7\n\2\2&\r\3\2\2\2\'")
        buf.write("(\7\6\2\2()\7\7\2\2)*\7\13\2\2*\17\3\2\2\2\3\30")
        return buf.getvalue()


class GameGrammarParser ( Parser ):

    grammarFileName = "GameGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'defend'", "'use'", "'collect'", "'attack'", 
                     "<INVALID>", "<INVALID>", "'heal'" ]

    symbolicNames = [ "<INVALID>", "DEFEND", "USE", "COLLECT", "ATTACK", 
                      "DIRECTION", "SKILL", "HEAL", "BUFF", "ID", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_defendCommand = 2
    RULE_useHealCommand = 3
    RULE_useSkillDirectionCommand = 4
    RULE_collectCommand = 5
    RULE_attackCommand = 6

    ruleNames =  [ "program", "sentence", "defendCommand", "useHealCommand", 
                   "useSkillDirectionCommand", "collectCommand", "attackCommand" ]

    EOF = Token.EOF
    DEFEND=1
    USE=2
    COLLECT=3
    ATTACK=4
    DIRECTION=5
    SKILL=6
    HEAL=7
    BUFF=8
    ID=9
    WS=10

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
            return self.getTypedRuleContext(GameGrammarParser.SentenceContext,0)


        def EOF(self):
            return self.getToken(GameGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_program




    def program(self):

        localctx = GameGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.sentence()
            self.state = 15
            self.match(GameGrammarParser.EOF)
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

        def defendCommand(self):
            return self.getTypedRuleContext(GameGrammarParser.DefendCommandContext,0)


        def useHealCommand(self):
            return self.getTypedRuleContext(GameGrammarParser.UseHealCommandContext,0)


        def useSkillDirectionCommand(self):
            return self.getTypedRuleContext(GameGrammarParser.UseSkillDirectionCommandContext,0)


        def collectCommand(self):
            return self.getTypedRuleContext(GameGrammarParser.CollectCommandContext,0)


        def attackCommand(self):
            return self.getTypedRuleContext(GameGrammarParser.AttackCommandContext,0)


        def getRuleIndex(self):
            return GameGrammarParser.RULE_sentence




    def sentence(self):

        localctx = GameGrammarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.defendCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.useHealCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.useSkillDirectionCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.collectCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 21
                self.attackCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefendCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFEND(self):
            return self.getToken(GameGrammarParser.DEFEND, 0)

        def DIRECTION(self):
            return self.getToken(GameGrammarParser.DIRECTION, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_defendCommand




    def defendCommand(self):

        localctx = GameGrammarParser.DefendCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defendCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GameGrammarParser.DEFEND)
            self.state = 25
            self.match(GameGrammarParser.DIRECTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseHealCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(GameGrammarParser.USE, 0)

        def HEAL(self):
            return self.getToken(GameGrammarParser.HEAL, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_useHealCommand




    def useHealCommand(self):

        localctx = GameGrammarParser.UseHealCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_useHealCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(GameGrammarParser.USE)
            self.state = 28
            self.match(GameGrammarParser.HEAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseSkillDirectionCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(GameGrammarParser.USE, 0)

        def SKILL(self):
            return self.getToken(GameGrammarParser.SKILL, 0)

        def DIRECTION(self):
            return self.getToken(GameGrammarParser.DIRECTION, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_useSkillDirectionCommand




    def useSkillDirectionCommand(self):

        localctx = GameGrammarParser.UseSkillDirectionCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_useSkillDirectionCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(GameGrammarParser.USE)
            self.state = 31
            self.match(GameGrammarParser.SKILL)
            self.state = 32
            self.match(GameGrammarParser.DIRECTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLLECT(self):
            return self.getToken(GameGrammarParser.COLLECT, 0)

        def BUFF(self):
            return self.getToken(GameGrammarParser.BUFF, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_collectCommand




    def collectCommand(self):

        localctx = GameGrammarParser.CollectCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_collectCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GameGrammarParser.COLLECT)
            self.state = 35
            self.match(GameGrammarParser.BUFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttackCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTACK(self):
            return self.getToken(GameGrammarParser.ATTACK, 0)

        def DIRECTION(self):
            return self.getToken(GameGrammarParser.DIRECTION, 0)

        def ID(self):
            return self.getToken(GameGrammarParser.ID, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_attackCommand




    def attackCommand(self):

        localctx = GameGrammarParser.AttackCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attackCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(GameGrammarParser.ATTACK)
            self.state = 38
            self.match(GameGrammarParser.DIRECTION)
            self.state = 39
            self.match(GameGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





