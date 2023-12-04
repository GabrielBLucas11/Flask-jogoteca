from flask import session, flash, redirect, url_for

def logout_routes():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))
