import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cpf = ui.dialog1()
		r=requests.get(f'https://lukazinnapi.000webhostapp.com/api/consulta/cpf/cpf2.php?cpf={cpf}').text
		if 'A Consulta' in r:
			msg='A consulta está funcionando normalmente, porém o CPF não foi encontrado.'
		else:
			msg=r.replace('''"''', '').replace(',','\n').replace('}', '').replace('{', '')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
