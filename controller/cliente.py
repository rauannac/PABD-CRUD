#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, telefone, email):
    db.cur.execute("""
                   INSERT into public.tbusuarios (nome, telefone, email)
                   VALUES ('%s','%s','%s')
                   """ % (nome, telefone, email))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbusuarios
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def selecionar_id (id):
    db.cur.execute("""
            SELECT * FROM tbusuarios WERE id = '%s'
    """ % (id))
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def deletar (id):
    db.cur.execute("""
            DELETE FROM tbusuarios WHERE id = '%s'
        """ % (id))
    db.con.commit()