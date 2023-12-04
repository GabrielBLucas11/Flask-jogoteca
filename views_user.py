from jogoteca import app
from controller.login import login_route
from controller.authenticar import authenticar_route
from controller.logout import logout_routes

@app.route('/login')
def login():
    return login_route()

@app.route('/autenticar', methods=['POST',])
def autenticar():
    return authenticar_route()

@app.route('/logout')
def logout():
    return logout_routes()
