from flask import request, render_template
from helpers import FormularioUsuario

def login_route():
    proxima = request.args.get('proxima')
    form_user = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form_user)
