%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token VAR
%token INT
%token STRING
%token WHILE
%token IF
%token ELSE
%token READ
%token PRINT
%token BOOL

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token LESS;
%token LESSOREQ;
%token EQ;
%token NOTEQ;
%token BIGGEROREQ;
%token DOUBLEEQ;
%token BIGGER;

%token SEMICOLON;
%token PARENTHOPEN;
%token PARENTHCLOSE;
%token BRACKETOPEN;
%token BRACKETCLOSE;
%token COMMA;
%token SQUAREOPEN
%token SQUARECLOSE

%token IDENTIFIER;
%token INTCONSTANT;
%token STRINGCONSTANT;


%start Program

%%

Program : StmtList { printf("Program -> StmtList\n"); }
        ;

StmtList : Stmt SEMICOLON { printf("StmtList -> Stmt ;\n"); }
         | Stmt SEMICOLON StmtList { printf("StmtList -> Stmt ; StmtList\n"); }
         ;

Stmt : SimplStmt { printf("Stmt -> SimplStmt\n"); }
     | StructStmt { printf("Stmt -> StructStmt\n"); }
     ;

SimplStmt : Declaration { printf("SimplStmt -> Declaration\n"); }
          | AssignStmt { printf("SimplStmt -> AssignStmt\n"); }
          | IOStmt { printf("SimplStmt -> IOStmt\n"); }
          ;

Declaration : Type IDENTIFIER { printf("Declaration -> Type Identifier\n"); }
            | Type IDENTIFIER EQ Expression { printf("Declaration -> Type Identifier = Expression\n"); }
            ;

Type : Type1 { printf("Type -> Type1\n"); }
     | ArrayDecl { printf("Type -> ArrayDecl\n"); }
     ;

Type1 : BOOL { printf("Type1 -> bool\n"); }
      | STRING { printf("Type1 -> string\n"); }
      | INT { printf("Type1 -> int\n"); }
      ;

ArrayDecl : Type1 SQUAREOPEN INTCONSTANT SQUARECLOSE { printf("ArrayDecl -> Type1 [ INT_CONSTANT ]\n"); }
          ;

AssignStmt : IDENTIFIER EQ Expression { printf("AssignStmt -> Identifier = Expression\n"); }
           ;

Expression : Expression PLUS Term { printf("Expression -> Expression + Term\n"); }
           | Expression MINUS Term { printf("Expression -> Expression - Term\n"); }
           | Term { printf("Expression -> Term\n"); }
           ;

Term : Term TIMES Factor { printf("Term -> Term * Factor\n"); }
     | Term DIV Factor { printf("Term -> Term / Factor\n"); }
     | Factor { printf("Term -> Factor\n"); }
     ;

Factor : PARENTHOPEN Expression PARENTHCLOSE { printf("Factor -> ( Expression )\n"); }
       | IDENTIFIER { printf("Factor -> Identifier\n"); }
       | INTCONSTANT { printf("Factor -> INTCONSTANT\n"); }
       ;

IOStmt : READ PARENTHOPEN IDENTIFIER PARENTHCLOSE { printf("IOStmt -> read ( Identifier )\n"); }
       | PRINT PARENTHOPEN IDENTIFIER PARENTHCLOSE { printf("IOStmt -> print ( Identifier )\n"); }
       | PRINT PARENTHOPEN STRINGCONSTANT PARENTHCLOSE { printf("IOStmt -> print ( StringConstant )\n"); }
       ;

StructStmt : CmpdStmt { printf("StructStmt -> CmpdStmt\n"); }
           | IfStmt { printf("StructStmt -> IfStmt\n"); }
           | WhileStmt { printf("StructStmt -> WhileStmt\n"); }
           ;

CmpdStmt : BRACKETOPEN StmtList BRACKETCLOSE { printf("CmpdStmt -> { StmtList }\n"); }
         ;

IfStmt : IF PARENTHOPEN Condition PARENTHCLOSE Stmt { printf("IfStmt -> if ( Condition ) Stmt\n"); }
       | IF PARENTHOPEN Condition PARENTHCLOSE Stmt ELSE Stmt { printf("IfStmt -> if ( Condition ) Stmt else Stmt\n"); }
       ;

WhileStmt : WHILE PARENTHOPEN Condition PARENTHCLOSE Stmt { printf("WhileStmt -> while ( Condition ) Stmt\n"); }


Condition : Expression Relation Expression     { printf("Condition -> Expression Relation Expression\n"); }
          ;

Relation : LESS     { printf("Relation -> <\n"); }
         | LESSOREQ     { printf("Relation -> <=\n"); }
         | DOUBLEEQ     { printf("Relation -> ==\n"); }
         | NOTEQ     { printf("Relation -> !=\n"); }
         | BIGGEROREQ     { printf("Relation -> >=\n"); }
         | BIGGER     { printf("Relation -> >\n"); }
         ;

%%

int yyerror(char *s) {
    printf("Error: %s", s);
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1)
        yyin = fopen(argv[1], "r");
    if (!yyparse())
        fprintf(stderr, "\tOK\n");
}
