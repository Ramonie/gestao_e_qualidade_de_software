from conexaoBD import *
def ler_matriculas(bd):
     return ler_bd(bd, "SELECT nome FROM matricula WHERE ativo = 1")
     
