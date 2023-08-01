from app import app 

@app.route('/')


def index():
    return '''Olá mundo!'''

@app.route('/contato')
def contato():
    return 'Meu contato: (84) 98111-0891'

@app.route('/sobre')
def sobre():
    return 'Meu nome é Maria Eduarda, aluna do Senac'