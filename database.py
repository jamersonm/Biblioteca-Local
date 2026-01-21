import sqlite3
from datetime import datetime

class BibliotecaDB:
    def __init__(self, db_name="biblioteca.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        query = """
            CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT UNIQUE,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER,
            idioma TEXT,
            nacionalidade_autor TEXT,
            serie TEXT,
            paginas INTEGER,
            caminho_capa TEXT,
            genero TEXT,
            data_termino TEXT,
            preco REAL,
            avaliacao INTEGER
        )
        """
        self.cursor.execute(query)
        self.conn.commit()


    def adicionar_livro(self, dados):
        """
        Recebe um dicionário com os dados e insere no banco.
        """
        query = """
        INSERT INTO livros (
            isbn, titulo, autor, ano_publicacao, idioma, nacionalidade_autor,
            serie, paginas, caminho_capa, genero, data_termino, preco, avaliacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        # O uso de '?' previne SQL Injection, uma prática de segurança essencial
        self.cursor.execute(query, (
            dados.get('isbn'), dados['titulo'], dados['autor'], dados['ano'], dados['idioma'],
            dados['nacionalidade'], dados['serie'], dados['paginas'],
            dados['capa'], dados['genero'], dados['data'], dados['preco'],
            dados['avaliacao']
        ))
        self.conn.commit()

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM livros")
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()

