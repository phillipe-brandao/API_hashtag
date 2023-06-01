# API_hashtag
O projeto contem uma API desenvolvida para participação do processo seletivo da Hashtag Treinamentos.

# Orientações:
Sua API deve ser construída usando Flask

Simulador dos webhooks:
https://simuladorwebhook-production.up.railway.app/

- A gente precisa criar um sistema que recebe um webhook do sistema de pagamento e decida como vamos tratar o cliente

- se o cliente tem o pagamento aprovado, então devemos:
	- liberar o acesso dele ao curso
	- enviar mensagem de boas vindas
- se o cliente tem o pagamento recusado
	- enviar mensagem de pagamento recusado
- se o cliente tem o status reembolsado
	- tirar o acesso dele ao curso
- Precisamos ter registrado (para poder consultar quando precisarmos) todos os webhooks que chegaram e todas as "tratativas" que o sistema fez.
	Ex: se o sistema mandou liberar o acesso ao curso e enviou mensagem, tem que ter um registro que o sistema fez isso (no banco de dados mesmo)
- o sistema precisa ter autenticação de login para só poder entrar usuários autorizados. A criação de conta só pode ser feita por usuários que tenham o token: uhdfaAADF123 que deve ser enviado junto do formulário de criação de conta
- os usuários devem ter 1 tela onde possam ver todas as tratativas que o sistema fez para cada usuário e que seja possível pesquisar por um usuário e ver o que rolou com ele

As funcionalidades de enviar mensagem, tirar acesso e liberar acesso não precisam "fazer nada", só precisam "printar o que seria feito", do tipo:
print("Liberar acesso do e-mail: fulano@email.com")
ou então
print("Enviar mensagem de boas vindas para o email: fulano@email.com")
