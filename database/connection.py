import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

#CONECTANDO AO BANCO DE DADOS
conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = conexao.cursor()
print("Conexão bem-sucedida!")