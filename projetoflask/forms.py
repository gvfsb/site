from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from projetoflask.models import Usuario


#As classes serão subclasses da classe FlaskForm, quer dizer que eles receberão o FlaskForm como herança, por isso não precisa do __init__.
class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirme a senha:', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar conta')


    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError('Esse nome já está cadastrado. Cadastre-se com outro nome ou faça login para continuar.')            


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')            


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')