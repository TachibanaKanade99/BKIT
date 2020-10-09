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

// Integer Literal:
fragment DIGIT: [0-9];
fragment INT: [1-9] DIGIT* | '0';
fragment HEXA_DEC: '0'[Xx] [0-9A-F]+;
fragment OCTAL: '0'[Oo] [0-7]+;
INT_LIT: INT | HEXA_DEC | OCTAL;

// Float Literal:
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXPONENT_PART: [Ee] [+-]? DIGIT+;
FLOAT_LIT: (INT DECIMAL_PART? EXPONENT_PART) | (INT DECIMAL_PART EXPONENT_PART?);  

// Boolean Literal:
BOOL_LIT: TRUE | FALSE;

// String Literals:
STRING_LIT: '"' . | '\\' [bfrnt\'\] '"';

// Identifiers:
ID: [a-z][a-zA-Z_0-9]*;

COMMENT: '**' .*? '**' -> skip; // comment
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;