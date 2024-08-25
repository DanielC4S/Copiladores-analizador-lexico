import ply.lex as lex
from flask import Flask, render_template, request

app = Flask(__name__)

reserved = {
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'if' : 'IF',
    'else' : 'ELSE'
}

tokens = ['PABIERTO','PCERRADO'] + list(reserved.values())

t_FOR = r'for'
t_WHILE = r'while'
t_DO = r'do'
t_IF = r'if'
t_ELSE = r'else'
t_ignore = ' \t\n\r'

t_PABIERTO = r'\('
t_PCERRADO = r'\)'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        expresion = request.form.get('Expresion')
        lexer.input(expresion)
 
        result_lexema = [
            (f"Reservada {expresion.type.capitalize()}" if expresion.type in reserved.values() else "Parentesis de apertura" if expresion.type == "PABIERTO" else "Parentesis de cierre", expresion.value)
            for expresion in lexer
        ]
        return render_template('index.html', tokens=result_lexema, expresion=expresion)
    return render_template('index.html', expresion=None)