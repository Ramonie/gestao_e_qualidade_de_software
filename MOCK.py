
from unittest import TestCase
import sys 
sys.path.insert(0, '..')

from conexaoBD import *
import sqlite3
BD = "TestBD.db"
class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()
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
            cursor.execute(query_create_turma)
            cursor.execute(query_create_disciplina)
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_matricula)
            #cursor.execute('''CREATE TABLE aluno 
            #                    (id_aluno INTERGER NOT NULL PRIMARY KEY, nome text NOT NULL)''')

            #cursor.execute('''CREATE TABLE Disciplina 
             #                   (id_disciplina INTERGER NOT NULL PRIMARY KEY, nome text NOT NULL)''')   
        
                    #cursor.execute('CREATE TABLE  turma (id int NOT NULL PRIMARY KEY, nome text NOT NULL, turno text NOT NULL, id_disciplina int NOT NULL, FOREIGN KEY (id_disciplina) REFERENCES disciplina(id))')
            
                    #cursor.execute('CREATE TABLE matricula( id int  PRIMARY KEY, id_aluno int NOT NULL, id_turma int NOT NULL, FOREIGN KEY (id_aluno) REFERENCES aluno (id), FOREIGN KEY (id_turma) REFERENCES turma (id))')
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")  
        try:
            query_insert_matricula = """ INSERT INTO matricula (id, id_aluno, id_turma)
                                         VALUES (10,1,1),(11,2,3),(12,1,3)"""

            query_insert_turma = """INSERT INTO turma (id , nome, turno, id_disciplina)
                                        VALUES ((1, 'Geografia ', 'Matutino', 2011), 
                                        (2, 'Estatistica', 'Matutino', 3060), 
                                        (3, 'Geografia ', 'Matutino', 2010), 
                                        (4, 'APOO', 'Matutino', 3061))"""
            query_insert_disciplina = """ INSERT INTO disciplina (id, nome)
                                         VALUES (
                                        (2011, 'Geografia  '),
                                        (2010, 'Geografia '),
                                        (3060, 'Matematica I'),
                                        (3061, 'Analise e Projeto Orientado a Objetos'))"""
            query_insert_aluno = """INSERT INTO aluno (id, nome) VALUES (
                                    (1,'Carla'),
                                    ( 2,'Ramonie'),
                                    ( 3,'Felipe'))"""
                                                
            #cursor.execute("INSERT INTO aluno (id_aluno, nome) VALUES (1,'Carla'),(2, 'Ramonie')")
            #cursor.execute("INSERT INTO disciplina (id_disciplina, nome) VALUES  (2011, 'Geografia')")
            cursor.execute(query_insert_matricula)
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_disciplina)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            con = desconectar(BD)
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
                cursor.execute("DROP TABLE aluno")
                #cursor.execute("DROP TABLE turma")
                cursor.execute("DROP TABLE disciplina")

                con.commit()
                cursor.close()
                print("Removeu os dados das tabelas.")
            except sqlite3.Error as error:
                print("Banco de dados não existe. Erro na remoção do BD.", error)
            finally:
                desconectar(con)