      Import sqlite3

From datetime import datetime

From database import conectar



Def adicionar_calculo(descricao, valor, tipo):

    Data_atual = datetime.now().strftime(“%Y-%m-%d %H:%M:%S”)

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“INSERT INTO calculos (descricao, valor, data, tipo) VALUES (?, ?, ?, ?)”,

                   (descricao, valor, data_atual, tipo))

    Conn.commit()

    Conn.close()



Def listar_calculos():

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“SELECT * FROM calculos”)

    Calculos = cursor.fetchall()

    Conn.close()

    Return calculos



Def editar_calculo(calculo_id, nova_descricao, novo_valor, novo_tipo):

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“UPDATE calculos SET descricao = ?, valor = ?, tipo = ? WHERE id = ?”,

                   (nova_descricao, novo_valor, novo_tipo, calculo_id))

    Conn.commit()

    Conn.close()



Def deletar_calculo(calculo_id):

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“DELETE FROM calculos WHERE id = ?”, (calculo_id,))

    Conn.commit()

    Conn.close()



Def calcular_lucro_prejuizo():

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“SELECT SUM(valor) FROM calculos WHERE tipo = ‘Lucro’”)

    Total_lucro = cursor.fetchone()[0] or 0.0

    Cursor.execute(“SELECT SUM(valor) FROM calculos WHERE tipo = ‘Prejuízo’”)

    Total_prejuizo = cursor.fetchone()[0] or 0.0

    Conn.close()

    Return total_lucro – total_prejuizo



Def adicionar_transacao_fixa(descricao, valor, data, tipo):

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“INSERT INTO transacoes_fixas (descricao, valor, data, tipo) VALUES (?, ?, ?, ?)”,

                   (descricao, valor, data, tipo))

    Conn.commit()

    Conn.close()



Def listar_transacoes_fixas():

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“SELECT * FROM transacoes_fixas”)

    Transacoes = cursor.fetchall()

    Conn.close()

    Return transacoes



Def calcular_produto_estimado(data):

    Conn = conectar()

    Cursor = conn.cursor()

    Cursor.execute(“SELECT SUM(valor) FROM transacoes_fixas WHERE tipo = ‘Lucro’ AND data <= ?”, (data,))

    Total_lucro = cursor.fetchone()[0] or 0.0

    Cursor.execute(“SELECT SUM(valor) FROM transacoes_fixas WHERE tipo = ‘Prejuízo’ AND data <= ?”, (data,))

    Total_prejuizo = cursor.fetchone()[0] or 0.0

    Conn.close()

    Return total_lucro – total_prejuizo



Def informar_gastos_extraordinarios(descricao, valor):

    Data_atual = datetime.now().strftime(“%Y-%m-%d %H:%M:%S”)

    Adicionar_calculo(descricao, valor, “Prejuízo”),

