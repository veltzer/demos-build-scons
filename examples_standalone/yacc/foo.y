/* File: ex.y */

%{
	int vbltable[26];
	void yyerror (char const *s);
	int yylex();
%}


%token  NAME 
%token  NUMBER
%token  EQ
%token PLUS MINUS TIMES DIV
%left MINUS PLUS
%left TIMES DIV 
%nonassoc UMINUS

%%

statement_list
        : statement 
        | statement statement_list

statement
        : NAME EQ expression ';' {vbltable[$1] = $3; }
        

expression
        : expression PLUS expression {$$ = $1 + $3;}
        | expression MINUS expression {$$ = $1 - $3;}
        | expression TIMES expression {$$ = $1 * $3;}
        | expression DIV   expression {$$ = $1 / $3;}
        | MINUS expression %prec UMINUS {$$ = - $2;}    
        | '(' expression ')' { $$ = $2; } 
        | NUMBER
        | NAME   { $$ = vbltable[$1]; }
        
%%

void yyerror (char const *s) {
	//fprintf (stderr, "%s\n", s);
}

int yylex() {
	return 0;
}
