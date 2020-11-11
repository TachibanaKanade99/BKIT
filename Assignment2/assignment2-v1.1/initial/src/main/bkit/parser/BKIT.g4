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
many_declars: global_var_declar_lst func_declar_lst;

// Global variable declaration:
global_var_declar_lst: var_decl many_var_decl | ;
many_var_decl: var_decl many_var_decl | ;

// Variable declaration:
var_decl: VAR COLON var_lst SEMI;
var_lst: var many_var;
many_var: COMMA var many_var | ;

// Variable:
var: ( ID | composite_var ) initial_value;
initial_value: ASSIGN lit | ;
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

stmt_lst: global_var_declar_lst other_stmt_lst;
other_stmt_lst: stmt many_stmts | ;
many_stmts: stmt many_stmts | ;

// Main function:
// main_func: FUNCTION COLON 'main' body;

// Expression:

expr: operand_1 (EQ | NOT_EQ) operand_1
    | operand_1 (LESS | GREATER) operand_1
    | operand_1 (LESS_EQ | GREATER_EQ) operand_1
    | operand_1 FLOAT_NOT_EQ operand_1
    | operand_1 (FLOAT_LESS | FLOAT_GREATER) operand_1
    | operand_1 (FLOAT_LESS_EQ | FLOAT_GREATER_EQ) operand_1
    | operand_1;
operand_1: operand_1 (AND | OR) operand_2 | operand_2;
operand_2: operand_2 (PLUS | FLOAT_PLUS | MINUS | FLOAT_MINUS) operand_3 | operand_3;
operand_3: operand_3 (MUL | FLOAT_MUL | DIV | FLOAT_DIV | MOD) operand_4 | operand_4;
operand_4: NOT operand_4 | operand_5;
operand_5: (MINUS | FLOAT_MINUS) operand_5 | index_expr;

//Index expression:
index_expr: index_expr index_ops | func_call;
// Index operators:
index_ops: LSB expr RSB | LSB expr RSB index_ops;

// Function call:
func_call: ID LP argument_lst RP | operand;
operand: lit | ID | LP expr RP;

// Function call:
argument_lst: argument many_arguments | ;
many_arguments: COMMA argument many_arguments | ;
argument: expr;


// Statement:
stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;

// Assign Statement:
assign_stmt: (ID | index_expr) ASSIGN expr SEMI;

// If Statement:
if_stmt: IF expr THEN stmt_lst elseif_stmt_lst else_stmt ENDIF DOT;

// ElseIf Statement:
elseif_stmt_lst: elseif_stmt many_elseif_stmts | ;
many_elseif_stmts: elseif_stmt many_elseif_stmts | ; 
elseif_stmt: ELSEIF expr THEN stmt_lst;

// Else Statement:
else_stmt: ELSE stmt_lst | ;

// For Statement:
for_stmt: FOR LP ID ASSIGN expr COMMA expr COMMA expr RP DO stmt_lst ENDFOR DOT;

// While Statement:
while_stmt: WHILE expr DO stmt_lst ENDWHILE DOT;

// Do While Statement:
do_while_stmt: DO stmt_lst WHILE expr ENDDO DOT;

// Break Statement:
break_stmt: BREAK SEMI;

// Continue Statement:
continue_stmt: CONTINUE SEMI;

// Call Statement:
call_stmt: ID LP expr_lst RP SEMI;
expr_lst: expr many_exprs | ;
many_exprs: COMMA expr many_exprs | ;

// Return Statement:
return_stmt: RETURN SEMI | RETURN expr SEMI;

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
fragment HEXA_DEC: '0'[Xx] [1-9A-F] [0-9A-F]*;
fragment OCTAL: '0'[oO] [1-7] [0-7]*;
INT_LIT: INT | HEXA_DEC | OCTAL;

// Float Literal:
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXPONENT_PART: [Ee] [+-]? DIGIT+;
FLOAT_LIT: DIGIT+ DECIMAL_PART? EXPONENT_PART | DIGIT+ DECIMAL_PART EXPONENT_PART?;

// Boolean Literal:
// Defined:
bool_lit: TRUE | FALSE;

// String Literals:
fragment ESCAPE_QUOTE: '\'' '"';
fragment ESCAPE_CHAR: '\\' [bfrnt'\\]; 
STRING_LIT: '"' ( ~['"\b\f\r\n\t\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* '"' {self.text = self.text[1:-1]};

// Defined:
lit: INT_LIT | FLOAT_LIT | STRING_LIT | bool_lit | array_lit;

// Array Literals:
// Defined:
array_lit: LB lit_list RB;
lit_list: lit many_lits;
many_lits: COMMA lit many_lits | ;



ERROR_CHAR: .;
UNCLOSE_STRING: '"' ( ~['"\b\f\r\n\t\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* {self.text = self.text[1:]};
ILLEGAL_ESCAPE: '"' ( ~['"\b\f\r\n\t\\] | ESCAPE_CHAR | ESCAPE_QUOTE )* ('\\' ~[bfrnt'\\] | '\'' ~["] ) {self.text = self.text[1:]};
UNTERMINATED_COMMENT: '**' .?;
