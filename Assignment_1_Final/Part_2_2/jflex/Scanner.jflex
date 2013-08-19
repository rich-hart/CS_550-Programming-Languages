package Example;

import java_cup.runtime.SymbolFactory;
%%
%cup
%class Scanner
%{
	public Scanner(java.io.InputStream r, SymbolFactory sf){
		this(r);
		this.sf=sf;
	}
	private SymbolFactory sf;
%}
%eofval{
    return sf.newSymbol("EOF",sym.EOF);
%eofval}

%%
"," { return sf.newSymbol("Comma",sym.COMMA, new String(yytext())); }
"(" { return sf.newSymbol("Left Bracket",sym.LPAREN, new String(yytext())); }
")" { return sf.newSymbol("Right Bracket",sym.RPAREN, new String(yytext())); }
[0-9]+ { return sf.newSymbol("Integral Number",sym.NUMBER, new String(yytext())); }
[ \t\r\n\f] { /* ignore white space. */ }
. { System.err.println("Illegal character: "+yytext()); }
