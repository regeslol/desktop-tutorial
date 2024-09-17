Import sqlite3



Def conectar():

    Return sqlite3.connect(‘financas.db’)



Def criar_tabelas():

    Conn = conectar()

    Cursor = conn.cursor()



    Cursor.execute(‘’’

    CREATE TABLE IF NOT EXISTS calculos (

        Id INTEGER PRIMARY KEY AUTOINCREMENT,

        Descricao TEXT NOT NULL,

        Valor REAL NOT NULL,

        Data TEXT NOT NULL,

        Tipo TEXT NOT NULL 

    )

    ‘’’)

    Cursor.execute(‘’’

    CREATE TABLE IF NOT EXISTS transacoes_fixas (

        Id INTEGER PRIMARY KEY AUTOINCREMENT,

        Descricao TEXT NOT NULL,

        Valor REAL NOT NULL,

        Data TEXT NOT NULL,

        Tipo TEXT NOT NULL

    )

    ‘’’)

    Conn.commit(

   Conn.close()

