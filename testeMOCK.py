from unittest import TestCase
from sqlite3 import Cursor
from sqlite3 import query
import sys
sys.path.insert(0, '..')

from conexaoBD import *

BD = "TestBD.db"
class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()
#Turma: id (PK), nome, turno, id_disciplina (FK)
#Disciplina: id (PK), nome
#Aluno: id (PK), nome
#Matricula: id (PK), id_aluno (FK), id_turma (FK)
        query_create_turma= """CREATE TABLE turma (
                                id int NOT NULL PRIMARY KEY,
                                nome text NOT NULL,
                                turno text NOT NULL,
                                FOREIGN KEY (id_disciplina) REFERENCES disciplina(id)
                                )"""
        query_create_disciplina = """CREATE TABLE disciplina (
                                id int NOT NULL PRIMARY KEY,
                                nome text NOT NULL
                                )"""
        query_create_aluno = """CREATE TABLE aluno (
                                id int NOT NULL PRIMARY KEY,
                                nome text NOT NULL
                                )"""
        query_create_matricula = """CREATE TABLE matricula(
                                id int NOT NUL PRIMARY KEY,
                                FOREIGN KEY (id_aluno) REFERENCES aluno (id),
                                FOREIGN KEY (id_turma) REFERENCES turma (id)
                                )"""
    try:
        Cursor.execute(query_create_turma)
        Cursor.execute(query_create_disciplina)
        Cursor.execute(query_create_aluno)
        Cursor.execute(query_create_matricula)
        con.commit()
    except sqlite3.Error as error:
        print("Erro na criação das tabelas:", error)
    else:

#Popular o banco de dados de teste:
#Criar 4 turmas
#Sendo 2 delas de 'Geografia'
#Criar 4 disciplina
#Sendo uma delas 'Geografia' 
# Criar 8 alunos
# Sendo um deles 'Carla'
# Criar várias matrículas
# 'Carla' deve estar matriculada em 2 turmas

#Turma: id (PK), nome, turno, id_disciplina (FK)
#Disciplina: id (PK), nome
#Aluno: id (PK), nome
#Matricula: id (PK), id_aluno (FK), id_turma (FK)

        print("Criação das tabelas: OK")
        query_insert_turma = """INSERT INTO turma (id , nome, turno, id_disciplina)
                                VALUES
                                (1, 'Geografia I', 'Matutino'),
                                (2, 'Estatistica', 'Matutino'),
                                (3, 'Geografia II', 'Matutino'),
                                (4, 'APOO', 'Matutino')
                                )"""
        query_insert_disciplina = """INSERT INTO  disciplina(id, nome) VALUES
                                (2011, 'Geografia '),
                                (2010, 'Geografia '),
                                (3060, 'Matematica I'),
                                (3061, 'Analise e Projeto Orientado a Objetos')
                                )"""
        query_insert_aluno = """INSERT INTO aluno (id, nome) VALUES (
                                (1, 'Carla'),
                                (2, 'Ramonie'),
                                (3, 'Felipe'),
                                (4, 'Josué'),
                                (5, 'Lucas'),
                                (6, 'Luiz'),
                                (7, 'Emerson'),
                                (8, 'Nathan')
                                )"""
        query_insert_matricula = """
                                    """
    try:
        Cursor.execute(query_insert_medico)
        Cursor.execute(query_insert_horas_plantao)
        con.commit()
    except sqlite3.Error as error:
        print("Erro na inserção de dados:", error)
    else:
        print("Inserção dos dados: OK")
        cursor.close()
        desconectar(con)
        testconfig ={
        'bd': BD
        }
        cls.mock_db_config = testconfig
@classmethod
def tearDownClass(cls):
    print("TearDown")
    con = conectar(BD)
    cursor = con.cursor()
    try:
        cursor.execute("DROP TABLE Usuario")
        cursor.execute("DROP TABLE Turma")
        cursor.execute("DROP TABLE Disciplina")
        con.commit()
        cursor.close()
        print("Removeu os dados das tabelas.")
    except sqlite3.Error as error:
        print("Banco de dados não existe. Erro na remoção do BD.", error)
    finally:
        desconectar(con)