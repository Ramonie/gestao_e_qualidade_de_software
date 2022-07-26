
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
        try:
            cursor.execute('''CREATE TABLE aluno 
                                (id_aluno int NOT NULL PRIMARY KEY, nome text NOT NULL)''')

            cursor.execute('''CREATE TABLE Disciplina 
                                (id_disciplina int NOT NULL PRIMARY KEY, nome text NOT NULL)''')   
        
                    #cursor.execute('CREATE TABLE  turma (id int NOT NULL PRIMARY KEY, nome text NOT NULL, turno text NOT NULL, id_disciplina int NOT NULL, FOREIGN KEY (id_disciplina) REFERENCES disciplina(id))')
            
                    #cursor.execute('CREATE TABLE matricula( id int  PRIMARY KEY, id_aluno int NOT NULL, id_turma int NOT NULL, FOREIGN KEY (id_aluno) REFERENCES aluno (id), FOREIGN KEY (id_turma) REFERENCES turma (id))')
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")  
        try:
                    
            
            cursor.execute("INSERT INTO aluno (id_aluno, nome) VALUES (1,'Carla'),(2, 'Ramonie')")
            cursor.execute("INSERT INTO disciplina (id_disciplina, nome) VALUES  (2011, 'Geografia')")
                    #cursor.execute(query_insert_matricula)
                    #cursor.execute(query_insert_turma)
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
                cursor.execute("DROP TABLE matricula")
                #cursor.execute("DROP TABLE turma")
                cursor.execute("DROP TABLE turma")

                con.commit()
                cursor.close()
                print("Removeu os dados das tabelas.")
            except sqlite3.Error as error:
                print("Banco de dados não existe. Erro na remoção do BD.", error)
            finally:
                desconectar(con)