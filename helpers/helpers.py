import mysql.connector
from database.connection import conexao

#Criando função de formatação de texto
def padronizar_nome(nome):
    return nome.strip().title()

def remover_espacos(texto):
    return texto.strip()

def converter_maiusculo(texto):
    return texto.upper().strip()

def converter_minusculo(texto):
    return texto.lower().strip()

