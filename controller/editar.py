from flask import session, redirect, url_for, render_template
from models.Jogos import Jogos
from helpers import FormularioJogo, recupera_imagem

def editar_route(id):
    print(session)
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('To aquiiiiiiiiiiiii')
        return redirect(url_for('login'))
    
    jogo = Jogos.query.filter_by(user_id=id).first()
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    capa_jogo = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Jogo', user_id=id, capa_jogo=capa_jogo, form=form)
