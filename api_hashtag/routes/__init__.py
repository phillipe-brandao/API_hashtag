from flask import render_template, flash, redirect, url_for, make_response, jsonify, request
from api_hashtag import app, token_cadastro, bcrypt, database
from api_hashtag.forms import FormLogin, FormCadastroUsuario, FormBuscarRequisicao
from api_hashtag.models import Usuario, Requisicao
from flask_login import login_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario, remember=form.lembrar.data)
            print(form.email.data)
            flash(f'Login feito com sucesso para usuario: {form.email.data}', 'alert-success')
            return redirect(url_for('requisicoes'))
        else:
            flash(f'Usuário ou senha incorreto', 'alert-danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f'Sessão finalizada', 'alert alert-info')
    return redirect(url_for('login'))


@app.route("/get-usuarios", methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for item in usuarios:
        resultado.append(item.get_dict())
    print(resultado)
    return make_response(jsonify(resultado))

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastrar_usuario():
    form = FormCadastroUsuario()
    if form.validate_on_submit():
        if form.token.data == token_cadastro:
            senha_crypto = bcrypt.generate_password_hash(form.senha.data)
            novo_user = Usuario(email=form.email.data, senha=senha_crypto)
            database.session.add(novo_user)
            database.session.commit()
            flash(f'Usuário cadastrado com sucesso: {form.email.data}', 'alert-success')
            print(form.token.data)
            return redirect(url_for('cadastrar_usuario'))
        else:
            flash(f'Token inválido', 'alert-danger')
            return redirect(url_for('cadastrar_usuario'))
    return render_template('cadastrar_usuario.html', form=form)

@app.route("/requisicao", methods=['POST'])
def registrar_requisicao():
    try:
        dados = request.json
        requisicao = Requisicao(nome=dados['nome'],
                                email=dados['email'],
                                status=dados['status'],
                                valor=dados['valor'],
                                forma_pagamento=dados['forma_pagamento'],
                                parcelas=dados['parcelas'],
                                tratativa=None)
        requisicao.verificar_tratativa()
        database.session.add(requisicao)
        database.session.commit()
        print(f'Recebimento de Webhook - E-mail: {requisicao.email} > {requisicao.tratativa}')
        return make_response(
            jsonify(
                mensagem=requisicao.tratativa,
                status=requisicao.status
            )
        )
    except:
        return make_response(
            jsonify(
                mensagem='Não foi possível registrar a requisição',
                status='ERRO'
            )
        )


@app.route("/requisicoes", methods=['POST', 'GET'])
@login_required
def requisicoes():
    form = FormBuscarRequisicao()
    requisicoes = Requisicao.query.all()
    if form.validate_on_submit():
        if form.usuario.data:
            return redirect(url_for('requisicoes_busca', usuario=form.usuario.data))
        else:
            return redirect(url_for('requisicoes'))
    return render_template('requisicoes.html', requisicoes=requisicoes, form=form)


@app.route("/requisicoes/<usuario>", methods=['POST', 'GET'])
@login_required
def requisicoes_busca(usuario):
    form = FormBuscarRequisicao()
    if usuario:
        requisicoes = Requisicao.query.filter_by(nome=usuario).all()
    if form.validate_on_submit():
        if form.usuario.data:
            return redirect(url_for('requisicoes_busca', usuario=form.usuario.data))
        else:
            return redirect(url_for('requisicoes'))
    return render_template('requisicoes.html', requisicoes=requisicoes, form=form)