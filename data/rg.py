import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		rg = ui.dialog1()
		r = requests.get(f'https://dualityapi.xyz/apis/teste/Consultas%20Privadas/HTML/rg.php?consulta={rg}').text
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o RG inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n').replace('CPF', '\nCPF')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
