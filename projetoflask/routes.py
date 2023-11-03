from flask import render_template, url_for, request, flash, redirect
from projetoflask.forms import FormLogin, FormCriarConta, FormEditarPerfil
from projetoflask import app, database, bcrypt
from projetoflask.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required

lista_usuarios = ['Gabriel', 'Walisson', 'Luiz', 'Ricardo', 'João']

# Atribuindo uma nova funcionalidade para funcionalidade abaixo.


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    # Fez login com sucesso.
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(
                f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            param_url = request.args.get('next')
            if param_url:
                return redirect(param_url)
            else:
                return redirect(url_for('homepage'))
        else:
            flash(f'Falha no login. E-mail ou senha incorretos.', 'alert-danger')

    # Criou a conta com sucesso.
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso com e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('homepage'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)
    # Passando a váriavel foto_perfil para o arquivo perfil.html


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html')


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form_editarperfil = FormEditarPerfil()
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form_editarperfil=form_editarperfil)
