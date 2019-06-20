import pickle

nome = 0
telefone = 0
email = 0
site = 0
nascimento = 0
pausa = 0
salvar = 0
agenda = []

while (pausa != "fim"):
    nome = input("Digite seu nome: ")
    agenda.append(nome)
    telefone = input("Digte seu numero: ")
    agenda.append(telefone)
    email = input("Digite seu email: ")
    agenda.append(email)
    site = input("Digite seu site: ")
    agenda.append(site)
    nascimento = input("Data de nascimento: ")
    agenda.append(nascimento)
	
    salvar = str(input("Se deseja salvar os dados digite SIM: "))
    if salvar == "sim":
	
        pickle.dump(agenda, open("agenda.txt", "wb"))
    pausa = str(input("para finalizar o cadastro digite FIM: "))

agenda = pickle.load(open("agenda.txt", "rb"))
print(agenda)

for i in agenda:
    print(i)