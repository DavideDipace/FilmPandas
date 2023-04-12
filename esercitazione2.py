from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('esercitazione2.html')

@app.route('/lingua', methods = ['GET'])
def search():
    import pandas as pd
    lingua_film = request.args['lingua_film']
    Dati_Film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', delimiter = ';')
    risultato = Dati_Film[Dati_Film['Language']== lingua_film.capitalize()]
    if len(risultato) == 0:
        table = 'Film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table2.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)