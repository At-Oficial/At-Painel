import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cpf= int(ui.dialog1())
		r = requests.get(f'https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/cpf.php?consulta={cpf}').text
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o CPF inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n').replace('DDD:', 'DDD: ').replace('NOME:', 'Nome completo: ').replace('FONE:', 'Telefone: ').replace('INST:', 'Data de Compra: ').replace('PESSOA:', 'Pessoa: ').replace('CPF:', 'CPF: ').replace('PESSOA:', 'Pessoa: ')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
