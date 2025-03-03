import mysql.connector
from helpers.helpers import padronizar_nome, remover_espacos, converter_maiusculo, converter_minusculo
from database.connection import conexao

#CRIANDO FUNÇÃO DE ADICIONAR CLIENTE
def adicionar_cliente(nome, email, telefone, endereco):
    try:
        cursor = conexao.cursor()
        
        nome = padronizar_nome(nome)
        email = converter_minusculo(email)
        telefone = remover_espacos(telefone)
        endereco = converter_maiusculo(endereco)
        
        sql = "INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, telefone, endereco)
        
        cursor.execute(sql, valores)
        conexao.commit()
        print('✅ Cliente cadastrado com sucesso!')
    except mysql.connector.Error as erro:
        print(f'⚠️ Erro ao cadastrar o cliente: {erro}')
    finally:
        cursor.close()

#CRIANDO FUNÇÃO DE LISTAR CLIENTES
def listar_clientes():
    cursor = conexao.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for cliente in resultado:
        print(cliente)
    cursor.close() 
    
#CRIANDO FUNÇÃO DE ATUALIZAR CLIENTE
def atualizar_cliente(id, novo_nome, novo_email, novo_telefone, novo_endereco):
    try:
        cursor = conexao.cursor()
        
        novo_nome = padronizar_nome(novo_nome)
        novo_email = converter_minusculo(novo_email)
        novo_telefone = remover_espacos(novo_telefone)
        novo_endereco = converter_maiusculo(novo_endereco)
        
        
        sql = "UPDATE clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE id = %s"
        valores = (novo_nome, novo_email, novo_telefone, novo_endereco, id)
        
        cursor.execute(sql, valores)
        conexao.commit()
        print('✅ Cliente atualizado com sucesso!')
        
    except mysql.connector.Error as erro:
        print(f'⚠️ Erro ao atualizar o cliente: {erro}')
    finally:
        cursor.close()
        
#DELETAR CLIENTE
def deletar_cliente(id):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        valores = (id,)
        
        cursor.execute(sql, valores)
        conexao.commit()
        print('✅ Cliente removido com sucesso!')
    except mysql.connector.Error as erro:
        print(f'⚠️ Erro ao remover o cliente: {erro}')
    finally:
        cursor.close()
        
        