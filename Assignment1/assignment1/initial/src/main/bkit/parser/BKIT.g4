// ID: 1752595
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program: VAR COLON ID SEMI EOF ;

// Lexical:

// Keywords:

BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';

// Operators:
PLUS: '+';
FLOAT_PLUS: '+.';
MINUS: '-';
FLOAT_MINUS: '-.';
MUL: '*';
FLOAT_MUL: '*.';
DIV: '\\';
FLOAT_DIV: '\\.';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';
LESS: '<';
GREATER: '>';
LESS_EQ: '<=';
GREATER_EQ: '>=';
FLOAT_NOT_EQ: '=/=';
FLOAT_LESS: '<.';
FLOAT_GREATER: '>.';
FLOAT_LESS_EQ: '<=.';
FLOAT_GREATER_EQ: '>=.';
ASSIGN: '=';

// Separators:
LP: '(';
RP: ')';
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
COLON: ':';
DOT: '.';
COMMA: ',';
SEMI: ';';

// Literals:



// Identifiers:
ID: [a-z][a-zA-Z_0-9]*;

COMMENT: '**' .*? '**' -> skip; // comment
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;