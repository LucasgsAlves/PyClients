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
    janela_adicionar.geometry('300x350')
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
            messagebox.showwarning('ERRO', 'Todos os campos devem ser preenchidos!')
            
    #BOTÃO DE ADICIONAR CLIENTE AO BANCO DE DADOS
    btn_adicionar = tk.Button(janela_adicionar, text='Adicionar', bg='#caf0f8', command=adicionar_cliente)
    btn_adicionar.pack(pady=10)

#BOTÃO DE ADICIONAR TELA INICIAL
btn_adicionar = tk.Button(frame_btn, text='Adicionar Cliente', bg='#caf0f8', command=abrir_janela_adicionar)
btn_adicionar.pack(pady=5,fill='both', expand=True)

def abrir_janela_listar():
    #CHAMANDO FUNÇÃO
    clientes = listar_clientes()
    
    #CRIANDO JANELA NOVA
    janela_listar = tk.Toplevel(janela)
    janela_listar.title('Adicionar Cliente')
    janela_listar.geometry('400x350')
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



















#BOTÃO ATUALIZAR DADOS DO CLIENTE
btn_atualizar = tk.Button(frame_btn, text='Atualizar Cliente', bg='#90e0ef')
btn_atualizar.pack(pady=5,fill='both', expand=True)

#BOTÃO DE REMOÇÃO DO CLIENTE
btn_remover = tk.Button(frame_btn, text='Remover Cliente', bg='#48cae4')
btn_remover.pack(pady=5,fill='both', expand=True)

#BOTÃO DE SAIR DO SISTEMA
btn_sair = tk.Button(frame_btn, text='Sair', bg='#0096c7')
btn_sair.pack(pady=5,fill='both', expand=True)

janela.mainloop()