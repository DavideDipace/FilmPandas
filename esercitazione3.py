from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', delimiter = ';')
    
@app.route('/')
def home():
    nomi_film = dati_film.drop_duplicates(subset=['Language'])
    return render_template('esercitazione3.html', list= list(nomi_film['Language']))

@app.route('/radio', methods = ['GET'])
def search():
    lingua = request.args.get('lingua')
    risultato = dati_film[dati_film['Language']== lingua.capitalize()]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table3.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)