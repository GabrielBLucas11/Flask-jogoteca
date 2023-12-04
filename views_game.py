from flask import send_from_directory
from jogoteca import app
from controller.novo import novo_route
from controller.criar import criar_route
from controller.editar import editar_route
from controller.atualizar import atualizar_route
from controller.deletar import deletar_route
from controller.index import index_route

@app.route('/')
def index():
    return index_route()

@app.route('/novo')
def novo():
    return novo_route()

@app.route('/editar/<int:id>')
def editar(id):
    return editar_route(id)

@app.route('/criar', methods=['POST',])
def criar():
    return criar_route()

@app.route('/atualizar', methods=['POST',])
def atualizar():
    return atualizar_route()

@app.route('/deletar/<int:id>')
def deletar(id):
    return deletar_route(id)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

