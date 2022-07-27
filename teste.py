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
                                    ('Carla'),
                                    ( 'Ramonie'),
                                    ( 'Felipe'))"""
                                        
                                        
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