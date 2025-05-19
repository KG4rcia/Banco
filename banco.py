usuarios = {}
extrato = []

def selecionarOpcao ():

    opcao = int(input('''

    Selecione a sua opção!
    =========================
    | [1] - > Fazer Cadastro.
    | [2] - > Depositar.
    | [3] - > Sacar.
    | [4] - > Extrato.
    | [5] - > Listar Usuários.
    | [6] - > Sair.
    =========================

    - > Sua Resposta: '''))

    lista_de_opcoes = (1,2,3,4,5,6)
    if opcao not in lista_de_opcoes:
        print(f"{opcao} não é uma opção válida, tente novamente.")
    else:
        mensagemDeEscolha = f'''

    =========================
    | Você escolheu {opcao}!
    =========================
        
    '''
        print(mensagemDeEscolha)
        return opcao


def funcionalidades():
    while True:
        escolhido = selecionarOpcao()
        if escolhido == 1:
            nome_usuario = input('''

    =========================
    | Para começarmos, informe o seu nome.
    =========================       

    - > Sua resposta: ''')
            
            cpf_usuario = int(input(f'''

    =========================
    | Certo, {nome_usuario}. Agora informe o seu CPF.
    =========================       

    - > Sua resposta: '''))
            
            idade_usuario = int(input('''

    =========================
    | Por último, a sua idade.
    =========================       

    - > Sua resposta: '''))
            
            usuarios[cpf_usuario] = {

                "Nome": nome_usuario,
                "Idade": idade_usuario,
                "Saldo": 0
            }
            
            retornar = input('''
    =========================                             
    | Você deseja voltar para o menu?
    =========================
                             
    - > Sua resposta (S/N): '''.lower())
            if retornar == "sim" or retornar == "s":
                continue
            else:
                print('''
    =========================                  
    | Tudo bem!
    =========================                      
    ''')
                break

        elif escolhido == 2:
            encontrarUsuario = int(input('''
                                         
    =========================                  
    | Digite seu CPF.
    ========================= 

    - > Sua resposta: '''))
            if encontrarUsuario in usuarios:
                nome = usuarios[encontrarUsuario]["Nome"]
                valorDepositar = int(input(f'''
    =========================                  
    | Olá {nome}, quanto deseja depositar?
    ========================= 

    - > Sua resposta: '''))
                usuarios[encontrarUsuario]["Saldo"] += valorDepositar
                print(f'''
                      
    =========================                  
    | O valor de R$: {usuarios[encontrarUsuario]["Saldo"]:.2f} foi depositado!
    =========================

    ''')
            else:
                print('''
 
    =========================                  
    | Esse usuário não existe, tente novamente.
    ========================= 

    ''')
        elif escolhido == 3:
            encontrandoUsuarioSaque = int(input('''

    =========================                  
    | Digite seu CPF.
    ========================= 
                                                
    - > Sua resposta: '''))
            if encontrandoUsuarioSaque in usuarios:
                nomeSaque = usuarios[encontrandoUsuarioSaque]["Nome"]
                valorSaque = int(input(f'''

    =========================                  
    | Olá {nomeSaque}, digite o valor que você deseja sacar.
    ========================= 
    
    - > Sua resposta: '''))
                if valorSaque <= usuarios[encontrandoUsuarioSaque]["Saldo"]:
                    usuarios[encontrandoUsuarioSaque]["Saldo"] -= valorSaque
                    print(f'''

    =========================                  
    | Você realizou um saque de R$: {valorSaque}, agora você tem {usuarios[encontrandoUsuarioSaque]["Saldo"]:.2f} em conta.  
    ========================= ''')
                    
                else:
                    print(f'''

    =========================                  
    | Você não tem saldo o suficiente, pois seu saldo é de {usuarios[encontrandoUsuarioSaque]["Saldo"]}
    ========================= ''')

            
        elif escolhido == 5:
            for cpf, dados in usuarios.items():
                print(f'''

    =========================
    | CPF: {cpf} | Nome: {dados["Nome"]} | Idade: {dados["Idade"]} | Saldo: R%: {dados["Saldo"]:.2f}                      
    =========================
    
    ''')
                
        elif escolhido == 6:
            print(''' 
    =========================                  
    | Tudo bem! Até logo.
    ========================= 
''')
            break

funcionalidades()