from flask import request, redirect, url_for
from helpers import FormularioJogo, deleta_arquivo
from jogoteca import db, app
from models.Jogos import Jogos
import time

def atualizar_route():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(user_id=request.form['user_id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(jogo.user_id)
        arquivo.save(f'{upload_path}/capa{jogo.user_id}-{timestamp}.jpg')

    
    return redirect(url_for('index'))