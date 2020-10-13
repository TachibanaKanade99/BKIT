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

// Parser:

// Program Structure:
program: many_declars EOF;
many_declars: global_var_declar_lst func_declar_lst main_func;

// Global variable declaration:
global_var_declar_lst: var_decl many_var_decl | ;
many_var_decl: var_decl many_var_decl | ;

// Variable declaration:
var_decl: VAR COLON var_lst;
var_lst: var many_var;
many_var: COMMA var many_var | ;

// Variable:
var: ( ID | composite_var ) EQ LIT;
composite_var: ID dimension_lst;
dimension_lst: dimension many_dimension;
many_dimension: dimension many_dimension | ;
dimension: LSB INT_LIT RSB;

// Function Delcaration:
func_declar_lst: func_decl many_func_decl | ;
many_func_decl: func_decl many_func_decl | ;
func_decl: FUNCTION COLON func_name func_param? body;
func_name: ID;

// Function parameter:
func_param: PARAMETER COLON param_lst;
param_lst: param many_params;
many_params: COMMA param many_params | ;
param: ID | composite_var;

// Function Body:
body: BODY COLON stmt_lst ENDBODY DOT;
stmt_lst: stmt many_stmts | ;
many_stmts: stmt many_stmts | ;

// Main function:
main_func: FUNCTION COLON 'main' body;

// Expression:

// Function call:
func_call: ID LP argument_lst RP;
argument_lst: argument many_arguments | ;
many_arguments: argument many_arguments | ;
argument: .;

// Index operators:
ele_expr: expr index_op;
index_op: LSB expr RSB | LSB expr RSB index_op;

expr: .;

// Statement:
stmt: .;

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

// Identifiers:
ID: [a-z][a-zA-Z_0-9]*;

COMMENT: '**' .*? '**' -> skip; // comment
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

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
fragment ESCAPE_QUOTE: '\'' '"';
fragment ESCAPE_CHAR: '\\' ( [bfrnt'\\] ); 
STRING_LIT: '"' ( ~['"\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* '"' {self.text = self.text[1:-1]};

LIT: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT;

// Array Literals:
array_lit: LB lit_list RB;
lit_list: LIT many_lits;
many_lits: COMMA LIT many_lits | ;


ERROR_CHAR: .;
// UNCLOSE_STRING: .;
UNCLOSE_STRING: '"' ( ~['"\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* {self.text = self.text[1:]};
ILLEGAL_ESCAPE: '"' ( ~['"\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* ( '\\' ~ ( [bfrnt\\] | '\'' ) ) {self.text = self.text[1:]};
UNTERMINATED_COMMENT: '**' .*?;
