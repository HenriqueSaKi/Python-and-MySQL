from typing import ValuesView
import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306 #Porta padrão do MySQL

con = MySQLdb.connect(host, user, password, db, port)

#Retorna o padrão, ou seja, tuplas
#c = con.cursor()

#Retorna um dicionário
c = con.cursor(MSQLdb.cursors.DictCursor)

def select (fields, tables, where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where
    c.execute(query)

    #Pega todos os resultados e junta em um
    return c.fetchall()

#Retorna uma tupla de tuplas
#print(select("nome, cpf", "alunos"))

#Printando o nome
print(result[0]["nome"])

def insert(values, table, fields=None):
    global c, con
    query = "INSERT INTO " + tabela
    if (fields): 
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    query = VALUES

    c.execute(query)
    con.commit()

values = [
    "DEFAULT, 'João Pereira', '2000-01-01', 'Av. das Pedras, 123', 'Betim", 'MG', '12345678911'
    "DEFAULT, 'Maria Pedro', '2000-01-01', 'Av. das Pedras, 123', 'Betim", 'MG', '12345678910'
    ]

insert(values, "alunos")
print(select("*", "alunos"))

def update(sets, table, where=None):
    global c, con
    query = "UPDATE " + table + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where
    
    #Para executar o comando
    c.execute(query)
    #Para confirmar que o comando foi executado
    con.commit()

update({"nome": "João Martins", "cidade": "Curitiba"}, "alunos", "id_aluno = 8")
print(select("*", "alunos", "id_aluno = 8"))

def delete(table, where):
    global c, con
    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

print(select("*", "alunos", "id_aluno = 9"))
print(delete("alunos", "id_aluno = 9"))
print(select("*", "alunos", "id_aluno = 9")) #Return NONE