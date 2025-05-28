import sys, os
import subprocess
import unittest
from antlr4 import *


# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'D:\\Download\\antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'GameGrammar.g4'
SRC = 'GameGrammar.g4'
TESTS = os.path.join(DIR, './tests')


def printUsage():
    print('python run.py gen')
    print('python run.py test')


def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runTest(command):
    print('Running testcases...')
    
    from CompiledFiles.GameGrammarLexer import GameGrammarLexer
    from CompiledFiles.GameGrammarParser import GameGrammarParser
    from antlr4.error.ErrorListener import ErrorListener
    from antlr4 import InputStream, CommonTokenStream

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)

    # Tạo input stream từ chuỗi command
    input_stream = InputStream(command)
    lexer = GameGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GameGrammarParser(token_stream)

    # In cây parse để debug (tùy chọn)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    # Thiết lập listener để kiểm tra lỗi
    lexer = GameGrammarLexer(InputStream(command))  # reset lại input
    token_stream = CommonTokenStream(lexer)
    parser = GameGrammarParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        parser.program()
        print("Input accepted")
        return 1
    except SystemExit:
        # pass
        return 0

    printBreak()
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':       
        runTest()
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    