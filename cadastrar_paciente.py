import pickle

# Função para cadastro de paciente

def cadastrar_paciente():

    nomes = []
    emails = []
    fones = []
    rgs = []
    cpfs = []
    enderecos = []
    numeros = []
    bairros = []
    cidades = []
    ufs = []
    plaSaudes = []

    while (True):
        print('\nCADASTRAR DADOS DO PACIENTE\n')

        nome = str(input("Nome: ")).title()
        nomes.append(nome)
        email = str(input("E-mail: ")).lower()
        emails.append(email)
        fone = str(input("Telefone: "))
        fones.append(fone)
        rg = str(input("RG: "))
        rgs.append(rg)
        cpf = str(input("CPF: "))
        cpfs.append(cpf)
        endereco = str(input("Endereço: ")).title()
        enderecos.append(endereco)
        numero = str(input('Número: '))
        numeros.append(numero)
        bairro = str(input("Bairro: ")).title()
        bairros.append(bairro)
        cidade = str(input("Cidade: ")).title()
        cidades.append(cidade)
        uf = str(input("UF: ")).title().title()
        ufs.append(uf)
        plaSaude = str(input("Plano de Saúde: ")).title()
        plaSaudes.append(plaSaude)


        terminou = str(input("\nFinalizar? [s]/ [n]: ")).lower()
        if terminou == "s":
            break

    paciente = []
    for i in nomes,emails,fones,rgs,cpfs,enderecos,numeros,bairros,cidades,ufs,plaSaudes:
        paciente.append(i)
    pickle.dump(paciente,open("paciente.txt", "wb"))

    lista_paciente = pickle.load(open("paciente.txt", "rb"))
    print(lista_paciente,'\n')
    print()

    for i in lista_paciente:
        print(i)

print(cadastrar_paciente())
