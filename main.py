import os, sys
os.system('git pull')
def restart():
	python=sys.executable;os.excl(python, python, *sys.argv)
try:
	import colorama, requests
except:
	os.system('pip install colorama requests')
try:
	from data import ui, numero, cpf, nome, rg, email,nome2,datan, cep, placa
except Exception as e:
	print('ARQUIVO CORROMPIDO! '+str(e));exit()
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
Sair=False
while(Sair==False):
	try:
		op=int(ui.menu(ms0=f'\n{C}[{G}1{C}] Numero\n{C}[{G}2{C}] CPF\n{C}[{G}3{C}] Nome\n{C}[{G}4{C}] Email[{P}OFF{C}]\n{C}[{G}5{C}] RG\n{C}[{G}6{C}] Data de Nascimento\n{C}[{G}7{C}] CEP\n{C}[{G}8{C}] Placa\n\n{C}[{P}0{C}] Sair'))
		if op==1:
			numero.consultar()
		elif op==2:
			cpf.consultar()
		elif op==3:
			choice = int(ui.menu(ms0=f'\n{C}[{G}1{C}] Nome-1\n{C}[{G}2{C}] Nome-2{C}[{P}OFF{C}]'))
			if choice ==1:
				nome.consultar()
			elif choice ==2:
				nome2.consultar()
			else:
				ui.error()
		elif op==4:
			email.consultar()
		elif op==5:
			rg.consultar()
		elif op==6:
			datan.consultar()
		elif op==7:
			cep.consultar()
		elif op==8:
			placa.consultar()
		elif op==0:
			ui.clear();Sair=True
	except:
		ui.error()
