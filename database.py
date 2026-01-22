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
                volume TEXT,
                editora TEXT,
                paginas INTEGER,
                caminho_capa TEXT,
                genero TEXT,
                data_termino TEXT,
                preco REAL,
                avaliacao INTEGER,
                status TEXT,
                descricao TEXT,
                comentarios TEXT
            )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def adicionar_livro(self, dados):
        """
        Insere os dados coletados da interface no SQLite.
        """
        query = """
        INSERT INTO livros (
            isbn, titulo, autor, ano_publicacao, idioma, nacionalidade_autor,
            volume, editora, paginas, caminho_capa, genero, 
            data_termino, preco, avaliacao, status, descricao, comentarios
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Mapeamento sem o campo 'edicao'
        valores = (
            dados.get('isbn'),
            dados.get('titulo'),
            dados.get('autor'),
            dados.get('ano'),
            dados.get('idioma'),
            dados.get('nacionalidade'),
            dados.get('volume'),
            dados.get('editora'),
            dados.get('paginas'),
            dados.get('capa'),
            dados.get('genero'),
            dados.get('data'),
            dados.get('preco'),
            dados.get('avaliacao'),
            dados.get('status'),
            dados.get('descricao'),
            dados.get('comentarios')
        )

        try:
            self.cursor.execute(query, valores)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False # ISBN Duplicado
        except Exception as e:
            print(f"Erro ao inserir no banco: {e}")
            return False

    def listar_todos(self):
        """
        Consulta todos os livros cadastrados no banco de dados.
        Retorna uma lista de tuplas com todas as colunas da tabela.
        """
        try:
            # Selecionamos todas as colunas para garantir que o desmembramento
            # (id, isbn, titulo, autor, etc.) na tela funcione corretamente.
            self.cursor.execute("SELECT * FROM livros ORDER BY titulo ASC")
            livros = self.cursor.fetchall()
            return livros
        except Exception as e:
            print(f"Erro ao listar livros: {e}")
            return []
