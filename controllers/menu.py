from services.crud import adicionar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

adicionar_cliente('Pedro Carlos', 'pedrocarlinhos@gmail.com', '6198775323', 'QC 8')


def exibir_menu():
    print('\n' + '='*40)
    print('📋  MENU PRINCIPAL - CADASTRO DE CLIENTES')
    print('='*40)
    print('1️⃣    Adicionar cliente')
    print('2️⃣    Listar cliente')
    print('3️⃣    Atualiza cliente')
    print('4️⃣    Deletar cliente')
    print('0️⃣    Sair')
    print('='*40)
    
def menu():
    while True:
        exibir_menu()
        opcao = input('⌨    Digite uma opção: ').strip()
        
        if not opcao:
            print('Opção inválida!')
            continue
            
        if opcao == '1':
                nome = input('Nome: ')
                email = input('Email: ')
                telefone = input('Telefone: ')
                endereco = input('Endereço: ')
                adicionar_cliente(nome, email, telefone, endereco)
            
                
        elif opcao == '2':
            listar_clientes()
                
        elif opcao == '3':
            try:
                id = int(input('ID do Cliente: '))
                nome = input('Nome: ')
                email = input('Email: ')
                telefone = input('Telefone: ')
                endereco = input('Endreço: ')
                atualizar_cliente(id, nome, email, telefone, endereco)
            except:
                print('⚠️ ID inválido! Digite um número.')
                
        elif opcao == '4':
            try:
                id = int(input('ID Removido: '))
                deletar_cliente(id)
            except:
                print('⚠️ ID inválido! Digite um número.')
                
        elif opcao == '0':
            print('Você saiu do sistema!\n')
            break   
                
        else:
            print('⚠️ Opção inválida! Tente novamente.')
                
            
            
            
        
        
    