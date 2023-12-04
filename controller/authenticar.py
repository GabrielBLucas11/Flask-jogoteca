from helpers import FormularioUsuario
from flask import request, session, flash, redirect, url_for
from models.Usuarios import Usuarios

def authenticar_route():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname = form.nickname.data).first()
    if usuario:
        if form.senha.data == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))
