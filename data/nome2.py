import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		nome = ui.dialog1()
		r =requests.get(f'https://dualityapi.xyz/apis/teste/Consultas%20Privadas/HTML/nome_limitado.php?consulta={nome}').text
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o Nome inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
