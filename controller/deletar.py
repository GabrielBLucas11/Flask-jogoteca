from flask import session, redirect, url_for, flash
from models.Jogos import Jogos
from jogoteca import db

def deletar_route(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    Jogos.query.filter_by(user_id=id).delete()
    db.session.commit()
    flash('Jogo deletado com Sucesso!!')
    
    return redirect(url_for('index'))
