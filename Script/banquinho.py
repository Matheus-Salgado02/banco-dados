import mysql.connector
import mysql.connector.types
from datetime import date


def connectar():
    conn = mysql.connector.connect(
        user="root",
        host="localhost",
        database="adotaarvore",
        password= None
    )
    
    cursor = conn.cursor() 
    return conn,cursor

    

#INSERTS
def insert_uf(nome, sigla):
    conn,cursor=connectar()
    comando = "INSERT INTO uf (id, nome, sigla) VALUES (null,%s,%s)"
    valores = (nome, sigla)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_bioma(nome, descricao):
    conn,cursor=connectar()
    comando = "INSERT INTO bioma (id, nome, descricao) VALUES (null,%s,%s)"
    valores = (nome, descricao)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_especie(nome, descricao, expectativa_vida, nome_cientifico):
    conn,cursor=connectar()
    comando = "INSERT INTO especie (id, nome, descricao, expectativa_vida, nome_cientifico) VALUES (null,%s,%s,%s,%s)"
    valores = (nome, descricao, expectativa_vida, nome_cientifico)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_bioma_especie(id_especie, id_bioma):
    conn,cursor=connectar()
    comando = "INSERT INTO bioma_especie (id_especie, id_bioma) VALUES (%s,%s)"
    valores = (id_especie, id_bioma)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_locais(bairro, cidade, complemento, numero, rua, id_UF, id_bioma, nome, descricao, croqui, area_total, tipo_plantio):
    conn,cursor=connectar()
    comando = "INSERT INTO locais \
    (id, bairro, cidade, complemento, numero, rua, id_UF, id_bioma, nome, descricao, croqui, area_total, tipo_plantio) \
    VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (bairro, cidade, complemento, numero, rua, id_UF, id_bioma, nome, descricao, croqui, area_total, tipo_plantio)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_funcinario(nome, bairro, cidade, complemento, numero, rua, cpf, id_UF, data_nascimento):
    conn,cursor=connectar()
    comando = "INSERT INTO funcionario (id, nome, bairro, cidade, complemento, numero, rua, cpf, id_UF, data_nascimento) \
    VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (nome, bairro, cidade, complemento, numero, rua, cpf, id_UF, data_nascimento)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_cliente(nome, bairro, cidade, complemento, numero, rua, cpf, id_UF,telefone,email):
    conn,cursor=connectar()
    comando = "INSERT INTO cliente \
    (id, nome, bairro, cidade, complemento, numero, rua, cpf, id_UF,telefone,email) \
    VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (nome, bairro, cidade, complemento, numero, rua, cpf, id_UF,telefone,email)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_arvore(id_cliente, id_especie, id_locais, cord_latitude, cord_longitude):
    conn,cursor=connectar()
    comando = "INSERT INTO arvore (id, id_cliente, id_especie, id_locais, cord_latitude, cord_longitude) VALUES \
    (null,%s,%s,%s,%s,%s)"
    valores = (id_cliente, id_especie, id_locais, cord_latitude, cord_longitude)
    cursor.execute(comando, valores)
    conn.commit()
    arvore_inserida=cursor.lastrowid
    cursor.close()
    conn.close()
    data_criacao = date(2024,7,16)
    print(data_criacao)
    insert_protocolo(data_criacao, arvore_inserida)

def insert_protocolo(data_criacao,id_arvore):
    conn,cursor=connectar()
    comando = """
    INSERT INTO protocolo (id, data_criacao, data_plantar, deferido, id_arvore, id_funcionario)
    VALUES (null, %s, null, 0, %s, null)
    """
    
    valores = (data_criacao,id_arvore)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

def insert_car(reserva_legal, apps, uso_terra, id_locais):
    conn,cursor=connectar()
    comando = "INSERT INTO car (id, reserva_legal, apps, uso_terra, id_locais) VALUES \
    (null,%s,%s,%s,%s)"
    valores = (reserva_legal, apps, uso_terra, id_locais)
    cursor.execute(comando, valores)
    conn.commit()
    cursor.close()
    conn.close()

#DELETE
def delete_entidade(table,entidade,logica,cond):
    conn,cursor=connectar()
    comando = f"DELETE FROM {table} WHERE {entidade} {logica} {cond}"
    cursor.execute(comando)
    conn.commit()
    row_cont = cursor.rowcount
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row_cont,row

#SELECT
def select(table):
    conn,cursor=connectar()
    comando = f"SELECT * FROM {table}"
    cursor.execute(comando)
    coluna_nome = cursor.column_names
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row,coluna_nome

#SELECT comando
def select_comando(comando):
    conn,cursor=connectar()
    cursor.execute(comando)
    coluna_nome = cursor.column_names
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row,coluna_nome



def select_cond(table,escolher,entidade,logica,cond):
    conn,cursor=connectar()
    comando = f"SELECT {escolher} FROM {table} WHERE {entidade} {logica} {cond}"
    cursor.execute(comando)
    coluna_nome = cursor.column_names
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row,coluna_nome

#UPDATE
def update(table,entidade,entlog,logica,cond):
    conn,cursor=connectar()
    comando = f"UPDATE {table} SET {entidade} WHERE {entlog} {logica} {cond}"
    cursor.execute(comando)
    conn.commit()
    row_cont = cursor.rowcount
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row,row_cont




