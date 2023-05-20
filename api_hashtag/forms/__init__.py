from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, email, equal_to

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), length(5)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(6, 16)])
    lembrar = BooleanField('Lembrar-me')
    submit_entrar = SubmitField('Entrar')


class FormCadastroUsuario(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(6, 16)])
    confirmacao = PasswordField('Confirmação de Senha',  validators=[DataRequired(), equal_to('senha')])
    token = StringField('Token', validators=[DataRequired()])
    submit_criar = SubmitField('Criar')

class FormBuscarRequisicao(FlaskForm):
    usuario = StringField('Usuário')
    submit_buscar = SubmitField('Buscar')
