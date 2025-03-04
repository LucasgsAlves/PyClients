import tkinter as tk
from tkinter import messagebox
from services.crud import adicionar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

janela = tk.Tk()
janela.title('Gerenciador de Clientes')
janela.geometry('300x300')
janela.configure(bg="#2C2F33")
janela.resizable(False, False)

label = tk.Label(janela, text='Bem-vindo!', font=('Arial', 16, 'bold'), bg="#2C2F33", fg="white")
label.pack(pady=5)

#Frame para organização dos botões
frame_btn = tk.Frame(janela, bg="#2C2F33")
frame_btn.pack(pady=10, padx=10, fill='both', expand=True)

#CRIANDO JANELA PARA ADICIONAR DADOS
def abrir_janela_adicionar():
    janela_adicionar = tk.Toplevel(janela)
    janela_adicionar.title('Adicionar Cliente')
    janela_adicionar.geometry('300x300')
    janela_adicionar.configure(bg="#2C2F33")
    janela_adicionar.resizable(False, False)
    
    #ENTRADA NOME
    tk.Label(janela_adicionar, text='Nome', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    entrada_nome = tk.Entry(janela_adicionar)
    entrada_nome.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #ENTRADA EMAIL
    tk.Label(janela_adicionar, text='Email', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold') ).pack(fill='x', padx=10, pady=2)
    entrada_email = tk.Entry(janela_adicionar)
    entrada_email.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #ENTRADA TELEFONE
    tk.Label(janela_adicionar, text='Telefone', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold') ).pack(fill='x', padx=10, pady=2)
    entrada_telefone = tk.Entry(janela_adicionar)
    entrada_telefone.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #ENTRADA ENDEREÇO
    tk.Label(janela_adicionar, text='Endereço', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold') ).pack(fill='x', padx=10, pady=2)
    entrada_endereco = tk.Entry(janela_adicionar)
    entrada_endereco.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #CONFIGURAÇÃO DE ADICIONAR CLIENTE
    def adicionar_cliente_tk():
        nome = entrada_nome.get()
        email = entrada_email.get()
        telefone = entrada_telefone.get()
        endereco = entrada_endereco.get()
        
        #VERIFICAÇÃO
        if nome and email and telefone and endereco:
            adicionar_cliente(nome, email, telefone, endereco)
            messagebox.showinfo('✅ Cliente adicionado com sucesso!')
        else:
            messagebox.showwarning('⚠️ ERRO', 'Todos os campos devem ser preenchidos!')
            
    #BOTÃO DE ADICIONAR CLIENTE AO BANCO DE DADOS
    btn_adicionar = tk.Button(janela_adicionar, text='Adicionar', bg='#caf0f8', command=adicionar_cliente_tk)
    btn_adicionar.pack(pady=10)

#BOTÃO DE ADICIONAR TELA INICIAL
btn_adicionar = tk.Button(frame_btn, text='Adicionar Cliente', bg='#caf0f8', command=abrir_janela_adicionar)
btn_adicionar.pack(pady=5,fill='both', expand=True)

#FUNÇÃO DE LISTAR CLIENTES
def abrir_janela_listar():
    #CHAMANDO FUNÇÃO
    clientes = listar_clientes()
    
    #CRIANDO JANELA NOVA
    janela_listar = tk.Toplevel(janela)
    janela_listar.title('Adicionar Cliente')
    janela_listar.geometry('330x300')
    janela_listar.configure(bg="#2C2F33")
    janela_listar.resizable(False, False)
    
    #CONFIGURAÇÃO DE CAIXA DE TEXTO ONDE SERÁ EXEBIDO AS INFO
    texto = tk.Text(janela_listar, height=25, width=50, bg="#F0F0F0")
    texto.pack(padx=10, pady=10)

    #LAÇO PARA IMPRIMIR TODOS OS NOMES COM FORMATAÇÃO
    for cliente in clientes:
        texto.insert(tk.END, f"ID: {cliente[0]}\nNome: {cliente[1]}\nEmail: {cliente[2]}\nTelefone: {cliente[3]}\nEndereço: {cliente[4]}\n{'-'*30}\n")

    #IMPEDINDO EDIÇÃO DE TEXTO
    texto.config(state=tk.DISABLED)
    
#BOTÃO DE LISTAR TELA INICIAL
btn_listar = tk.Button(frame_btn, text='Listar Cliente', bg='#ade8f4', command=abrir_janela_listar)
btn_listar.pack(pady=5,fill='both', expand=True)

#JANELA DE FUNÇÃO DE ATUALIZAR DADOS DO CLIENTE
def abrir_janela_atualizar():
    #CRIANDO JANELA DE LISTAR
    janela_atualizar = tk.Toplevel(janela)
    janela_atualizar.title('Atualizar Cliente')
    janela_atualizar.geometry('400x400')
    janela_atualizar.configure(bg="#2C2F33")
    janela_atualizar.resizable(False, False)
    
    #ENTRADA ID ATUALIZADO
    tk.Label(janela_atualizar, text='Digite o ID', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    selecionar_id= tk.Entry(janela_atualizar)
    selecionar_id.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #ENTRADA NOME ATUALIZADO
    tk.Label(janela_atualizar, text='Novo Nome', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    atualizar_nome = tk.Entry(janela_atualizar)
    atualizar_nome.pack(fill='x', padx=10, pady=5, ipady=3)

    #ENTRADA EMAIL ATUALIZADO
    tk.Label(janela_atualizar, text='Novo Email', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    atualizar_email = tk.Entry(janela_atualizar)
    atualizar_email.pack(fill='x', padx=10, pady=5, ipady=3)

    #ENTRADA TELEFONE ATUALIZADO
    tk.Label(janela_atualizar, text='Novo Telefone', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    atualizar_telefone = tk.Entry(janela_atualizar)
    atualizar_telefone.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #ENTRADA ENDEREÇO ATUALIZADO
    tk.Label(janela_atualizar, text='Novo Endereço', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    atualizar_endereco = tk.Entry(janela_atualizar)
    atualizar_endereco.pack(fill='x', padx=10, pady=5, ipady=3)
    
    #FUNÇÃO DE ATUALIZAR DADOS DO CLIENTE
    def atualizar_cliente_tk():
        try:
            id = int(selecionar_id.get())
        except ValueError:
            messagebox.showwarning('⚠️ Erro', 'ID inválido! Digite um número válido.')
            return
        
        id = selecionar_id.get()
        novo_nome = atualizar_nome.get()
        novo_email = atualizar_email.get()
        novo_telefone = atualizar_telefone.get()
        novo_endereco = atualizar_endereco.get()
        
        #VERIFICAÇÃO
        if novo_nome and novo_email and novo_telefone and novo_endereco and id:
            atualizar_cliente(id, novo_nome, novo_email, novo_telefone, novo_endereco)
            messagebox.showinfo('Sucesso', '✅ Cliente Atualizado com sucesso!')
            janela_atualizar.destroy()
        else:
           messagebox.showwarning('⚠️ ERRO', 'Todos os campos devem ser preenchidos!')  
    
    btn_atualizar = tk.Button(janela_atualizar, text='Atualizar', bg='#caf0f8', command=atualizar_cliente_tk)
    btn_atualizar.pack(pady=10)

#BOTÃO ATUALIZAR DADOS DO CLIENTE
btn_atualizar = tk.Button(frame_btn, text='Atualizar Cliente', bg='#90e0ef', command=abrir_janela_atualizar)
btn_atualizar.pack(pady=5,fill='both', expand=True)



def abrir_janela_deletar():
    #CRIANDO JANELA DE REMOÇÃO
    janela_deletar = tk.Toplevel(janela)
    janela_deletar.title('Deletar Cliente')
    janela_deletar.geometry('400x150')
    janela_deletar.configure(bg="#2C2F33")
    janela_deletar.resizable(False, False)
    
    #SELECIONANDO ID A SER REMOVIDO
    tk.Label(janela_deletar, text='Digite o ID', anchor='w', justify='left', bg="#2C2F33", fg="white", font=('Arial', 12, 'bold')).pack(fill='x', padx=10, pady=2)
    selecionar_id= tk.Entry(janela_deletar)
    selecionar_id.pack(fill='x', padx=10, pady=5, ipady=3)
    
    def deletar_cliente_tk():  
        try:
            id = int(selecionar_id.get()) 
        except ValueError:
            messagebox.showwarning('⚠️ Erro', 'ID inválido! Digite um número válido.')
            return
        
        id = selecionar_id.get()
        
        if id:
            deletar_cliente(id)
            messagebox.showinfo('Sucesso', '✅ Cliente Deletado com sucesso!')
            janela_deletar.destroy()
        else:
            messagebox.showwarning('⚠️ ERRO', 'Todos os campos devem ser preenchidos!')    
        
    btn_atualizar = tk.Button(janela_deletar, text='Deletar', bg='#caf0f8', command=deletar_cliente_tk)
    btn_atualizar.pack(pady=10)
          
#BOTÃO DE REMOÇÃO DO CLIENTE
btn_deletar = tk.Button(frame_btn, text='Deletar Cliente', bg='#48cae4', command=abrir_janela_deletar)
btn_deletar.pack(pady=5,fill='both', expand=True)


#BOTÃO DE SAIR DO SISTEMA
btn_sair = tk.Button(frame_btn, text='Sair', bg='#0096c7', command=janela.destroy)
btn_sair.pack(pady=5,fill='both', expand=True)


janela.mainloop()