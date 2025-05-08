grammar Sample;

program: sentence;

sentence: DEF ABC BRACKET_OP ABC? BRACKET_CLO COLON;

DEF: 'def';
ABC: [a-z]+;

BRACKET_OP: '(';
BRACKET_CLO: ')';
COLON: ':';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines