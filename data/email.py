import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		email = ui.dialog1()
		r=requests.get(f'https://dualityapi.xyz/apis/teste/Consultas%20Privadas/HTML/email.php?consulta={email}').text
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o Email inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n').replace('CPF', '\nCPF')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
