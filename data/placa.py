import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		placa = ui.dialog1()
		r =requests.get(f'https://dualityapi.xyz/apis/flex_7/Consultas%20Privadas/HTML/placa.php?consulta={placa}').text
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, a placa inserida não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
