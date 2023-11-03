from projetoflask import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))   


class Usuario(database.Model, UserMixin):
    # primary_key para identificar o usuário como usuário único.
    id = database.Column(database.Integer, primary_key=True)
    # nullable == nào pode ser vazio
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False, unique=True)
    # foto do perfil será string, porque irei armazenar o nome do arquivo. 
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor_post', lazy=True)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False )
    # 'usuario.id' classe Usuario com 'u' minúsculo, ponto o atributo que eu quero pegar da classe

    