from testeMOCK import MockBD
import sys
sys.path.insert(0, '..')
from conexaoBD import *
from queries_matricula import *

class TestMedicoDB(MockBD):
    def test_matricula(self):
        retorno_esperado = [('Carla',), ('Ramonie',), ('Felipe',)]
        self.assertEqual(ler_matriculas(self.mock_db_config.get('bd')),
        retorno_esperado)
    def test_filtro_nome(self):
        retorno_esperado_1 = [('Carla',), ('Ramonie',)]
        retorno_esperado_2 = []
        self.assertEqual(ler_matriculas(self.mock_db_config.get('bd'), 'Carla'),
retorno_esperado_1)
        self.assertEqual(ler_matriculas(self.mock_db_config.get('bd'), 'Ramonie'),
        retorno_esperado_2)

 