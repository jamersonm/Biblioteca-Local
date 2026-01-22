import customtkinter as ctk
from PIL import Image
import os

class TelaBiblioteca(ctk.CTkFrame):
    def __init__(self, parent, controller, db):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.db = db

        # Configuração da Grid do Frame Principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # --- 1. CABEÇALHO E DIVISOR (Padronizado) ---
        self.label_titulo_pagina = ctk.CTkLabel(
            self, text="Meu Acervo", font=("JetBrains Mono", 32, "bold")
        )
        self.label_titulo_pagina.grid(row=0, column=0, padx=20, pady=(25, 15), sticky="w")

        self.linha_divisora = ctk.CTkFrame(self, height=2, fg_color="#4C566A")
        self.linha_divisora.grid(row=1, column=0, padx=20, pady=(0, 30), sticky="ew")

        # --- 2. CONTAINER DE SCROLL ---
        self.scroll_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_container.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
        
        # Ajuste de Scroll para Linux (Arch)
        self.scroll_container._parent_canvas.bind_all("<Button-4>", lambda e: self.scroll_container._parent_canvas.yview_scroll(-1, "units"))
        self.scroll_container._parent_canvas.bind_all("<Button-5>", lambda e: self.scroll_container._parent_canvas.yview_scroll(1, "units"))

        self.carregar_catalogo()

    def carregar_catalogo(self):
        """Busca livros no banco e renderiza a grade de capas"""

        # Limpa o container caso já existam itens
        for widget in self.scroll_container.winfo_children():
            widget.destroy()

        livros = self.db.listar_todos() # Pega a lista do seu database.py

        colunas = 4 # Quantidade de capas por linha
        for i, livro in enumerate(livros):
            id_livro, isbn, titulo, autor, *_, caminho_capa, _, _, _, _, _, _, _ = livro
            
            # 1. Preparar a Imagem (Com a mesma lógica de moldura)
            try:
                if caminho_capa and os.path.exists(caminho_capa):
                    img_pil = Image.open(caminho_capa)
                else:
                    # Imagem padrão caso não tenha capa
                    img_pil = Image.new('RGB', (270, 380), color='#4C566A')
                
                # Criamos a imagem levemente menor que o botão para dar o efeito de moldura
                img_ctk = ctk.CTkImage(light_image=img_pil, size=(180, 260)) 

                # 2. Criar o Botão/Capa
                btn_capa = ctk.CTkButton(
                    self.scroll_container,
                    text="", 
                    image=img_ctk,
                    width=200,
                    height=280,
                    fg_color="#3B4252",      # Nord 1 (Fundo da moldura)
                    hover_color="#434C5E",   # Nord 2
                    corner_radius=12,
                    command=lambda id=id_livro: self.abrir_detalhes_livro(id)
                )
                
                # Posicionamento na Grid
                linha = i // colunas
                coluna = i % colunas
                btn_capa.grid(row=linha, column=coluna, padx=15, pady=15)

            except Exception as e:
                print(f"Erro ao carregar capa do livro {id_livro}: {e}")

    def abrir_detalhes_livro(self, id_livro):
        """Função que será chamada ao clicar na capa"""
        print(f"Abrindo detalhes do livro ID: {id_livro}")
