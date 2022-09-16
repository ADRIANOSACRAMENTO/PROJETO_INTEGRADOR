#importar biblioteca de conexao ao dados
import _sqlit3 as lite
from datetime import datetime

#criar conexao banco
con = lite.connect('dados.db')

#funcao para inserir inventario
def inserir_from(i):
    with con:
        cur = con.cursor()
        query = "INSERT INVENTARIO(NOME,LOCAL,DESCRICAO,MARCA,DATA_DA_COMPRA, " \
                 "VALOR_DA_COMPRA,SERIE,IMAGEM) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

#funcao para deletar um registro/ linha /tupla
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM INVENTARIO WHERE ID=?,"
        cur.execute(query, i)

#funcao para atualizar um regisro/LINHA/TUPLA
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE INVENTARIO SET NOME=?, LOCAL=?, DESCRICAO=?, MARCA=?," \
                "DATA_DA_COMPRA=?, VALOR_DA_COMPRA=?, SERIE=?, IMAGEM=? WHERE ID=?" ,
         cur.execute(query, i)

#funcao para ver todos os itens do inventario
def ver_form():
    lista_itens = []
    with con:
        cur = CO.CURSOR()
        cur.execute ("SELECT * FROM INVENTARIO ORDER BY NOME")
        rows = cur.fetchall()
        for rows in rows :
            lista_itens.append(row)
       return lista_itens

