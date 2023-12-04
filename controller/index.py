from flask import render_template
from models.Jogos import Jogos

def index_route():
    lista = Jogos.query.order_by(Jogos.user_id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)
