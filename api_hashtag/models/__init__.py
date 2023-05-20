from time import timezone

import pytz

from api_hashtag import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    def get_dict(self):
        dict = {'id':self.id, 'email':self.email}
        return dict

class Requisicao(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    status = database.Column(database.String, nullable=False)
    valor = database.Column(database.Float, nullable=False)
    forma_pagamento = database.Column(database.String, nullable=False)
    parcelas = database.Column(database.Integer, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now)
    tratativa = database.Column(database.String, nullable=False)

    def verificar_tratativa(self):
        if self.status == 'aprovado':
            self.tratativa = 'Acesso ao curso liberado. Seja bem vindo!'
        elif self.status == 'recusado':
            self.tratativa = 'Pagamento Recusado'
        elif self.status == 'reembolsado':
            self.tratativa = 'Pagamento Reembolsado. Acesso ao curso removido'
        else:
            self.tratativa = 'Tratativa inválida'

    def data_formatada(self):
        data = self.data_criacao.strftime('%d/%m/%Y %H:%M')
        return data

