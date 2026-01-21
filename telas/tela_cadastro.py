import customtkinter as ctk
import os
import requests
from PIL import Image
from tkinter import messagebox

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master, db):
        # O master aqui será o main_frame da sua main.py
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.caminho_capa_atual = "assets/capas/default.png"

        # Configura a coluna única para centralizar os itens
        self.grid_columnconfigure(0, weight=1)
        
        self.setup_ui()

    def setup_ui(self):
        # 1. Título da Tela
        ctk.CTkLabel(self, text="📝 Cadastrar Novo Livro", font=("Arial", 24, "bold")).grid(row=0, column=0, pady=(0, 20))

        # 2. Seção ISBN (Entry + Botão lado a lado)
        isbn_frame = ctk.CTkFrame(self, fg_color="transparent")
        isbn_frame.grid(row=1, column=0, pady=5)
        
        self.entry_isbn = ctk.CTkEntry(isbn_frame, placeholder_text="Digite o ISBN", width=250)
        self.entry_isbn.pack(side="left", padx=5)
        
        self.btn_buscar = ctk.CTkButton(isbn_frame, text="🔍 Buscar", width=80, command=self.buscar_por_isbn)
        self.btn_buscar.pack(side="left", padx=5)

        # 3. Campos de Texto Básicos
        self.entry_titulo = ctk.CTkEntry(self, placeholder_text="Título do Livro", width=400)
        self.entry_titulo.grid(row=2, column=0, pady=5)

        self.entry_autor = ctk.CTkEntry(self, placeholder_text="Autor(es)", width=400)
        self.entry_autor.grid(row=3, column=0, pady=5)

        # 4. Novos Campos: Descrição e Status
        ctk.CTkLabel(self, text="Sinopse / Descrição:", font=("Arial", 12)).grid(row=4, column=0, pady=(10, 0))
        self.txt_descricao = ctk.CTkTextbox(self, width=400, height=80)
        self.txt_descricao.grid(row=5, column=0, pady=5)

        self.combo_status = ctk.CTkOptionMenu(self, values=["Quero Ler", "Lendo", "Lido"], width=200)
        self.combo_status.grid(row=6, column=0, pady=15)

        # 5. Preview da Capa
        self.label_preview = ctk.CTkLabel(self, text="Capa não selecionada", width=150, height=220, fg_color="gray20", corner_radius=8)
        self.label_preview.grid(row=7, column=0, pady=10)

        # 6. Botão de Ação Principal
        self.btn_salvar = ctk.CTkButton(self, text="Salvar no Acervo", fg_color="#2ecc71", hover_color="#27ae60",
                                        command=self.salvar_dados, width=200, height=40)
        self.btn_salvar.grid(row=8, column=0, pady=20)

    # --- Lógica das Funções (Aqui entram as APIs que já testamos) ---
    def buscar_por_isbn(self):
        # Aqui você insere a lógica do Google Books / Open Library que refatoramos
        pass

    def salvar_dados(self):
        # Aqui você coleta os dados e envia para self.db.adicionar_livro
        pass

    def baixar_e_exibir_capa(self, url, isbn):
        # Aqui você insere a lógica do Pillow para salvar e mostrar a imagem
        pass
